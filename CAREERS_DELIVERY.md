# Careers delivery verification

Status on 2026-10-19: **confirmed on the earlier GPT Sites origin, unverified on solarityai.com.** Repeat the one-application test below on `https://solarityai.com/careers/#apply`.

**Status after the move (2026-10-18):** the site is live on solarityai.com and posts to `careers@solarityai.com`, which the founder chose to keep. The founder confirmed activation and delivery from the GPT Sites origin. The same one-application test must be repeated on `https://solarityai.com`; until it passes, an applicant's first submission from solarityai.com may only trigger FormSubmit's activation email.

## What the form does

`/careers/` posts natively to `https://formsubmit.co/careers@solarityai.com` with `_captcha=true`, a `_honey` field, `_template=box`, and `_url` set to the public careers URL. FormSubmit shows its own CAPTCHA and confirmation pages. The Site never shows its own success state.

## Evidence gathered (read-only)

- **Connected mailbox search** (the founder's Gmail, which receives `info@solarityai.com` forwards). It covered every FormSubmit message, including trash.
  - Real job applications were delivered through FormSubmit to **info@solarityai.com** from the previous `https://solarityai.com/` site. Messages are dated 2026-01-30, 2026-02-16 (two), 2026-03-07, 2026-04-21 and 2026-07-20, the last two forwarded by info@. So FormSubmit delivery works for that address and origin.
  - There are **no** FormSubmit messages addressed to `careers@solarityai.com`, neither activation requests nor submissions.
  - There are **no** FormSubmit messages that mention the then-current origin `solarity-company.the-ata-turhan.chatgpt.site`.
- FormSubmit sends a separate "Action Required: Activate FormSubmit on <origin>" email for each new address and site origin. The mailbox shows separate activations for `www.solarityai.com`, `127.0.0.1:8000` and `127.0.0.1:45969`. Submissions sent before activation are not delivered.
- `solarityai.com` MX records point to `mx1/mx2.privateemail.com`. Whether `careers@` is a real mailbox, an alias, or forwarded somewhere was not verifiable from here.

**Interpretation:** unless the `careers@solarityai.com` inbox (not visible here) holds an activation that was clicked, applications sent from the current Site since launch may not have been delivered.

## Why the test was not run by Claude

A real application has to pass FormSubmit's CAPTCHA, which Claude does not solve. The activation email also arrives in the `careers@` inbox, which is not connected to this workspace. Submitting a job application is also an outward-facing action that the founder should take.

## Test procedure (one real application, about 5 minutes)

1. In a normal browser, open the deployed careers page: `https://solarityai.com/careers/#apply`. Activation is per origin, so the earlier GPT Sites test does not cover solarityai.com.
2. Fill the form with your own details. Use the subject-identifying name `Delivery test – <date>` and choose any role and work type.
3. Select **Continue application**, then complete FormSubmit's CAPTCHA.
4. Record what FormSubmit shows (confirmation page, or "activate your form" notice).
5. Check the `careers@solarityai.com` inbox, including spam, for **"Action Required: Activate FormSubmit on <the origin you tested>"**. If it is there, click **Activate Form**.
6. If you activated in step 5, repeat steps 1–3 once more. The first submission is not delivered.
7. Confirm that **"New Job Application - Solarity AI"** arrives in `careers@` with all fields: fullName, email, position, workType, plus the optional linkedin, portfolio and note.
8. Fill in the result below and commit this file.

If `careers@` cannot receive mail, the founder should decide between creating that mailbox and pointing the form to the already-activated `info@solarityai.com`. The second option also changes `visual_careers.py`, the `check_site.py` destination contract, and `CLAUDE.md`.

## Result

| Date | Tester | Activation email received | Activated | Test application received in careers@ | Notes |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Founder | Yes | Yes | Yes (reported by the founder) | Tested on the GPT Sites origin (`solarity-company.the-ata-turhan.chatgpt.site`) before the move. |
| _pending_ | Founder | | | | Repeat once on `https://solarityai.com/careers/#apply` (live since 2026-10-18), because activation is per origin. |
