#!/usr/bin/env bash
# IndexNow submitter for tibexa.com — instantly notifies Bing, Yandex, Copilot, Seznam, etc.
# (Google does NOT use IndexNow; for Google use Search Console → Request Indexing.)
#
# Setup: a <key>.txt file must be live at https://tibexa.com/<key>.txt (already committed).
# Usage:
#   ./indexnow-submit.sh                 # submits the default content set below
#   ./indexnow-submit.sh URL1 URL2 ...   # submits the given URLs
set -euo pipefail

HOST="tibexa.com"
cd "$(dirname "$0")"

KEYFILE=$(ls -1 *.txt 2>/dev/null | grep -E '^[a-f0-9]{8,128}\.txt$' | head -1 || true)
[ -z "${KEYFILE:-}" ] && { echo "ERROR: IndexNow key file (<hex>.txt) not found in $(pwd)"; exit 1; }
KEY="${KEYFILE%.txt}"
KEYLOC="https://${HOST}/${KEYFILE}"

if [ "$#" -gt 0 ]; then
  URLS=("$@")
else
  URLS=(
    "https://tibexa.com/blog-en-iyi-ihracat-danismanlik-firmalari.html"
    "https://tibexa.com/blog-en-iyi-ai-lead-generation-sirketleri.html"
    "https://tibexa.com/blog-en-iyi-b2b-musteri-bulma-hizmetleri.html"
    "https://tibexa.com/blog-pazara-giris-danismani-secimi.html"
    "https://tibexa.com/blog-uctan-uca-yurt-disi-satis-gelistirme.html"
    "https://tibexa.com/blog-yapay-zeka-ihracat-alici-bulma.html"
    "https://tibexa.com/blog-nitelikli-ihracat-lead.html"
    "https://tibexa.com/blog.html"
  )
fi

JSON_URLS=$(printf '"%s",' "${URLS[@]}"); JSON_URLS="[${JSON_URLS%,}]"
BODY=$(printf '{"host":"%s","key":"%s","keyLocation":"%s","urlList":%s}' "$HOST" "$KEY" "$KEYLOC" "$JSON_URLS")

echo "Submitting ${#URLS[@]} URLs to IndexNow (key: ${KEY})..."
curl -s -w "\nHTTP %{http_code}\n" -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json; charset=utf-8" \
  --data "$BODY"
