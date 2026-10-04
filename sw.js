// Service worker của CareerLift: cho phép cài app và mở khi không có mạng.
// Trang chính: lấy bản mới từ mạng trước, mất mạng thì dùng bản đã lưu (nên không cần đổi CACHE mỗi lần sửa index.html).
// Font và thư viện đọc CV từ CDN: dùng bản đã lưu, đồng thời cập nhật ngầm. Gọi AI và Google Drive không bao giờ được lưu.
const CACHE = "careerlift-v1", RUNTIME = "careerlift-rt-v1";
const SHELL = ["./", "index.html", "manifest.webmanifest", "icon-192.png", "icon-512.png", "icon-maskable-512.png", "apple-touch-icon.png"];
const CDN = ["fonts.googleapis.com", "fonts.gstatic.com", "cdnjs.cloudflare.com"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE && k !== RUNTIME).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener("fetch", e => {
  const req = e.request;
  if(req.method !== "GET") return;
  const url = new URL(req.url);
  if(url.origin === location.origin){
    if(req.mode === "navigate" || url.pathname.endsWith("/index.html")){
      e.respondWith(fetch(req).then(res => {
        if(res.ok){ const copy = res.clone(); caches.open(CACHE).then(c => c.put("index.html", copy)); }
        return res;
      }).catch(() => caches.match("index.html", {ignoreSearch: true})));
      return;
    }
    e.respondWith(caches.match(req, {ignoreSearch: true}).then(hit => hit || fetch(req)));
    return;
  }
  if(CDN.includes(url.hostname)){
    e.respondWith(caches.open(RUNTIME).then(c => c.match(req).then(hit => {
      const net = fetch(req).then(res => { if(res.ok || res.type === "opaque") c.put(req, res.clone()); return res; }).catch(() => hit);
      return hit || net;
    })));
  }
});
