// Lightweight Service Worker for Offline Academic Portal Access
const CACHE_NAME = 'academic-portal-v1';

const STATIC_ASSETS = [
  './',
  './index.html',
  './css/style.css',
  './js/app.js',
  './discrete/index.html',
  './discrete/assignments/index.html',
  './dld/index.html',
  './dld/assignments/index.html',
  './dld/practical-lab-record/index.html',
  './ppl/index.html',
  './ppl/assignments/index.html',
  './ppl/practical-lab-record/index.html',
  './dev-tools/index.html',
  './dev-tools/assignments/index.html',
  './dev-tools/practical-lab-record/index.html',
  './dsa/index.html',
  './dsa/assignments/index.html',
  './dsa/practical-lab-record/index.html',
  './feedback-control-systems/index.html',
  './feedback-control-systems/assignments/index.html'
];

// Install: Cache static pages & core assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(STATIC_ASSETS);
    }).then(() => self.skipWaiting())
  );
});

// Activate: Clean up old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch: Network-first with cache fallback (ensures fresh updates online, works offline)
self.addEventListener('fetch', (event) => {
  // Only handle GET requests
  if (event.request.method !== 'GET') return;

  event.respondWith(
    fetch(event.request)
      .then((networkResponse) => {
        // Cache valid responses
        if (networkResponse && networkResponse.status === 200) {
          const responseToCache = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseToCache);
          });
        }
        return networkResponse;
      })
      .catch(() => {
        // Offline fallback
        return caches.match(event.request).then((cachedResponse) => {
          if (cachedResponse) {
            return cachedResponse;
          }
          // If request is an HTML navigation, fallback to root index
          if (event.request.mode === 'navigate') {
            return caches.match('./index.html') || caches.match('/index.html');
          }
        });
      })
  );
});
