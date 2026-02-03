#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const file = path.join(__dirname, '..', 'index.html');
let html = fs.readFileSync(file, 'utf8');

// Find the Custom Styles block: <!-- Custom Styles --> ... <style> ... </style>
const startMarker = '    <!-- Custom Styles -->';
const styleOpen = '<style>';
const styleClose = '</style>';
const startIdx = html.indexOf(startMarker);
if (startIdx === -1) {
  console.error('Could not find Custom Styles comment');
  process.exit(1);
}
const styleStart = html.indexOf(styleOpen, startIdx);
const cssStart = styleStart + styleOpen.length;
const cssEnd = html.indexOf(styleClose, cssStart);
if (styleStart === -1 || cssEnd === -1) {
  console.error('Could not find style block boundaries');
  process.exit(1);
}
let css = html.slice(cssStart, cssEnd);

// Minify: remove comments, then collapse whitespace
css = css.replace(/\/\*[\s\S]*?\*\//g, '');
css = css.replace(/\s+/g, ' ');
css = css.replace(/\s*{\s*/g, '{');
css = css.replace(/\s*}\s*/g, '}');
css = css.replace(/\s*:\s*/g, ':');
css = css.replace(/\s*;\s*/g, ';');
css = css.replace(/\s*,\s*/g, ',');
css = css.trim();

const endOfBlock = cssEnd + styleClose.length;
const newBlock = startMarker + '\n    <style>' + css + '\n    </style>';
const newHtml = html.slice(0, startIdx) + newBlock + html.slice(endOfBlock);
fs.writeFileSync(file, newHtml);
console.log('Minified inline CSS: ' + (cssEnd - cssStart) + ' -> ' + css.length + ' chars');
