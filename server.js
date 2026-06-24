const http = require('http');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { URL } = require('url');

const ROOT = __dirname;
const PORT = process.env.PORT || 80;
const R2_BUCKET = process.env.PLUSVIBE_REPORT_R2_BUCKET || process.env.R2_BUCKET || 'hermes-autoreport';
const R2_PREFIX = (process.env.PLUSVIBE_REPORT_R2_PREFIX || 'plusvibe').replace(/^\/+|\/+$/g, '');
const R2_ENDPOINT = (process.env.CLOUDFLARE_S3_API_ENDPOINT || '').replace(/\/+$/g, '');
const R2_ACCESS_KEY = process.env.CLOUDFLARE_ACCESS_KEY_ID || process.env.CLOUDFLARE_R2_ACCESS_KEY_ID || '';
const R2_SECRET_KEY = process.env.CLOUDFLARE_SECRET_ACCESS_KEY || process.env.CLOUDFLARE_R2_SECRET_ACCESS_KEY || '';

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.xml': 'application/xml; charset=utf-8',
  '.txt': 'text/plain; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.webp': 'image/webp',
  '.avif': 'image/avif',
  '.ico': 'image/x-icon',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf',
  '.eot': 'application/vnd.ms-fontobject',
  '.pdf': 'application/pdf',
};

function hmac(key, msg) {
  return crypto.createHmac('sha256', key).update(msg, 'utf8').digest();
}

function sha256Hex(data) {
  return crypto.createHash('sha256').update(data).digest('hex');
}

function encodeKey(key) {
  return key.split('/').map(part => encodeURIComponent(part)).join('/');
}

function signR2Get(key) {
  if (!R2_ENDPOINT || !R2_ACCESS_KEY || !R2_SECRET_KEY || !R2_BUCKET) {
    throw new Error('R2 env missing: CLOUDFLARE_S3_API_ENDPOINT, CLOUDFLARE_ACCESS_KEY_ID, CLOUDFLARE_SECRET_ACCESS_KEY, PLUSVIBE_REPORT_R2_BUCKET');
  }
  const endpoint = new URL(R2_ENDPOINT);
  const host = endpoint.host;
  const basePath = endpoint.pathname.replace(/\/+$/g, '');
  const canonicalUri = `${basePath}/${encodeURIComponent(R2_BUCKET)}/${encodeKey(key)}`;
  const url = `${endpoint.protocol}//${host}${canonicalUri}`;

  const now = new Date();
  const amzDate = now.toISOString().replace(/[:-]|\.\d{3}/g, '');
  const dateStamp = amzDate.slice(0, 8);
  const payloadHash = 'UNSIGNED-PAYLOAD';
  const canonicalHeaders = `host:${host}\nx-amz-content-sha256:${payloadHash}\nx-amz-date:${amzDate}\n`;
  const signedHeaders = 'host;x-amz-content-sha256;x-amz-date';
  const canonicalRequest = ['GET', canonicalUri, '', canonicalHeaders, signedHeaders, payloadHash].join('\n');
  const algorithm = 'AWS4-HMAC-SHA256';
  const credentialScope = `${dateStamp}/auto/s3/aws4_request`;
  const stringToSign = [algorithm, amzDate, credentialScope, sha256Hex(canonicalRequest)].join('\n');
  const kDate = hmac(Buffer.from('AWS4' + R2_SECRET_KEY, 'utf8'), dateStamp);
  const kRegion = hmac(kDate, 'auto');
  const kService = hmac(kRegion, 's3');
  const kSigning = hmac(kService, 'aws4_request');
  const signature = crypto.createHmac('sha256', kSigning).update(stringToSign, 'utf8').digest('hex');
  const authorization = `${algorithm} Credential=${R2_ACCESS_KEY}/${credentialScope}, SignedHeaders=${signedHeaders}, Signature=${signature}`;
  return { url, headers: { Host: host, 'x-amz-content-sha256': payloadHash, 'x-amz-date': amzDate, Authorization: authorization } };
}

function send(res, status, body, headers = {}) {
  res.writeHead(status, headers);
  res.end(body);
}

