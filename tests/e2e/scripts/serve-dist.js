#!/usr/bin/env node

const fs = require('node:fs')
const http = require('node:http')
const path = require('node:path')

const DIST_DIR = path.resolve(__dirname, '../../../dist')
const PORT = Number(process.argv[2] || process.env.PORT || 4173)

const MIME_TYPES = {
  '.css': 'text/css; charset=utf-8',
  '.gif': 'image/gif',
  '.html': 'text/html; charset=utf-8',
  '.ico': 'image/x-icon',
  '.jpeg': 'image/jpeg',
  '.jpg': 'image/jpeg',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.svg': 'image/svg+xml',
  '.txt': 'text/plain; charset=utf-8',
  '.webp': 'image/webp',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.xml': 'application/xml; charset=utf-8',
}

if (!fs.existsSync(DIST_DIR)) {
  console.error(`dist directory not found: ${DIST_DIR}`)
  process.exit(1)
}

function resolveFile(requestPath) {
  let pathname = requestPath.split('?')[0].split('#')[0]

  try {
    pathname = decodeURIComponent(pathname)
  } catch {
    return null
  }

  if (pathname === '/') {
    pathname = '/index.html'
  }

  const candidates = []

  if (pathname.endsWith('/')) {
    candidates.push(`${pathname}index.html`)
  }

  candidates.push(pathname)

  if (!path.extname(pathname)) {
    candidates.push(`${pathname}.html`)
  }

  for (const candidate of candidates) {
    const absolutePath = path.resolve(DIST_DIR, `.${candidate}`)

    if (!absolutePath.startsWith(DIST_DIR)) {
      continue
    }

    if (fs.existsSync(absolutePath) && fs.statSync(absolutePath).isFile()) {
      return absolutePath
    }
  }

  return null
}

const server = http.createServer((req, res) => {
  const method = req.method || 'GET'

  if (method !== 'GET' && method !== 'HEAD') {
    res.writeHead(405, { 'Content-Type': 'text/plain; charset=utf-8' })
    res.end('Method Not Allowed')
    return
  }

  const filePath = resolveFile(req.url || '/')

  if (!filePath) {
    res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' })
    res.end('Not Found')
    return
  }

  const ext = path.extname(filePath).toLowerCase()
  const contentType = MIME_TYPES[ext] || 'application/octet-stream'

  res.writeHead(200, {
    'Cache-Control': 'no-store',
    'Content-Type': contentType,
  })

  if (method === 'HEAD') {
    res.end()
    return
  }

  fs.createReadStream(filePath)
    .on('error', () => {
      if (!res.headersSent) {
        res.writeHead(500, { 'Content-Type': 'text/plain; charset=utf-8' })
      }
      res.end('Internal Server Error')
    })
    .pipe(res)
})

server.listen(PORT, '127.0.0.1', () => {
  // eslint-disable-next-line no-console
  console.log(`Serving dist from ${DIST_DIR} at http://127.0.0.1:${PORT}`)
})

for (const signal of ['SIGINT', 'SIGTERM']) {
  process.on(signal, () => {
    server.close(() => process.exit(0))
  })
}
