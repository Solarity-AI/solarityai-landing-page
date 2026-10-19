(function () {
  'use strict';
  if (typeof document === 'undefined') return;

  const imageDialog = document.getElementById('image-dialog');
  const previewImage = document.getElementById('image-dialog-image');
  const previewTitle = document.getElementById('image-dialog-title');
  const previewClose = document.getElementById('image-dialog-close');
  // Optional sequence controls: older markup without them keeps single-image previews.
  const previewNav = document.getElementById('image-dialog-nav');
  const previewPrev = document.getElementById('image-dialog-prev');
  const previewNext = document.getElementById('image-dialog-next');
  const previewCount = document.getElementById('image-dialog-count');
  // Optional caption: a link may name its own source; others keep the dialog's default line.
  const previewCaption = document.getElementById('image-dialog-caption');
  const defaultCaption = previewCaption ? previewCaption.textContent : '';
  if (imageDialog && previewImage && previewTitle && previewClose && typeof imageDialog.showModal === 'function') {
    let previewTrigger = null;
    let current = -1;
    const sameOrigin = (link) => new URL(link.href, window.location.href).origin === window.location.origin;
    // The page's screenshots, in reading order, form one browsable sequence.
    const links = Array.from(document.querySelectorAll('a.screenshot-open')).filter(sameOrigin);
    const browsable = Boolean(previewNav && previewPrev && previewNext && previewCount) && links.length > 1;

    function show(index) {
      current = (index + links.length) % links.length;
      const link = links[current];
      previewTitle.textContent = link.dataset.imageTitle || 'App preview';
      previewImage.alt = link.dataset.imageAlt || 'Official app promotional screenshot with sample content';
      previewImage.src = new URL(link.href, window.location.href).href;
      if (previewCaption) previewCaption.textContent = link.dataset.imageCaption || defaultCaption;
      if (browsable) previewCount.textContent = (current + 1) + ' of ' + links.length;
    }

    links.forEach((link, index) => {
      link.addEventListener('click', (event) => {
        // Preserve the link's native open-in-new-tab and image fallback behavior.
        if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
        show(index);
        try {
          imageDialog.showModal();
          previewTrigger = link;
          document.body.classList.add('image-preview-open');
          if (previewNav) previewNav.hidden = !browsable;
          previewClose.focus();
          event.preventDefault();
        } catch (_) {
          // If a dialog cannot open, the original anchor still opens the image.
          document.body.classList.remove('image-preview-open');
        }
      });
    });
    if (browsable) {
      previewPrev.addEventListener('click', () => show(current - 1));
      previewNext.addEventListener('click', () => show(current + 1));
      imageDialog.addEventListener('keydown', (event) => {
        if (!imageDialog.open || event.altKey || event.ctrlKey || event.metaKey) return;
        if (event.key === 'ArrowLeft') { event.preventDefault(); show(current - 1); }
        if (event.key === 'ArrowRight') { event.preventDefault(); show(current + 1); }
      });
    }
    previewClose.addEventListener('click', () => imageDialog.close());
    imageDialog.addEventListener('click', (event) => {
      if (event.target !== imageDialog) return;
      const rect = imageDialog.getBoundingClientRect();
      const outside = event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom;
      if (outside) imageDialog.close();
    });
    // Native Escape/cancel closes the dialog and reaches this same cleanup path.
    imageDialog.addEventListener('close', () => {
      document.body.classList.remove('image-preview-open');
      if (previewTrigger && previewTrigger.isConnected) previewTrigger.focus();
      previewTrigger = null;
    });
  }
})();
