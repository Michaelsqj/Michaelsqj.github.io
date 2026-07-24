---
name: maintain-quiet-scholar-site
description: Maintain Qijia Shen's Quiet Scholar Jekyll website, including profile copy, research data, writing posts, reading-topic collections, MRI archives, slides, CV assets, styling, validation, and GitHub Pages deployment. Use for any content, design, structure, metadata, or publishing change in this repository.
---

# Maintain the Quiet Scholar site

Preserve the approved restrained academic design and the content taxonomy:
About, Research, Writing, Reading, Slides, and CV.

## Start every change

1. Read `AGENTS.md`, `_config.yml`, and the files directly affected.
2. Read the relevant reference:
   - Content or Markdown: [content-formats.md](references/content-formats.md)
   - Styling or layout: [design-system.md](references/design-system.md)
   - Build or publish: [deployment.md](references/deployment.md)
3. Preserve unrelated user changes.

## Content ownership

- Edit social/contact links in `_data/profile.yml` and homepage copy in
  `index.html`.
- Edit research only in `_data/research.yml`; templates render it elsewhere.
- Edit experience and education only in `_data/timeline.yml`.
- Add finished essays to `_posts/` with `public_writing: true`.
- Add living paper collections to `_reading/`.
- Maintain the 2021 MRI collection through `_data/mri_archive.yml`; keep the
  original `_posts/` files and URLs.
- Add slide metadata and real assets only after public materials exist.
- Replace CV files in `assets/cv/` without changing their stable filenames.

## Public-content rules

- Publish factual content only. Do not add demo, sample, prototype, placeholder,
  fabricated, or speculative material.
- Do not publish unfinished article bodies. Works in progress may appear only
  as honest, non-clickable titles on `writing.html`.
- Do not publish empty topic or slide cards.
- Never label MRI or medical-imaging work as ongoing.
- Keep research summaries to one sentence, ideally 20–35 words.
- Label links accurately: Paper, Preprint, Code, Related code, Dataset, Slides.
- Keep Generative 3D & Vision before Medical Imaging & Neuroscience.
- Preserve the phrase `staleness–stability–efficiency trade-off`.
- Preserve `Mini-Miles` as the companion project name and distinguish it from
  the upstream Miles framework.

## Design rules

- Reuse `_layouts/default.html`, `_includes/rail.html`, and
  `assets/css/style.css`.
- Preserve paper-like neutrals, serif body typography, restrained navy/brown
  accents, thin rules, and generous whitespace.
- Do not introduce decorative slogans, template branding, ornamental badges,
  gradients, animation-heavy effects, or generic dashboard components.
- Keep navigation and keyboard focus accessible.
- Use real imagery only when it adds information; keep the portrait unchanged
  unless the user supplies a replacement.

## Validation

Before committing:

1. Build with `bundle exec jekyll build`.
2. Confirm no missing internal targets.
3. Search public output for `demo`, `sample`, `placeholder`, `prototype`,
   `planned`, and `draft`; investigate every match.
4. Confirm Research order and dates.
5. Confirm CV PDF and DOCX targets exist.
6. Confirm old MRI note URLs still build.

## Publishing

Follow [deployment.md](references/deployment.md). Push source to `src`; GitHub
Actions builds and deploys it. Do not use the old Travis or force-rewrite
`gh-pages` workflow.
