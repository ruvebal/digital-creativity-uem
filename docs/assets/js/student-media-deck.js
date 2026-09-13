(() => {
  const body = document.body;
  const slidesRoot = document.getElementById('slides');
  const base = '/digital-creativity-uem';
  const loadingBackground = `${base}/assets/images/media/fractal-loading.svg`;
  const defaultBackgrounds = [
    {
      url: `${base}/assets/images/media/organic-pixel-drift.svg`,
      title: 'Organic pixel drift',
      credit_line: 'Course-generated visual · visual-forger',
      licence: 'Original studio SVG · educational use',
      resource_uuid: '7e3c9a4e-4d6b-4c38-9b2d-0f5e8a6c1d72',
      forger_version: 'visual-forger 1.2.0',
    },
    {
      url: `${base}/assets/images/media/pixel-grid-mutation.svg`,
      title: 'Pixel grid mutation',
      credit_line: 'Course-generated visual · visual-forger',
      licence: 'Original studio SVG · educational use',
      resource_uuid: 'b6a1f2d8-8c47-4f3e-a9c1-2d7e5b904613',
      forger_version: 'visual-forger 1.2.0',
    },
  ];
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

  const caption = (asset) => asset ? `
    <strong>${escapeHtml(asset.title || asset.alt_text || 'Untitled image')}</strong><br>
    <span>${escapeHtml(asset.credit_line || asset.provider || '')}</span><br>
    ${asset.canonical_source_url ? `<a href="${escapeHtml(asset.canonical_source_url)}" target="_blank" rel="noopener">View source record</a>` : '<span>Studio-generated background</span>'}${asset.licence ? `<br><span>${escapeHtml(asset.licence)}</span>` : ''}${asset.resource_uuid ? `<br><span>Resource UUID: ${escapeHtml(asset.resource_uuid)}</span>` : ''}${asset.forger_version ? `<br><span>Forger: ${escapeHtml(asset.forger_version)}</span>` : ''}` : '';

  slidesRoot.innerHTML = `<section data-background-image="${loadingBackground}" data-background-size="cover"><div class="student-media-slide"><h1>Loading reviewed media</h1></div></section>`;

  const loadDeck = () => fetch(`${body.dataset.contentUrl}?v=${Date.now()}`)
    .then(async (response) => {
      if (!response.ok) throw new Error(`Slide data returned ${response.status}`);
      return response.json();
    })
    .then((data) => {
      const assets = new Map(data.assets.map((asset) => [asset.media_slot_id, asset]));
      slidesRoot.innerHTML = data.slides.map((slide, slideIndex) => {
        const directAsset = assets.get(slide.media_slot_id);
        const asset = directAsset || null;
        const fallback = defaultBackgrounds[slideIndex % defaultBackgrounds.length];
        const captionAsset = asset || fallback;
        const imageUrl = asset?.asset_url || fallback.url;
        const image = ` data-background-image="${escapeHtml(imageUrl)}" data-background-size="cover" data-background-position="center"`;
        return `<section${image} data-caption="${escapeHtml(caption(captionAsset))}">
          <div class="student-media-slide">
            <p class="student-media-slide__unit">${escapeHtml(data.unit_label)}</p>
            <h1>${escapeHtml(slide.heading)}</h1>
            <p>${escapeHtml(slide.sentence)}</p>
            ${slide.citation ? `<p class="student-media-slide__citation"><a href="${escapeHtml(slide.citation.href)}">${escapeHtml(slide.citation.label)}</a></p>` : ''}
            ${slide.prompt ? `<p class="student-media-slide__prompt">${escapeHtml(slide.prompt)}</p>` : ''}
          </div>
        </section>`;
      }).join('');
      if (window.Reveal.isReady && Reveal.isReady()) Reveal.sync();
      else Reveal.initialize({ hash: true, slideNumber: true, transition: 'slide', backgroundTransition: 'fade', width: 1280, height: 720, margin: 0.055, minScale: 0.2, maxScale: 1.35 });
      Reveal.configure({ hash: true });
      if (!body.dataset.mediaControlsBound) {
        body.dataset.mediaControlsBound = 'true';
        document.querySelector('[data-media-toggle]').addEventListener('click', (event) => {
          const button = event.currentTarget;
          const hidden = body.classList.toggle('student-media-card-hidden');
          button.setAttribute('aria-pressed', String(!hidden));
        });
      }
      Reveal.on('ready', () => {
        const updateCaption = () => {
          captionRoot.innerHTML = Reveal.getCurrentSlide()?.dataset.caption || '';
          captionRoot.hidden = !captionRoot.innerHTML;
        };
        updateCaption();
        Reveal.on('slidechanged', updateCaption);
      });
    })
    .catch((error) => {
      slidesRoot.innerHTML = `<section data-background-image="${loadingBackground}" data-background-size="cover"><div class="student-media-slide"><h1>Slides unavailable</h1><p>${escapeHtml(error.message)}</p></div></section>`;
    });

  loadDeck();
})();
