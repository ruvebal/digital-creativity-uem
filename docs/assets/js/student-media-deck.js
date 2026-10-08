(() => {
  // Digital Creativity student deck (PHASE-EX5).
  //
  // v2 decks are pre-rendered by scripts/render-decks.mjs: every slide, its
  // background, caption, alt text and speaker notes are already in the HTML.
  // This script only enhances them: Reveal, the card toggle, Lab timer, and
  // printable-card back-link swap.
  //
  // Legacy decks (no schema_version, e.g. how-to-pass / image-morphology) ship
  // an empty #slides; for them only, the slides are built from content.json at
  // runtime (legacyLoad below). No timestamp cache-bust; no hard-coded base.
  //
  // Base URL: body[data-base-url] (Jekyll site.baseurl). Pages without it fall
  // back to the part of data-content-url before "/tracks/".
  document.documentElement.classList.remove('no-js');
  document.documentElement.classList.add('js');

  const body = document.body;
  const slidesRoot = document.getElementById('slides');
  const contentUrl = body.dataset.contentUrl || '';
  const base = String(body.dataset.baseUrl ?? (contentUrl.includes('/tracks/') ? contentUrl.split('/tracks/')[0] : ''))
    .replace(/\/$/, '');
  const lessonUrl = body.dataset.lessonUrl || '';
  const params = new URLSearchParams(window.location.search);

  const escapeHtml = (value) => String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;');

  // -------------------------------------------------------------------------
  // Enhancements (all decks)
  // -------------------------------------------------------------------------

  const formatTime = (seconds) => `${Math.floor(seconds / 60)}:${String(seconds % 60).padStart(2, '0')}`;

  /** Lab timer: start/pause + reset on every section[data-timer]. */
  const addTimers = () => {
    slidesRoot.querySelectorAll('section[data-timer]').forEach((section) => {
      if (section.querySelector('.slide-timer')) return;
      const total = Math.max(1, parseInt(section.dataset.timer, 10) || 180);
      let left = total;
      let handle = null;
      const box = document.createElement('div');
      box.className = 'slide-timer';
      box.innerHTML = '<button type="button" class="slide-timer__toggle"></button>'
        + '<button type="button" class="slide-timer__reset" aria-label="Reset timer">↺</button>'
        + '<output class="slide-timer__time" aria-live="polite"></output>';
      const toggle = box.querySelector('.slide-timer__toggle');
      const reset = box.querySelector('.slide-timer__reset');
      const time = box.querySelector('.slide-timer__time');
      const draw = () => {
        time.textContent = left > 0 ? formatTime(left) : 'Time';
        toggle.textContent = handle ? 'Pause' : (left === total ? `Start ${formatTime(total)}` : 'Resume');
        box.classList.toggle('slide-timer--done', left === 0);
      };
      const stop = () => { if (handle) window.clearInterval(handle); handle = null; };
      toggle.addEventListener('click', () => {
        if (handle) { stop(); draw(); return; }
        if (left === 0) left = total;
        handle = window.setInterval(() => {
          left = Math.max(0, left - 1);
          if (left === 0) stop();
          draw();
        }, 1000);
        draw();
      });
      reset.addEventListener('click', () => { stop(); left = total; draw(); });
      draw();
      section.append(box);
    });
  };

  /** Reading-card toggle: hides the card and caption so the whole image shows. */
  const addCardToggle = () => {
    const controls = document.createElement('div');
    controls.className = 'student-media-controls';
    controls.innerHTML = '<button type="button" data-media-toggle aria-pressed="true" aria-label="Show or hide reading card" title="Show or hide reading card">◉</button>';
    document.body.append(controls);
    controls.querySelector('[data-media-toggle]').addEventListener('click', (event) => {
      const hidden = body.classList.toggle('student-media-card-hidden');
      event.currentTarget.setAttribute('aria-pressed', String(!hidden));
    });
  };

  /** Back link: lesson by default; printable card when the slide names one. */
  const bindBackLink = () => {
    const backLink = document.getElementById('deck-back');
    if (!backLink) return null;
    const update = () => {
      const current = typeof Reveal !== 'undefined' && Reveal.getCurrentSlide ? Reveal.getCurrentSlide() : null;
      const cardHref = current?.getAttribute('data-card-href') || '';
      backLink.href = cardHref || lessonUrl || backLink.getAttribute('href') || '#';
      backLink.textContent = cardHref ? '← Printable card' : (lessonUrl.includes('master-lectures') ? '← Back to master lecture' : '← Back to lesson');
      backLink.setAttribute('aria-label', cardHref ? 'Back to printable card' : 'Back to lesson');
    };
    return update;
  };

  const startReveal = (afterSync) => {
    addTimers();
    addCardToggle();
    const updateBack = bindBackLink();
    Reveal.initialize({
      hash: true,
      slideNumber: true,
      transition: 'slide',
      backgroundTransition: 'fade',
      width: 1280,
      height: 720,
      margin: 0.055,
      minScale: 0.2,
      maxScale: 1.35,
      showNotes: params.has('show-notes'),
    });
    const sync = () => {
      if (afterSync) afterSync();
      if (updateBack) updateBack();
    };
    Reveal.on('ready', sync);
    Reveal.on('slidechanged', sync);
  };

  // -------------------------------------------------------------------------
  // Legacy runtime path (decks without pre-rendered sections only)
  // -------------------------------------------------------------------------

  const geometricalBase = `${base}/assets/images/fractal-pass-track`;
  const geometricalCycle = [
    'uem-henon-pass-01-structure-2fc3613c22a1.svg',
    'uem-henon-pass-02-threshold-c378606cc29b.svg',
    'uem-henon-pass-03-branching-46681e3d02cd.svg',
    'uem-henon-pass-04-practice-1ab1247ed3af.svg',
    'uem-henon-pass-05-feedback-903832404a06.svg',
    'uem-henon-pass-06-coherence-a8444d20854d.svg',
  ];
  const diagramFile = 'uem-diagram-fallback-2fc3613c22a1.svg';
  const diagramUrl = `${base}/assets/images/fractal-triangles/${diagramFile}`;
  const svgHash = (file) => (file.match(/-([0-9a-f]{8,})\.svg$/) || [])[1] || '';

  const citationHref = (href) => {
    const value = String(href || '');
    if (!value || value.startsWith('#') || /^(?:https?:|mailto:|\/\/)/i.test(value)) return value;
    if (base && value.startsWith(`${base}/`)) return value;
    return `${base}${value.startsWith('/') ? value : `/${value}`}`;
  };

  const cleanTitle = (title) => String(title || '')
    .replace(/^File:/i, '')
    .replace(/\s*\[[^\]]*\]\s*$/g, '')
    .replace(/\.(?:jpe?g|png|gif|svg|webp|tiff?)$/i, '')
    .trim();

  const legacyCaption = (asset) => {
    const title = cleanTitle(asset.title || asset.alt_text || 'Untitled image');
    const author = String(asset.author || asset.credit_line || '').trim();
    const source = String(asset.canonical_source_url || asset.source || '').trim();
    return [
      `<span class="slide-caption__title">${escapeHtml(title)}</span>`,
      author ? `<span>${escapeHtml(author)}</span>` : '',
      asset.licence ? (asset.licence_url
        ? `<a href="${escapeHtml(asset.licence_url)}" target="_blank" rel="noopener">${escapeHtml(asset.licence)}</a>`
        : `<span>${escapeHtml(asset.licence)}</span>`) : '',
      /^https?:/i.test(source) ? `<a href="${escapeHtml(source)}" target="_blank" rel="noopener">Source</a>` : '',
    ].filter(Boolean).join(' · ');
  };
  const svgCaption = (label, file) => `<span class="slide-caption__title">${escapeHtml(label)}</span>`
    + ` · <span class="slide-caption__hash">#${escapeHtml(svgHash(file))}</span> · <span>Original course SVG</span>`;

  const isGeometrical = (slide) => slide.background_kind === 'geometrical'
    || ['analysis_opener', 'lab_opener', 'workshop_opener', 'outro', 'retrieval'].includes(slide.slide_role);

  const backgroundUrlBySection = new WeakMap();
  const paintBackgrounds = () => {
    slidesRoot.querySelectorAll(':scope > section').forEach((section) => {
      const url = backgroundUrlBySection.get(section);
      const bg = url && typeof Reveal.getSlideBackground === 'function' ? Reveal.getSlideBackground(section) : null;
      const node = bg?.querySelector?.('.slide-background-content') || bg;
      if (!node) return;
      node.style.backgroundImage = `url(${JSON.stringify(url)})`;
      node.style.backgroundSize = 'cover';
      node.style.backgroundPosition = 'center';
      node.style.backgroundRepeat = 'no-repeat';
    });
  };

  const legacyBuild = (data) => {
    const assets = new Map((data.assets || []).map((asset) => [asset.media_slot_id, asset]));
    let geometricalIndex = 0;
    slidesRoot.innerHTML = '';
    data.slides.forEach((slide) => {
      const asset = slide.media_slot_id ? assets.get(slide.media_slot_id) : null;
      let url;
      let captionHtml;
      let alt = '';
      if (isGeometrical(slide)) {
        const file = geometricalCycle[geometricalIndex % geometricalCycle.length];
        geometricalIndex += 1;
        url = `${geometricalBase}/${file}`;
        captionHtml = svgCaption('Course geometric background', file);
      } else if (asset?.asset_url) {
        url = citationHref(asset.asset_url);
        captionHtml = legacyCaption(asset);
        alt = asset.alt_text || '';
      } else if (slide.background_kind === 'none') {
        url = '';
        captionHtml = '';
      } else {
        url = diagramUrl;
        captionHtml = svgCaption('Course diagram · geometric fallback', diagramFile);
      }
      const section = document.createElement('section');
      section.setAttribute('data-background-color', '#0b1220');
      if (slide.slide_role) section.setAttribute('data-slide-role', slide.slide_role);
      if (slide.portfolio_bound) section.setAttribute('data-portfolio-bound', 'true');
      if (['lab_exercise', 'workshop_work'].includes(slide.slide_role)) section.setAttribute('data-timer', '180');
      if (slide.card_link?.href) section.setAttribute('data-card-href', citationHref(slide.card_link.href));
      section.innerHTML = `
        <div class="student-media-slide">
          <p class="student-media-slide__unit">${escapeHtml(data.unit_label)}</p>
          <h1>${escapeHtml(slide.heading)}</h1>
          <p class="student-media-slide__sentence">${escapeHtml(slide.sentence || '')}</p>
          ${slide.quote ? `<blockquote class="student-media-slide__quote"><p>${escapeHtml(slide.quote)}</p></blockquote>` : ''}
          ${slide.citation ? `<p class="student-media-slide__citation"><a href="${escapeHtml(citationHref(slide.citation.href))}">${escapeHtml(slide.citation.label)}</a></p>` : ''}
          ${slide.prompt ? `<p class="student-media-slide__prompt">${escapeHtml(slide.prompt)}</p>` : ''}
          ${slide.portfolio_trace ? `<p class="student-media-slide__prompt">${escapeHtml(slide.portfolio_trace)}</p>` : ''}
        </div>
        ${alt ? `<p class="sr-only">Image: ${escapeHtml(alt)}</p>` : ''}
        ${captionHtml ? `<p class="slide-caption">${captionHtml}</p>` : ''}`;
      if (url) backgroundUrlBySection.set(section, url);
      slidesRoot.append(section);
    });
  };

  const legacyLoad = () => {
    slidesRoot.innerHTML = '<section data-background-color="#0b1220"><div class="student-media-slide"><h1>Loading deck</h1></div></section>';
    return fetch(contentUrl, { cache: 'no-cache' })
      .then((response) => {
        if (!response.ok) throw new Error(`Slide data returned ${response.status}`);
        return response.json();
      })
      .then((data) => {
        legacyBuild(data);
        startReveal(paintBackgrounds);
      })
      .catch((error) => {
        slidesRoot.innerHTML = `<section data-background-color="#0b1220"><div class="student-media-slide"><h1>Slides unavailable</h1><p>${escapeHtml(error.message)}</p></div></section>`;
        startReveal();
      });
  };

  if (slidesRoot.querySelector(':scope > section')) startReveal();
  else legacyLoad();
})();
