(() => {
  const body = document.body;
  const slidesRoot = document.getElementById('slides');
  const captionRoot = document.createElement('aside');
  captionRoot.className = 'pass-track-art__caption';
  captionRoot.setAttribute('aria-live', 'polite');
  document.body.append(captionRoot);

  const escapeHtml = (value) => String(value)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;');

  const renderCaption = (figure, release) => `
    <span class="pass-track-art__title">${escapeHtml(figure.title)}</span>
    <span class="pass-track-art__formula">${escapeHtml(figure.formulae[0].display)}</span>
    <span class="pass-track-art__description">${escapeHtml(figure.formulae[0].basic_explanation)}</span>
    <span class="pass-track-art__source">${escapeHtml(figure.formulae[0].citation.inline)} ${escapeHtml(release.caption.source)}</span>
    <span class="pass-track-art__credit">${escapeHtml(figure.authorship.name)} · ${escapeHtml(figure.created_at.slice(0, 10))} · #${escapeHtml(figure.fractal_hash256)}</span>
  `;

  const renderFirstSlideLogo = () => {
    const logoUrl = body.dataset.logoUrl;
    if (!logoUrl) return '';
    const logoAlt = body.dataset.logoAlt || '';
    return `<figure class="pass-track-slide-logo"><img src="${escapeHtml(logoUrl)}" alt="${escapeHtml(logoAlt)}" width="467" height="80" loading="eager" decoding="async"></figure>`;
  };

  const renderDeckHeader = () => {
    const header = document.createElement('header');
    header.className = 'pass-track-deck-header';
    header.innerHTML = `
      <div class="pass-track-deck-header__title">
        <span>${escapeHtml(body.dataset.trackTitle || '')}</span>
        <small>${escapeHtml(body.dataset.trackSubtitle || '')}</small>
      </div>
      <div class="pass-track-deck-header__meta">
        <span>${escapeHtml(body.dataset.trackAuthor || '')}</span>
      </div>`;
    document.body.append(header);
  };

  const renderCalendarNote = (calendar) => {
    return `
      <aside class="pass-track-calendar-note">
        <p>${escapeHtml(calendar.note)} <a href="${escapeHtml(calendar.source_url)}" target="_blank" rel="noopener">${escapeHtml(calendar.source_label)}</a>.</p>
      </aside>`;
  };

  const updateCaption = () => {
    const currentSlide = Reveal.getCurrentSlide();
    captionRoot.innerHTML = currentSlide?.dataset.artCaption || '';
    captionRoot.hidden = !captionRoot.innerHTML;
  };

  const requests = [
    fetch(body.dataset.contentUrl),
    fetch(`${body.dataset.artBase}/index.json`),
  ];
  if (body.dataset.calendarUrl) {
    requests.push(fetch(body.dataset.calendarUrl));
  }

  Promise.all(requests)
    .then(async ([contentResponse, artResponse, calendarResponse]) => {
      if (!contentResponse.ok) throw new Error(`Slide data returned ${contentResponse.status}`);
      if (!artResponse.ok) throw new Error(`Art index returned ${artResponse.status}`);
      if (calendarResponse && !calendarResponse.ok) throw new Error(`Calendar data returned ${calendarResponse.status}`);
      return [
        await contentResponse.json(),
        await artResponse.json(),
        calendarResponse ? await calendarResponse.json() : null,
      ];
    })
    .then(async ([data, artIndex, calendar]) => {
      // index.json accumulates every historical regeneration, so several
      // releases can share the same formula (a generator re-run after a
      // fix, a palette tweak, ...). Keep only the newest release per
      // distinct formula, so the deck cycles through each confirmed
      // formula exactly once rather than replaying old regenerations.
      const latestByFormula = new Map();
      for (const item of artIndex.releases) {
        if (item.brand !== body.dataset.brand || item.assets.length === 0) continue;
        const key = item.formula?.latex;
        const existing = latestByFormula.get(key);
        if (!existing || Date.parse(item.created_at) > Date.parse(existing.created_at)) {
          latestByFormula.set(key, item);
        }
      }
      const releases = [...latestByFormula.values()].sort((a, b) => Date.parse(a.created_at) - Date.parse(b.created_at));
      if (releases.length === 0) throw new Error('No compatible art release is indexed.');
      if (releases.some((item) => !item.figcaption_manifest)) throw new Error('No figcaption manifest is indexed for this art release.');

      const figuresBySvg = new Map();
      const combinedAssets = [];
      for (const release of releases) {
        const figcaptionResponse = await fetch(`${body.dataset.artBase}/${release.figcaption_manifest}`);
        if (!figcaptionResponse.ok) throw new Error(`Figcaption data returned ${figcaptionResponse.status}`);
        const figcaptionData = await figcaptionResponse.json();
        for (const figure of figcaptionData.figures) {
          figuresBySvg.set(figure.delivery.svg, figure);
        }
        for (const asset of release.assets) {
          combinedAssets.push({ asset, release });
        }
      }

      renderDeckHeader();
      const firstSlideLogo = renderFirstSlideLogo();
      const calendarNote = calendar ? renderCalendarNote(calendar) : '';
      slidesRoot.innerHTML = data.slides.map((slide, index) => {
        const { asset, release } = combinedAssets[index % combinedAssets.length];
        const figure = figuresBySvg.get(asset.svg);
        if (!figure) throw new Error(`No figcaption record exists for ${asset.svg}`);
        const imageUrl = `${body.dataset.artBase}/${escapeHtml(asset.svg)}`;
        const slideCalendarNote = slide.calendar_note ? calendarNote : '';
        const slideLogo = index === 0 ? firstSlideLogo : '';
        return `<section
          data-background-image="${imageUrl}"
          data-background-size="auto 126%"
          data-background-position="right center"
          data-background-color="rgb(var(--background))"
          data-art-caption="${escapeHtml(renderCaption(figure, release))}">
          <div class="pass-track-slide-copy">${slideLogo}${slide.content}${slideCalendarNote}</div>
        </section>`;
      }
      ).join('');

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
      }).then(() => {
        updateCaption();
        Reveal.on('slidechanged', updateCaption);
        Reveal.on('ready', updateCaption);
      });
    })
    .catch((error) => {
      captionRoot.hidden = true;
      slidesRoot.innerHTML = `<section><h2>Slides unavailable</h2><p>${error.message}</p></section>`;
      Reveal.initialize({ hash: true, slideNumber: true });
    });
})();
