(function () {
  'use strict';
  if (typeof document === 'undefined') return;

  const imageDialog = document.getElementById('image-dialog');
  const previewImage = document.getElementById('image-dialog-image');
  const previewTitle = document.getElementById('image-dialog-title');
  const previewClose = document.getElementById('image-dialog-close');
  if (imageDialog && previewImage && previewTitle && previewClose && typeof imageDialog.showModal === 'function') {
    let previewTrigger = null;
    document.querySelectorAll('a.screenshot-open').forEach((link) => {
      link.addEventListener('click', (event) => {
        // Preserve the link's native open-in-new-tab and image fallback behavior.
        if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
        const imageUrl = new URL(link.href, window.location.href);
        if (imageUrl.origin !== window.location.origin) return;
        previewTitle.textContent = link.dataset.imageTitle || 'App preview';
        previewImage.alt = link.dataset.imageAlt || 'Official app promotional screenshot with sample content';
        previewImage.src = imageUrl.href;
        try {
          imageDialog.showModal();
          previewTrigger = link;
          document.body.classList.add('image-preview-open');
          previewClose.focus();
          event.preventDefault();
        } catch (_) {
          // If a dialog cannot open, the original anchor still opens the image.
          document.body.classList.remove('image-preview-open');
        }
      });
    });
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
