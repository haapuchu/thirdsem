// ACADEMIC TREE PORTAL JAVASCRIPT
// Handles checklist persistence, live search filter, dark/light mode toggle, side navigation drawer, and offline service worker

(function() {
  // Theme logic
  function getEffectiveTheme() {
    const saved = localStorage.getItem('theme');
    if (saved) return saved;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    const btn = document.getElementById('theme-toggle');
    if (btn) {
      btn.textContent = theme === 'dark' ? 'light' : 'dark';
    }
  }

  // Bind on DOM load
  document.addEventListener('DOMContentLoaded', () => {
    // Theme Button
    const btn = document.getElementById('theme-toggle');
    if (btn) {
      btn.textContent = getEffectiveTheme() === 'dark' ? 'light' : 'dark';
      btn.addEventListener('click', () => {
        const current = getEffectiveTheme();
        const next = current === 'dark' ? 'light' : 'dark';
        localStorage.setItem('theme', next);
        applyTheme(next);
      });
    }

    // Side Drawer Navigation
    const menuBtn = document.getElementById('menu-toggle');
    const drawer = document.getElementById('side-drawer');
    const overlay = document.getElementById('drawer-overlay');
    const closeBtn = document.getElementById('drawer-close');

    function openDrawer() {
      if (!drawer || !overlay) return;
      drawer.classList.add('open');
      overlay.classList.add('open');
      drawer.setAttribute('aria-hidden', 'false');
      overlay.setAttribute('aria-hidden', 'false');
      if (menuBtn) menuBtn.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
    }

    function closeDrawer() {
      if (!drawer || !overlay) return;
      drawer.classList.remove('open');
      overlay.classList.remove('open');
      drawer.setAttribute('aria-hidden', 'true');
      overlay.setAttribute('aria-hidden', 'true');
      if (menuBtn) menuBtn.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    }

    if (menuBtn) {
      menuBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        if (drawer && drawer.classList.contains('open')) {
          closeDrawer();
        } else {
          openDrawer();
        }
      });
    }

    if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
    if (overlay) overlay.addEventListener('click', closeDrawer);

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && drawer && drawer.classList.contains('open')) {
        closeDrawer();
      }
    });

    // Highlight active link in drawer based on current location
    try {
      const currentNorm = window.location.pathname.replace(/\/index\.html$/, '').replace(/\/$/, '');
      const drawerLinks = document.querySelectorAll('.side-drawer a');
      drawerLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (!href) return;
        const linkUrl = new URL(href, window.location.href);
        const linkNorm = linkUrl.pathname.replace(/\/index\.html$/, '').replace(/\/$/, '');
        if (linkNorm === currentNorm) {
          link.classList.add('drawer-active-item');
        }
      });
    } catch (_) {}

    // Interactive Checkboxes
    const checkboxes = document.querySelectorAll('.checklist-item input[type="checkbox"]');
    checkboxes.forEach((cb, idx) => {
      const pageKey = window.location.pathname + '_cb_' + idx;
      const saved = localStorage.getItem(pageKey);
      if (saved === 'true') {
        cb.checked = true;
        cb.closest('.checklist-item').classList.add('checked');
      }

      cb.addEventListener('change', () => {
        localStorage.setItem(pageKey, cb.checked);
        if (cb.checked) {
          cb.closest('.checklist-item').classList.add('checked');
        } else {
          cb.closest('.checklist-item').classList.remove('checked');
        }
      });
    });

    // Directory Tree Search
    const filterInput = document.getElementById('tree-filter');
    if (filterInput) {
      filterInput.addEventListener('input', (e) => {
        const term = e.target.value.toLowerCase().trim();
        const treeNodes = document.querySelectorAll('.tree-node-subject');
        
        treeNodes.forEach(node => {
          const text = node.innerText.toLowerCase();
          if (text.includes(term)) {
            node.style.display = '';
          } else {
            node.style.display = 'none';
          }
        });
      });
    }

    // Mobile PDF note
    const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
    if (isMobile) {
      const mobileNotes = document.querySelectorAll('.mobile-fallback-note');
      mobileNotes.forEach(el => {
        el.style.display = 'block';
      });
    }
  });

  // Offline Access: Service Worker Registration
  if ('serviceWorker' in navigator && (window.location.protocol === 'http:' || window.location.protocol === 'https:')) {
    window.addEventListener('load', () => {
      let rootPath = './';
      const script = document.querySelector('script[src*="app.js"]');
      if (script) {
        const src = script.getAttribute('src');
        if (src.includes('../../')) {
          rootPath = '../../';
        } else if (src.includes('../')) {
          rootPath = '../';
        }
      }
      navigator.serviceWorker.register(rootPath + 'sw.js', { scope: rootPath }).catch(() => {
        // Fallback root registration
        navigator.serviceWorker.register('/sw.js').catch(() => {});
      });
    });
  }
})();
