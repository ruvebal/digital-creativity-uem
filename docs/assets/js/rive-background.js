/**
 * Mount Rive .riv scenes as decorative backgrounds.
 * Requires /assets/vendor/rive/rive.js (+ local wasm). SVG/static fallback when
 * prefers-reduced-motion, missing canvas, or load failure.
 *
 * Base URL must include Jekyll site.baseurl (e.g. /digital-creativity-uem).
 * Prefer body[data-base-url]; else derive from this script's src so wasm is
 * never requested at bare /assets/vendor/rive/rive.wasm under a subpath host.
 */
(function () {
  'use strict';

  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function resolveBase() {
    const fromBody = String(document.body?.dataset?.baseUrl || '').replace(/\/$/, '');
    if (fromBody) return fromBody;
    const script = document.currentScript
      || document.querySelector('script[src*="rive-background.js"]');
    const src = script?.getAttribute?.('src') || '';
    const m = src.match(/^(.*)\/assets\/js\/rive-background\.js(?:\?.*)?$/i);
    if (m) return m[1];
    // Last resort: strip after /assets/ on an already-absolute data-rive-src.
    const riv = document.querySelector('[data-rive-src]')?.getAttribute('data-rive-src') || '';
    const m2 = riv.match(/^(.*)\/assets\//);
    return m2 ? m2[1] : '';
  }

  const base = resolveBase();
  const wasmUrl = `${base}/assets/vendor/rive/rive.wasm`;
  const wasmFallbackUrl = `${base}/assets/vendor/rive/rive_fallback.wasm`;

  function withBase(path) {
    if (!path) return '';
    if (/^https?:\/\//i.test(path)) return path;
    if (base && path.startsWith(base + '/')) return path;
    if (path.startsWith('/')) return `${base}${path}`;
    return path;
  }

  function loadRuntime() {
    if (window.rive?.Rive) return Promise.resolve(window.rive);
    return new Promise((resolve, reject) => {
      const existing = document.querySelector('script[data-rive-runtime]');
      if (existing) {
        existing.addEventListener('load', () => resolve(window.rive));
        existing.addEventListener('error', reject);
        return;
      }
      const s = document.createElement('script');
      s.src = `${base}/assets/vendor/rive/rive.js`;
      s.async = true;
      s.dataset.riveRuntime = '1';
      s.onload = () => resolve(window.rive);
      s.onerror = reject;
      document.head.appendChild(s);
    });
  }

  function mountOne(host, src, fallback) {
    if (!host || host.dataset.riveMounted === '1') return;
    host.dataset.riveMounted = '1';
    const rivSrc = withBase(src);
    const fb = withBase(fallback);

    if (reduced || !rivSrc) {
      if (fb) host.style.backgroundImage = `url(${JSON.stringify(fb)})`;
      return;
    }

    const canvas = document.createElement('canvas');
    canvas.className = 'rive-background__canvas';
    canvas.setAttribute('aria-hidden', 'true');
    host.appendChild(canvas);

    loadRuntime()
      .then((riveApi) => {
        if (riveApi.RuntimeLoader?.setWasmUrl) riveApi.RuntimeLoader.setWasmUrl(wasmUrl);
        if (riveApi.RuntimeLoader?.setWasmFallbackUrl) {
          riveApi.RuntimeLoader.setWasmFallbackUrl(wasmFallbackUrl);
        } else if (riveApi.RuntimeLoader) {
          riveApi.RuntimeLoader.wasmFallbackURL = wasmFallbackUrl;
        }
        const instance = new riveApi.Rive({
          src: rivSrc,
          canvas,
          autoplay: true,
          onLoad: () => {
            host.classList.add('is-rive-live');
            try {
              instance.resizeDrawingSurfaceToCanvas();
            } catch (_) { /* older runtimes */ }
          },
          onLoadError: () => {
            host.classList.remove('is-rive-live');
            canvas.remove();
            if (fb) host.style.backgroundImage = `url(${JSON.stringify(fb)})`;
          },
        });
        host._riveInstance = instance;
        const ro = new ResizeObserver(() => {
          try {
            instance.resizeDrawingSurfaceToCanvas();
          } catch (_) { /* ignore */ }
        });
        ro.observe(host);
      })
      .catch(() => {
        canvas.remove();
        if (fb) host.style.backgroundImage = `url(${JSON.stringify(fb)})`;
      });
  }

  function mountDeck() {
    if (!window.Reveal) return;
    const paint = () => {
      document.querySelectorAll('.reveal .slides > section[data-rive-src]').forEach((section) => {
        const bg = typeof Reveal.getSlideBackground === 'function'
          ? Reveal.getSlideBackground(section)
          : null;
        const host = bg?.querySelector?.('.slide-background-content') || bg || section;
        if (!host) return;
        host.classList.add('rive-background');
        mountOne(host, section.getAttribute('data-rive-src'), section.getAttribute('data-rive-fallback'));
      });
    };
    if (Reveal.isReady?.()) paint();
    else Reveal.on?.('ready', paint);
    Reveal.on?.('slidechanged', paint);
  }

  function mountPageArt() {
    document.querySelectorAll('[data-rive-src].page-art, .page-art[data-rive-src]').forEach((el) => {
      el.classList.add('rive-background');
      mountOne(el, el.getAttribute('data-rive-src'), el.getAttribute('data-rive-fallback'));
    });
  }

  function boot() {
    mountPageArt();
    mountDeck();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
