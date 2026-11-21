// ACADEMIC TREE PORTAL JAVASCRIPT
// Handles checklist persistence, live search filter, dark/light mode toggle, and offline service worker

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
