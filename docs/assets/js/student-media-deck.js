(() => {
  const body = document.body;
  const slidesRoot = document.getElementById('slides');
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
    <a href="${escapeHtml(asset.canonical_source_url || '')}" target="_blank" rel="noopener">View source record</a>${asset.licence ? `<br><span>${escapeHtml(asset.licence)}</span>` : ''}` : '';

  const loadDeck = () => fetch(`${body.dataset.contentUrl}?v=${Date.now()}`)
    .then(async (response) => {
      if (!response.ok) throw new Error(`Slide data returned ${response.status}`);
      return response.json();
    })
    .then((data) => {
      const assets = new Map(data.assets.map((asset) => [asset.media_slot_id, asset]));
      slidesRoot.innerHTML = data.slides.map((slide) => {
        const asset = assets.get(slide.media_slot_id);
        const image = asset?.asset_url ? ` data-background-image="${escapeHtml(asset.asset_url)}" data-background-size="cover" data-background-position="center"` : '';
        const alt = asset ? `<p class="sr-only">${escapeHtml(asset.alt_text)}</p>` : '';
        return `<section${image} data-caption="${escapeHtml(caption(asset))}">
          <div class="student-media-slide">
            <p class="student-media-slide__unit">${escapeHtml(data.unit_label)}</p>
            <h1>${escapeHtml(slide.heading)}</h1>
            <p>${escapeHtml(slide.sentence)}</p>
            ${slide.citation ? `<p class="student-media-slide__citation"><a href="${escapeHtml(slide.citation.href)}">${escapeHtml(slide.citation.label)}</a></p>` : ''}
            ${slide.prompt ? `<p class="student-media-slide__prompt">${escapeHtml(slide.prompt)}</p>` : ''}
            ${alt}
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
      slidesRoot.innerHTML = `<section><h1>Slides unavailable</h1><p>${escapeHtml(error.message)}</p></section>`;
    });

  loadDeck();
})();
