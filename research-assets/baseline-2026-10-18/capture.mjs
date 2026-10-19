// Full-page baseline renders in a throwaway headless Chrome (lazy images loaded by scrolling first).
// Usage: node capture.mjs https://solarityai.com <output folder>  (needs Chrome at the path below and Node 22+)
import { spawn } from 'node:child_process';
import { mkdtempSync, mkdirSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const [origin, outDir] = process.argv.slice(2);
const routes = ['/', '/apps/', '/apps/looks-max/', '/apps/iq-max/', '/apps/sleep-max/', '/apps/fitness-max/', '/platform/', '/company/', '/investors-partners/', '/careers/', '/contact/', '/404.html'];
const jobs = [];
for (const w of [360, 390, 768, 1024, 1440]) for (const r of routes) jobs.push({ r, w, h: w < 768 ? 800 : 900 });
for (const [w, h] of [[1280, 800], [1920, 1080]]) for (const r of ['/', '/investors-partners/']) jobs.push({ r, w, h });
for (const w of [390, 1440]) for (const r of routes) jobs.push({ r, w, h: w < 768 ? 800 : 900, reduced: true });
mkdirSync(outDir, { recursive: true });
const profile = mkdtempSync(join(process.env.SCRATCH || tmpdir(), 'chrome-'));
const port = 9300 + Math.floor(Math.random() * 500);
const proc = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', ['--headless=new', `--remote-debugging-port=${port}`, `--user-data-dir=${profile}`, '--no-first-run', '--hide-scrollbars', 'about:blank'], { stdio: 'ignore' });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
let target;
for (let i = 0; i < 50 && !target; i++) { try { target = (await (await fetch(`http://127.0.0.1:${port}/json/list`)).json()).find((t) => t.type === 'page'); } catch (_) {} if (!target) await sleep(200); }
const ws = new WebSocket(target.webSocketDebuggerUrl);
await new Promise((r) => ws.addEventListener('open', r, { once: true }));
let id = 0; const pending = new Map(); const events = [];
ws.addEventListener('message', (m) => { const msg = JSON.parse(m.data); if (msg.id && pending.has(msg.id)) { pending.get(msg.id)(msg); pending.delete(msg.id); } else if (msg.method) events.push(msg); });
const send = (method, params = {}) => new Promise((r) => { const n = ++id; pending.set(n, r); ws.send(JSON.stringify({ id: n, method, params })); });
const evaluate = async (expression) => (await send('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true })).result?.result?.value;
const waitLoad = async () => { const start = events.length; for (let i = 0; i < 150; i++) { if (events.slice(start).some((e) => e.method === 'Page.loadEventFired')) return; await sleep(100); } };
const index = [];
try {
  await send('Page.enable'); await send('Runtime.enable');
  for (const job of jobs) {
    await send('Emulation.setDeviceMetricsOverride', { width: job.w, height: job.h, deviceScaleFactor: 1, mobile: job.w < 768 });
    await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: job.reduced ? 'reduce' : 'no-preference' }] });
    const loaded = waitLoad(); await send('Page.navigate', { url: origin + job.r }); await loaded;
    await evaluate('document.fonts.ready.then(() => true)');
    const height = await evaluate('document.scrollingElement.scrollHeight');
    for (let y = 0; y < height; y += job.h) { await evaluate(`window.scrollTo(0, ${y}); true`); await sleep(250); }
    await evaluate('window.scrollTo(0, 0); Promise.all([...document.images].filter(i => !i.complete).map(i => new Promise(r => { i.onload = i.onerror = r; setTimeout(r, 3000); }))).then(() => true)');
    await sleep(400);
    const full = await evaluate('document.scrollingElement.scrollHeight');
    const shot = await send('Page.captureScreenshot', { format: 'jpeg', quality: 70, captureBeyondViewport: true, clip: { x: 0, y: 0, width: job.w, height: full, scale: 1 } });
    const slug = job.r === '/' ? 'home' : job.r.replace(/\.html$/, '').replace(/^\/|\/$/g, '').replace(/\//g, '-');
    const file = `${slug}-${job.w}x${job.h}${job.reduced ? '-reduced-motion' : ''}.jpg`;
    writeFileSync(join(outDir, file), Buffer.from(shot.result.data, 'base64'));
    const overflow = await evaluate('document.scrollingElement.scrollWidth > innerWidth');
    index.push({ route: job.r, width: job.w, viewportHeight: job.h, reducedMotion: !!job.reduced, pageHeight: full, horizontalOverflow: overflow, file });
    console.log(file, full);
  }
  writeFileSync(join(outDir, 'index.json'), JSON.stringify({ source: origin, captured: process.env.STAMP, renders: index }, null, 2) + '\n');
} finally { ws.close(); proc.kill(); await sleep(500); try { rmSync(profile, { recursive: true, force: true }); } catch (_) {} }
