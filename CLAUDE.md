# Repo conventions

## CV generation (`cv/`)

`cv/generate_cv_pdf.py` turns the markdown CVs into A4 ATS-friendly PDFs.
Pass filenames as arguments, or none to build every `*.md` in `cv/`.

```
cd cv && python3 generate_cv_pdf.py Anson_Chan_CV_<name>.md
```

Supported markup: `#`/`##`/`###` headings, `**bold**`, `*italic*`, `- ` bullets,
pipe tables, and a bare `---PAGEBREAK---` line to force a page break. Note that
forced page breaks usually make a document *longer* — check the reported page
count before assuming.

A CJK face is embedded so Traditional Chinese renders; runs of CJK are
auto-tagged, so mixed Chinese/English lines are fine.

### RULE — every CV must end with an AVAILABILITY & PACKAGE section

Standing instruction from Anson (2026-08-04). Every CV, for every application,
ends with:

```markdown
## AVAILABILITY & PACKAGE

**Current:** HK$40,600 per month — self-employed consulting income. Gross, and
excluding employer MPF contribution, paid annual leave and medical coverage, so
not directly comparable to a permanent package.

**Expected:** **HK$<range> per month base**, excluding bonus. <one line tying the
range to a named market benchmark for that specific role> Flexible depending on
how the role is levelled and the total package — happy to anchor to your
budgeted band rather than guess.

**Availability:** 2 weeks from agreed terms.

**Location:** Hong Kong, available on-site.
```

Rules for the numbers:

- **Current is HK$40,600/month and always carries the freelance qualifier.**
  The qualifier is not padding — it is the only thing stopping HK$40,600 from
  anchoring the offer. Never state the figure bare.
- **Expected is a range, never a single number.** A single figure becomes the
  ceiling.
- **Set the range from a named benchmark for that role**, not a habit. Morgan
  McKinley Hong Kong 2026 monthly reference points used so far: CRM Manager
  HK$58,000 · Digital Marketing Manager HK$55,000 · Marketing Manager HK$55,000 ·
  Head of Marketing HK$66,000–72,000 (JobsDB). Add roughly 10–15% for fintech.
  HK creative ladder: Senior Copywriter 30–45K · Creative Group Head 45–60K ·
  ACD 55–75K · CD 70–110K.
- **Keep the ask within roughly +20% to +35% of current.** Against a stated
  current of HK$40,600, a larger ask reads as unanchored and gets screened by HR
  before a hiring manager sees it.
- **Whatever goes on the CV must match what goes in the application form.** An
  inconsistency between the two is worse than either number alone.

### Channel figures — verify before writing, they go stale

@aieasyjob numbers change monthly and were wrong across every CV until
2026-08-03. Pull fresh vidIQ data rather than copying an older CV.

Verified 2026-08-03: **87,504 lifetime YouTube views · 58 videos · 335
subscribers.** Trailing 30 days: **+8 videos, +9,364 views.**

Two standing cautions:

- **Do not present the YouTube view total as evidence that the AI content
  performs.** Roughly 60% of lifetime views come from one Japanese anime music
  cover; the AI and marketing videos sit in the hundreds to low thousands. A
  reader who opens the channel sees that immediately.
- **"Weekly cadence" is not supportable.** 58 videos since January 2025 is about
  one every ten days. Use the checkable version instead — "58 films, eight of
  them in the last month".

The durable distribution proof is the Facebook Reel: **76,000 organic views from
a 77-follower page, zero paid support, with a second Reel at 11,000** confirming
it was structural.

## Analysis documents (`analysis/`)

One file per company, dated. Each records what was verified with sources, what
could not be verified, the role-fit assessment, and the decision taken. Written
in Cantonese with English quotations kept verbatim.

Research in this container runs behind an egress proxy that blocks most direct
page fetches, so findings usually come from search-result summaries rather than
primary documents. Say so in the document and mark load-bearing figures for
manual re-checking.
