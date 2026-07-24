# Content formats

## Writing post

Use `_posts/YYYY-MM-DD-short-slug.md`.

```yaml
---
layout: post
title: "Clear article title"
description: "One sentence used on index pages and in metadata."
date: 2026-07-25
updated: 2026-07-25
eyebrow: "Essay · Agentic RL"
public_writing: true
math: true
---
```

Start Markdown content at `##`; the layout supplies the page title.

Recommended structure: question, motivation, core idea, code/math/empirical
example, limitations, references.

## Writing status page

An announced essay may use `writing/<slug>.html` with a stable permalink before
the finished post exists. Label it `Work in progress`, state its factual scope,
and say that the completed article will appear there. Do not add an outline,
sample prose, citations, or other material that could be mistaken for a
finished article. Link its card on `writing.html` and the homepage directly to
that stable URL.

## Reading topic

Use `_reading/topic-slug.md`.

```yaml
---
title: "Topic name"
description: "One concise sentence."
domain: "Agentic AI"
meta: "Updated July 2026"
order: 3
published: true
---
```

Use one evolving page per topic. Group papers by date or concept. Give each
paper a citation line, 40–100 word neutral summary, and optional **Quick take**.

## Research entry

Add to `_data/research.yml`:

```yaml
- direction: Agentic AI
  title: "Research title"
  period: "2026"
  tags: "Agent environments · Reinforcement learning"
  summary: "One factual sentence under 35 words."
  paper: "https://..."
  code: "https://..."
  featured: false
  order: 10
```

Supported optional link keys: `paper`, `preprint`, `code`, `related_code`.

## Markdown

- Use sentence-case headings without skipped levels.
- Use fenced code with lower-case language identifiers.
- Use `$...$` for inline math and `$$...$$` for display math.
- Define symbols near first use.
- Use `{% cite key %}` for formal citations and add the record to
  `_bibliography/papers.bib`.
- Use direct Paper/Code links in curated Reading collections.
- Add precise alt text to every meaningful image.
- Do not hotlink publisher images.

## Slides

Publish a slide only with a real title, event, date, description, and PDF or
embeddable public URL. Prefer an embed with a direct PDF fallback. Never show
empty cards or invented events.

## CV

Keep stable public paths:

- `assets/cv/Qijia_Shen_CV.pdf`
- `assets/cv/Qijia_Shen_CV.docx`
