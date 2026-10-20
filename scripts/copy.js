(function () {
  'use strict';
  if (typeof document === 'undefined') return;

  // A fallback for visitors whose email links do not open a mail app. Buttons
  // stay hidden unless the clipboard is available, so nothing is offered that
  // cannot work. Each button reports through its own polite status region.
  const clipboard = typeof navigator !== 'undefined' && navigator.clipboard;
  if (!clipboard || typeof clipboard.writeText !== 'function') return;

  document.querySelectorAll('button[data-copy]').forEach((button) => {
    const status = document.getElementById(button.getAttribute('data-copy-status') || '');
    const label = button.textContent;
    let reset = null;

    function report(message, buttonText) {
      if (status) status.textContent = message;
      button.textContent = buttonText;
      if (reset) clearTimeout(reset);
      reset = setTimeout(() => {
        button.textContent = label;
        if (status) status.textContent = '';
        reset = null;
      }, 4000);
    }

    button.addEventListener('click', () => {
      const text = button.getAttribute('data-copy');
      const name = button.getAttribute('data-copy-name');
      clipboard.writeText(text).then(
        () => report((name || text) + ' copied to your clipboard.', 'Copied'),
        () => report('Copying is not available here. Select the ' + (name ? 'text' : 'address') + ' to copy it.', label)
      );
    });
    button.hidden = false;
  });
})();
