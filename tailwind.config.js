/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './revenue-infrastruc-43.html',
    './case-*.html',
    './marketing-agency-67.html',
  ],
  theme: {
    extend: {
      colors: {
        bg: '#000000',
        surface: '#0A0A0A',
        surface2: '#141414',
        textmain: '#FFFFFF',
        textsec: '#A1A1AA',
        borderline: '#27272A',
      },
      fontFamily: {
        sans: ['"Geist Sans"', 'sans-serif'],
        mono: ['"Geist Mono"', 'monospace'],
      },
      letterSpacing: {
        tightest: '-0.04em',
        tech: '0.08em',
      },
    },
  },
  plugins: [],
}
