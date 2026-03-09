#!/usr/bin/env node
/**
 * Local static server with Cache-Control + gzip for Lighthouse audits.
 * Production uses S3/CloudFront with cache set in deploy workflow.
 * Usage: node server.js [port]   (default: 8080)
 */
const http = require('http');
const fs = require('fs');
const path = require('path');
const zlib = require('zlib');

const PORT = parseInt(process.env.PORT || process.argv[2] || '8080', 10);
const ROOT = path.join(__dirname);

const MIME = {
  '.html': 'text/html',
  '.css': 'text/css',
  '.js': 'application/javascript',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.webp': 'image/webp',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf',
  '.eot': 'application/vnd.ms-fontobject',
  '.txt': 'text/plain',
  '.xml': 'application/xml',
};

const LONG_CACHE = 'public, max-age=31536000, immutable';
const HTML_CACHE = 'public, max-age=3600, must-revalidate';
const METADATA_CACHE = 'public, max-age=86400, must-revalidate';

function getCacheControl(filePath) {
  const ext = path.extname(filePath);
  const base = path.basename(filePath);
  if (ext === '.html') {
    return HTML_CACHE;
  }
  if (base === 'robots.txt' || base === 'sitemap.xml' || base === 'humans.txt') {
    return METADATA_CACHE;
  }
  return LONG_CACHE;
}

const server = http.createServer((req, res) => {
  let urlPath = req.url.split('?')[0] || '/';
  if (urlPath === '/') urlPath = '/index.html';
  const filePath = path.join(ROOT, path.normalize(urlPath).replace(/^(\.\.(\/|\\|$))+/, ''));

  if (!filePath.startsWith(ROOT)) {
    res.writeHead(403);
    res.end('Forbidden');
    return;
  }

  fs.stat(filePath, (err, stat) => {
    if (err || !stat.isFile()) {
      if (urlPath.endsWith('/')) {
        const index = path.join(filePath, 'index.html');
        return fs.stat(index, (e, s) => {
          if (e || !s || !s.isFile()) {
            res.writeHead(404);
            res.end('Not Found');
          } else {
            serveFile(req, index, res);
          }
        });
      }
      res.writeHead(404);
      res.end('Not Found');
      return;
    }

    serveFile(req, filePath, res);
  });
});

const COMPRESSIBLE = new Set([
  'text/html', 'text/css', 'text/javascript', 'application/javascript',
  'application/json', 'text/plain', 'text/xml', 'application/xml', 'image/svg+xml',
]);

function serveFile(req, filePath, res) {
  const ext = path.extname(filePath);
  const contentType = MIME[ext] || 'application/octet-stream';
  const cacheControl = getCacheControl(filePath);
  const acceptEncoding = (req.headers && req.headers['accept-encoding']) || '';
  const useGzip = COMPRESSIBLE.has(contentType) && acceptEncoding.includes('gzip');

  const stream = fs.createReadStream(filePath);
  stream.on('error', () => {
    res.writeHead(500);
    res.end('Error');
  });
  const headers = {
    'Content-Type': contentType,
    'Cache-Control': cacheControl,
    'cf-email-decoding': 'off',
    'Vary': 'Accept-Encoding',
  };
  if (useGzip) {
    headers['Content-Encoding'] = 'gzip';
    res.writeHead(200, headers);
    stream.pipe(zlib.createGzip({ level: 6 })).pipe(res);
  } else {
    res.writeHead(200, headers);
    stream.pipe(res);
  }
}

server.listen(PORT, () => {
  console.log(`Server running at http://127.0.0.1:${PORT}/`);
  console.log('Static assets: Cache-Control max-age=31536000, immutable; HTML/CSS/JS/SVG: gzip');
  console.log('For Lighthouse cache/compression audits, run the audit against this URL.');
});
