/** PurgeCSS: main.css içinden HTML/JS'te kullanılmayan stilleri kaldır */
module.exports = {
  content: [
    'index.html',
    'blog.html',
    'careers.html',
    'legal.html',
    'assets/js/*.js'
  ],
  css: ['assets/css/main.css'],
  output: 'assets/css/',
  safelist: {
    standard: [
      'lang-tr',
      'lang-en',
      'hidden',
      'active',
      'sticky',
      'stat-satisfaction-en',
      'stat-satisfaction-tr'
    ],
    deep: [/^lni/, /^wow/],
    greedy: [/^animate-/]
  },
  rejected: false,
  rejectedCss: false
};
