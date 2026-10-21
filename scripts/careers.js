(function () {
  'use strict';

  const ROLES = ['full-stack-engineer', 'marketing-specialist'];
  const WORK_TYPES = ['full-time', 'part-time', 'intern'];
  const trim = (value) => String(value || '').trim();
  const hasControls = (value) => /[\u0000-\u001f\u007f]/.test(value);

  function readCareerRole(search) {
    const role = new URLSearchParams(search).get('role');
    return ROLES.includes(role) ? role : '';
  }

  function parseWebUrl(value) {
    const text = trim(value);
    if (!/^https?:\/\//i.test(text) || text.length > 500 || /\s/.test(text) || hasControls(text) || text.includes('\\')) return null;
    try {
      const url = new URL(text);
      return ['https:', 'http:'].includes(url.protocol) && url.hostname && !url.username && !url.password ? url : null;
    } catch (_) {
      return null;
    }
  }

  function isLinkedInProfile(value) {
    const url = parseWebUrl(value);
    // Country subdomains such as tr.linkedin.com are standard profile links.
    if (!url || url.protocol !== 'https:' || url.port || !/^(?:(?:www|[a-z]{2})\.)?linkedin\.com$/.test(url.hostname)) return false;
    const match = url.pathname.match(/^\/in\/([^/]+)\/?$/);
    if (!match) return false;
    try {
      const profile = decodeURIComponent(match[1]);
      return !!profile && !/[\s/\\?#]/.test(profile) && !hasControls(profile) && !['.', '..'].includes(profile);
    } catch (_) {
      return false;
    }
  }

  // People often paste links without a scheme (linkedin.com/in/name). Add https://
  // to anything that looks like a domain; leave other input for validation to explain.
  function withScheme(value) {
    const text = trim(value);
    if (!text || /^[a-z][a-z0-9+.-]*:/i.test(text)) return text;
    if (text.startsWith('//')) return 'https:' + text;
    return /^[a-z0-9-]+(?:\.[a-z0-9-]+)+(?:[/?#]|$)/i.test(text) ? 'https://' + text : text;
  }

  function isEmailAddress(value) {
    const email = trim(value);
    // Match the HTML email input grammar rather than restricting the provider.
    return email.length <= 254 && /^[a-z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?(?:\.[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)*$/i.test(email);
  }

  // The optional note matches the textarea's maxlength.
  const NOTE_LIMIT = 1000;

  function validateCareerApplication(input) {
    const errors = {};
    const fullName = trim(input.fullName);
    if (!fullName) errors.fullName = 'Enter your full name.';
    else if (fullName.length < 2) errors.fullName = 'Use at least 2 characters for your full name.';
    else if (fullName.length > 100) errors.fullName = 'Use 100 characters or fewer for your name.';
    else if (hasControls(fullName)) errors.fullName = 'Enter your name on one line.';
    if (!isEmailAddress(input.email)) errors.email = 'Enter a valid email address, such as name@example.com.';
    if (trim(input.linkedin) && !isLinkedInProfile(input.linkedin)) errors.linkedin = 'Enter your LinkedIn profile URL, such as https://www.linkedin.com/in/your-name.';
    if (trim(input.portfolio) && !parseWebUrl(input.portfolio)) errors.portfolio = 'Enter a complete website, portfolio, GitHub, or Linktree URL starting with https:// or http://.';
    if (!ROLES.includes(input.position)) errors.position = 'Choose one of the listed positions.';
    if (!WORK_TYPES.includes(input.workType)) errors.workType = 'Choose your preferred work type.';
    if (String(input.note || '').length > NOTE_LIMIT) errors.note = 'Use ' + NOTE_LIMIT.toLocaleString('en-US') + ' characters or fewer for your note.';
    return errors;
  }

  function isPlainActivation(event, link) {
    return !event.defaultPrevented && (event.button === undefined || event.button === 0)
      && !event.metaKey && !event.ctrlKey && !event.shiftKey && !event.altKey
      && (!link.target || link.target === '_self') && !link.hasAttribute('download');
  }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { readCareerRole, parseWebUrl, isLinkedInProfile, isEmailAddress, validateCareerApplication, isPlainActivation, withScheme };
  }
  if (typeof document === 'undefined') return;

  const form = document.getElementById('career-form');
  if (!form) return;
  const fields = {
    fullName: document.getElementById('career-name'),
    email: document.getElementById('career-email'),
    linkedin: document.getElementById('career-linkedin'),
    portfolio: document.getElementById('career-portfolio'),
    position: document.getElementById('career-position'),
    workType: document.getElementById('career-work-type')
  };
  // The note is optional markup: pages without it keep the original six fields.
  const note = document.getElementById('career-note');
  if (note) fields.note = note;
  const summary = document.getElementById('career-errors');
  const errorList = document.getElementById('career-error-list');
  const status = document.getElementById('career-status');
  const submit = document.getElementById('career-submit');
  if (!summary || !errorList || !status || !submit || Object.values(fields).some((field) => !field)) return;
  const errorElements = Object.fromEntries(Object.entries(fields).map(([key, field]) => [key, document.getElementById(field.id + '-error')]));
  if (Object.values(errorElements).some((error) => !error)) return;

  let attempted = false;
  let handoff = false;
  let handoffAt = 0;
  const touched = new Set();
  const values = () => Object.fromEntries(Object.entries(fields).map(([key, field]) => [key, field.value]));

  function renderErrors(errors) {
    Object.entries(fields).forEach(([key, field]) => {
      const message = attempted || touched.has(key) ? errors[key] : '';
      const error = errorElements[key];
      error.textContent = message || '';
      error.hidden = !message;
      const descriptions = (field.getAttribute('aria-describedby') || '').split(/\s+/).filter((id) => id && id !== error.id);
      if (message) {
        field.setAttribute('aria-invalid', 'true');
        descriptions.push(error.id);
      } else {
        field.removeAttribute('aria-invalid');
      }
      if (descriptions.length) field.setAttribute('aria-describedby', descriptions.join(' '));
      else field.removeAttribute('aria-describedby');
    });
    errorList.replaceChildren();
    if (attempted) {
      Object.entries(errors).forEach(([key, message]) => {
        const item = document.createElement('li');
        const link = document.createElement('a');
        link.href = '#' + fields[key].id;
        link.textContent = message;
        link.addEventListener('click', (event) => {
          if (!isPlainActivation(event, link)) return;
          event.preventDefault();
          fields[key].focus();
        });
        item.append(link);
        errorList.append(item);
      });
    }
    summary.hidden = !attempted || !Object.keys(errors).length;
  }

  function resetHandoff() {
    if (!handoff) return;
    handoff = false;
    form.removeAttribute('aria-busy');
    submit.removeAttribute('aria-busy');
    status.textContent = '';
  }

  Object.entries(fields).forEach(([key, field]) => {
    field.addEventListener('blur', () => {
      if (key === 'linkedin' || key === 'portfolio') field.value = withScheme(field.value);
      touched.add(key);
      renderErrors(validateCareerApplication(values()));
    });
  });
  function handleEdit() {
    resetHandoff();
    status.textContent = '';
    renderErrors(validateCareerApplication(values()));
  }
  form.addEventListener('input', handleEdit);
  form.addEventListener('change', handleEdit);

  const initialRole = readCareerRole(window.location.search);
  // Preserve values restored by the browser when returning from the verification service.
  if (initialRole && !fields.position.value) fields.position.value = initialRole;
  document.querySelectorAll('a[data-career-role]').forEach((link) => {
    link.addEventListener('click', (event) => {
      if (!isPlainActivation(event, link)) return;
      const role = link.getAttribute('data-career-role');
      const destination = new URL(link.href, window.location.href);
      if (!ROLES.includes(role) || destination.origin !== window.location.origin || !/^\/careers\/?$/.test(destination.pathname)) return;
      event.preventDefault();
      resetHandoff();
      fields.position.value = role;
      touched.add('position');
      renderErrors(validateCareerApplication(values()));
      status.textContent = fields.position.options[fields.position.selectedIndex].textContent + ' selected. Complete the application below.';
      // Start where the applicant has work left: the first empty field, which sits above the role field.
      const next = [fields.fullName, fields.email, fields.workType].find((field) => !field.value.trim()) || fields.position;
      next.focus({ preventScroll: true });
      const reducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      next.scrollIntoView({ block: 'center', behavior: reducedMotion ? 'instant' : 'smooth' });
    });
  });

  form.addEventListener('submit', (event) => {
    // A second click while the provider is loading would post the application twice.
    if (handoff && Date.now() - handoffAt < 10000) {
      event.preventDefault();
      return;
    }
    attempted = true;
    resetHandoff();
    fields.linkedin.value = withScheme(fields.linkedin.value);
    fields.portfolio.value = withScheme(fields.portfolio.value);
    const errors = validateCareerApplication(values());
    renderErrors(errors);
    if (Object.keys(errors).length) {
      event.preventDefault();
      status.textContent = '';
      summary.focus();
      return;
    }
    // Keep the native POST, service CAPTCHA, and server confirmation intact.
    // Never infer successful delivery from this page or from URL parameters.
    Object.values(fields).forEach((field) => { field.value = field.value.trim(); });
    handoff = true;
    handoffAt = Date.now();
    form.setAttribute('aria-busy', 'true');
    submit.setAttribute('aria-busy', 'true');
    status.textContent = 'Continuing to FormSubmit for verification. Your application has not been confirmed yet.';
  });
  window.addEventListener('pageshow', resetHandoff);
  // Native HTML constraints remain active if the enhancement cannot initialize.
  form.noValidate = true;
})();
