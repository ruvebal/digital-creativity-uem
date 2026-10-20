document.addEventListener('click', (event) => {
	const button = event.target.closest('.dignity-flip');
	if (!button) return;

	const image = document.getElementById(button.getAttribute('aria-controls'));
	if (!image) return;

	const showingPositive = button.getAttribute('aria-pressed') !== 'true';
	image.src = showingPositive ? image.dataset.positiveSrc : image.dataset.negativeSrc;
	image.alt = showingPositive ? image.dataset.positiveAlt : image.dataset.negativeAlt;
	button.setAttribute('aria-pressed', String(showingPositive));
	button.textContent = showingPositive ? button.dataset.labelNegative : button.dataset.labelPositive;
	const caption = document.getElementById(button.dataset.captionId);
	if (caption) caption.textContent = showingPositive ? button.dataset.captionAlternative : button.dataset.captionCritical;
});
