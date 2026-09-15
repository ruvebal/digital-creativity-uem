(() => {
  // Digital Creativity student deck — Profield-backed Reveal slides.
  // Spine: unit_cover → analysis → masterclass ≤6 → geometrical lab_opener → lab
  // → geometrical workshop_opener → workshop → geometrical outro.
  // Captions: clean title · human credit · Commons source page · original file.
  // Geometrical captions include the SVG content-hash UUID from the filename.
  // Backgrounds: painted via CSS after Reveal.sync — never data-background-image
  // for remote URLs (commas split multi-bg; %2B gets encodeURI-doubled to %252B).
  // Never expose Resource UUID / forger version.
  const body = document.body;
  const slidesRoot = document.getElementById('slides');
  const base = '/digital-creativity-uem';
  const geometricalCycle = [
    'uem-henon-pass-01-structure-2fc3613c22a1.svg',
    'uem-henon-pass-02-threshold-c378606cc29b.svg',
    'uem-henon-pass-03-branching-46681e3d02cd.svg',
    'uem-henon-pass-04-practice-1ab1247ed3af.svg',
    'uem-henon-pass-05-feedback-903832404a06.svg',
    'uem-henon-pass-06-coherence-a8444d20854d.svg',
  ];
  const geometricalBase = `${base}/assets/images/fractal-pass-track`;
  const diagramFallback = {
    url: `${base}/assets/images/media/organic-pixel-drift.svg`,
    title: 'Course diagram',
    credit_line: 'Course-generated visual',
    licence: 'Original studio SVG · educational use',
  };
  const loadingBackground = `${base}/assets/images/media/fractal-loading.svg`;

  const captionRoot = document.createElement('aside');
  captionRoot.className = 'student-media-caption';
  captionRoot.setAttribute('aria-live', 'polite');
  document.body.append(captionRoot);

  const controls = document.createElement('div');
  controls.className = 'student-media-controls';
  controls.innerHTML = '<button type="button" data-media-toggle aria-pressed="true" aria-label="Show or hide reading card" title="Show or hide reading card">◉</button>';
  document.body.append(controls);

  const escapeHtml = (value) => String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;');

  const stripUtm = (url) => {
    if (!url) return '';
    try {
      const parsed = new URL(url);
      ['utm_source', 'utm_campaign', 'utm_content', 'utm_medium', 'utm_term'].forEach((key) => parsed.searchParams.delete(key));
      const query = parsed.searchParams.toString();
      return `${parsed.origin}${parsed.pathname}${query ? `?${query}` : ''}`;
    } catch {
      return String(url).replace(/[?&]utm_[^=]+=[^&]*/g, '').replace(/\?$/, '');
    }
  };

  const cleanTitle = (title) => String(title || '')
    .replace(/^File:/i, '')
    .replace(/\s*\[[^\]]*\]\s*$/g, '')
    .trim();

  const humanProvider = (value) => {
    const raw = String(value || '').trim();
    if (!raw) return 'Wikimedia Commons';
    if (/^wikimedia(_commons)?$/i.test(raw)) return 'Wikimedia Commons';
    if (/^internet_archive$/i.test(raw)) return 'Internet Archive';
    return raw.replace(/_/g, ' ');
  };

  const commonsPageFromAssetId = (assetId) => {
    const match = String(assetId || '').match(/^wikimedia:File:(.+)$/i);
    if (!match) return '';
    const fileName = match[1].replace(/ /g, '_');
    return `https://commons.wikimedia.org/wiki/File:${encodeURIComponent(fileName).replace(/%2F/g, '/')}`;
  };

  const sourcePageUrl = (asset) => {
    const fromField = asset.canonical_source_url || asset.source || '';
    if (/commons\.wikimedia\.org\/wiki\/File:/i.test(fromField)
      || /wikipedia\.org\/wiki\/File:/i.test(fromField)) {
      return fromField;
    }
    return commonsPageFromAssetId(asset.asset_id) || fromField;
  };

  const captionsBySection = new WeakMap();
  const backgroundUrlBySection = new WeakMap();

  const publicCaption = (asset) => {
    if (!asset) return '';
    const title = cleanTitle(asset.title || asset.alt_text || 'Untitled image');
    const credit = humanProvider(asset.credit_line || asset.provider);
    const licence = asset.licence || '';
    const pageUrl = sourcePageUrl(asset);
    const fileUrl = stripUtm(asset.source_file_url || asset.asset_url || asset.preview_url || asset.url || '');
    const svgUuid = asset.svg_uuid ? `<br><span>#${escapeHtml(asset.svg_uuid)}</span>` : '';
    const links = [];
    if (pageUrl) {
      links.push(`<a href="${escapeHtml(pageUrl)}" target="_blank" rel="noopener">View source record</a>`);
    }
    if (fileUrl && fileUrl !== pageUrl && /^https?:/i.test(fileUrl)) {
      links.push(`<a href="${escapeHtml(fileUrl)}" target="_blank" rel="noopener">Original file</a>`);
    }
    if (!links.length) links.push('<span>Studio-generated background</span>');
    return `<strong>${escapeHtml(title)}</strong><br>`
      + `<span>${escapeHtml(credit)}</span><br>`
      + `${links.join(' · ')}`
      + `${licence ? `<br><span>${escapeHtml(licence)}</span>` : ''}`
      + svgUuid;
  };

  const isGeometrical = (slide) =>
    slide.background_kind === 'geometrical'
    || ['analysis_opener', 'lab_opener', 'workshop_opener', 'outro'].includes(slide.slide_role);

  /** Apply remote/local image URLs after Reveal builds .slide-background nodes. */
  const paintBackgrounds = () => {
    [...slidesRoot.querySelectorAll('section')].forEach((section) => {
      const url = backgroundUrlBySection.get(section);
      if (!url) return;
      const bg = (typeof Reveal.getSlideBackground === 'function')
        ? Reveal.getSlideBackground(section)
        : null;
      const node = bg?.querySelector?.('.slide-background-content') || bg;
      if (!node) return;
      node.style.backgroundImage = `url(${JSON.stringify(url)})`;
      node.style.backgroundSize = 'cover';
      node.style.backgroundPosition = 'center';
      node.style.backgroundRepeat = 'no-repeat';
    });
  };

  slidesRoot.innerHTML = `<section data-background-color="#0b1220"><div class="student-media-slide"><h1>Loading reviewed media</h1></div></section>`;

  const loadDeck = () => fetch(`${body.dataset.contentUrl}?v=${Date.now()}`)
    .then(async (response) => {
      if (!response.ok) throw new Error(`Slide data returned ${response.status}`);
      return response.json();
    })
    .then((data) => {
      const assets = new Map((data.assets || []).map((asset) => [asset.media_slot_id, asset]));
      let geometricalIndex = 0;
      slidesRoot.innerHTML = '';
      data.slides.forEach((slide) => {
        const directAsset = slide.media_slot_id ? assets.get(slide.media_slot_id) : null;
        let fileUrl;
        let captionAsset;

        if (isGeometrical(slide)) {
          const file = geometricalCycle[geometricalIndex % geometricalCycle.length];
          geometricalIndex += 1;
          fileUrl = `${geometricalBase}/${file}`;
          const uuidMatch = file.match(/-([a-f0-9]{8,})\.svg$/i);
          captionAsset = {
            title: file.replace(/\.svg$/, '').replace(/uem-henon-pass-\d+-/, '').replace(/-/g, ' '),
            credit_line: 'Course geometrical background',
            licence: 'Original studio SVG · educational use',
            url: fileUrl,
            svg_uuid: uuidMatch ? uuidMatch[1] : '',
          };
        } else if (directAsset?.asset_url) {
          fileUrl = stripUtm(directAsset.asset_url);
          captionAsset = {
            ...directAsset,
            asset_url: fileUrl,
            title: cleanTitle(directAsset.title || directAsset.alt_text),
            credit_line: humanProvider(directAsset.credit_line || directAsset.provider),
          };
        } else {
          fileUrl = diagramFallback.url;
          captionAsset = diagramFallback;
        }

        const section = document.createElement('section');
        section.setAttribute('data-background-color', '#0b1220');
        if (slide.slide_role) section.setAttribute('data-slide-role', slide.slide_role);
        if (slide.portfolio_bound) section.setAttribute('data-portfolio-bound', 'true');
        section.innerHTML = `
          <div class="student-media-slide">
            <p class="student-media-slide__unit">${escapeHtml(data.unit_label)}</p>
            <h1>${escapeHtml(slide.heading)}</h1>
            <p>${escapeHtml(slide.sentence)}</p>
            ${slide.quote ? `<blockquote class="student-media-slide__quote"><p>${escapeHtml(slide.quote)}</p></blockquote>` : ''}
            ${slide.citation ? `<p class="student-media-slide__citation"><a href="${escapeHtml(slide.citation.href)}">${escapeHtml(slide.citation.label)}</a></p>` : ''}
            ${slide.prompt ? `<p class="student-media-slide__prompt">${escapeHtml(slide.prompt)}</p>` : ''}
            ${slide.portfolio_trace ? `<p class="student-media-slide__prompt">${escapeHtml(slide.portfolio_trace)}</p>` : ''}
          </div>`;
        backgroundUrlBySection.set(section, fileUrl);
        captionsBySection.set(section, publicCaption(captionAsset));
        slidesRoot.append(section);
      });

      if (window.Reveal.isReady && Reveal.isReady()) Reveal.sync();
      else Reveal.initialize({ hash: true, slideNumber: true, transition: 'slide', backgroundTransition: 'fade', width: 1280, height: 720, margin: 0.055, minScale: 0.2, maxScale: 1.35 });
      Reveal.configure({ hash: true });
      paintBackgrounds();

      if (!body.dataset.mediaControlsBound) {
        body.dataset.mediaControlsBound = 'true';
        document.querySelector('[data-media-toggle]').addEventListener('click', (event) => {
          const button = event.currentTarget;
          const hidden = body.classList.toggle('student-media-card-hidden');
          button.setAttribute('aria-pressed', String(!hidden));
        });
      }

      const updateCaption = () => {
        const current = Reveal.getCurrentSlide();
        captionRoot.innerHTML = (current && captionsBySection.get(current)) || '';
        captionRoot.hidden = !captionRoot.innerHTML;
        paintBackgrounds();
      };
      Reveal.on('ready', updateCaption);
      Reveal.on('slidechanged', updateCaption);
      if (Reveal.isReady && Reveal.isReady()) updateCaption();
    })
    .catch((error) => {
      slidesRoot.innerHTML = `<section data-background-image="${loadingBackground}" data-background-size="cover"><div class="student-media-slide"><h1>Slides unavailable</h1><p>${escapeHtml(error.message)}</p></div></section>`;
    });

  loadDeck();
})();