function send404(res) {
  const custom404 = path.join(ROOT, '404.html');
  if (fs.existsSync(custom404)) {
    send(res, 404, fs.readFileSync(custom404), { 'Content-Type': 'text/html; charset=utf-8' });
  } else {
    send(res, 404, '404 Not Found\n', { 'Content-Type': 'text/plain; charset=utf-8' });
  }
}

function isBlockedProbe(pathname) {
  return /^\/(wp-admin|wp-login|wp-content|wp-includes|wordpress|xmlrpc\.php|wp-cron\.php)/i.test(pathname)
    || /\.(php|asp|aspx|jsp|cgi)$/i.test(pathname)
    || /^\/(\.env|\.git|\.aws|admin|login|phpmyadmin|mysql|backup|config\.json|\.well-known\/security\.txt)/i.test(pathname);
}

function serveStatic(req, res, pathname) {
  if (isBlockedProbe(pathname)) return send(res, 410, 'Gone\n', { 'Content-Type': 'text/plain; charset=utf-8' });

  let decoded;
  try { decoded = decodeURIComponent(pathname); } catch { return send404(res); }
  if (decoded === '/') decoded = '/index.html';
  const full = path.resolve(ROOT, '.' + decoded);
  if (!full.startsWith(ROOT + path.sep) && full !== ROOT) return send404(res);

  let file = full;
  if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
  if (!fs.existsSync(file) || !fs.statSync(file).isFile()) return send404(res);

  const ext = path.extname(file).toLowerCase();
  const headers = { 'Content-Type': MIME[ext] || 'application/octet-stream' };
  if (ext === '.html') headers['Cache-Control'] = 'public, no-cache, must-revalidate';
  else if (/\.(jpg|jpeg|png|gif|ico|svg|webp|avif|css|js|woff|woff2|ttf|eot)$/i.test(file)) headers['Cache-Control'] = 'public, max-age=2592000, immutable';
  fs.createReadStream(file).pipe(res.writeHead(200, headers));
}

function proxyR2(req, res, pathname) {
  if (req.method !== 'GET' && req.method !== 'HEAD') return send(res, 405, 'Method Not Allowed\n');
  let rel = pathname.replace(/^\/plusvibe\/?/, '');
  if (!rel || rel.endsWith('/')) rel += 'index.html';
  if (rel.includes('..')) return send404(res);
  const key = `${R2_PREFIX}/${rel}`;

  let signed;
  try { signed = signR2Get(key); }
  catch (err) { return send(res, 500, `R2 proxy not configured: ${err.message}\n`, { 'Content-Type': 'text/plain; charset=utf-8' }); }

  const upstream = new URL(signed.url);
  const client = upstream.protocol === 'https:' ? require('https') : require('http');
  const proxyReq = client.request({
    hostname: upstream.hostname,
    port: upstream.port || (upstream.protocol === 'https:' ? 443 : 80),
    path: upstream.pathname,
    method: req.method,
    headers: signed.headers,
  }, proxyRes => {
    const headers = { ...proxyRes.headers };
    delete headers['transfer-encoding'];
    headers['Cache-Control'] = proxyRes.statusCode === 200 ? 'public, no-cache, must-revalidate' : 'no-cache';
    res.writeHead(proxyRes.statusCode || 502, headers);
    proxyRes.pipe(res);
  });
  proxyReq.on('error', err => send(res, 502, `R2 upstream error: ${err.message}\n`, { 'Content-Type': 'text/plain; charset=utf-8' }));
  proxyReq.end();
}

const server = http.createServer((req, res) => {
  let url;
  try {
    url = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
  } catch {
    // Bozuk istek yolu (ör. bot'ların gönderdiği "//") tüm process'i düşürmesin.
    return send(res, 400, 'Bad Request\n', { 'Content-Type': 'text/plain; charset=utf-8' });
  }
  if (url.pathname === '/healthz') return send(res, 200, 'ok\n', { 'Content-Type': 'text/plain; charset=utf-8' });
  if (url.pathname === '/plusvibe' || url.pathname.startsWith('/plusvibe/')) return proxyR2(req, res, url.pathname);
  return serveStatic(req, res, url.pathname);
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`tibexa website listening on :${PORT}`);
});

// Son güvenlik ağı: yakalanmamış bir hata process'i çökertip siteyi düşürmesin.
process.on('uncaughtException', err => {
  console.error('uncaughtException (yutuldu):', err && err.stack ? err.stack : err);
});
