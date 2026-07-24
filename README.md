# Qijia Shen — personal website

Live site: [michaelsqj.github.io](https://michaelsqj.github.io/)

This repository contains the source for Qijia Shen's personal academic website.
The site introduces current work, research, writing, reading notes, slides, and
the curriculum vitae.

## Branches

- `main` contains this repository guide.
- `src` contains the maintained Jekyll website source.
- GitHub Actions builds and publishes the website from `src`.
- Do not edit or force-push `gh-pages`; it is not the maintained source.

All website content changes must be made on the `src` branch.

## Update content in GitHub

For a small manual edit:

1. Open the repository on GitHub.
2. Select the `src` branch from the branch menu.
3. Open the relevant file listed below.
4. Select the pencil icon, make the change, and preview the diff.
5. Commit directly to `src`, or create a pull request if the change needs
   review.
6. Open the repository's **Actions** tab and wait for
   **Build and deploy GitHub Pages** to finish successfully.
7. Verify the result at [michaelsqj.github.io](https://michaelsqj.github.io/).

## Content map

| Content | File or directory |
| --- | --- |
| Homepage introduction | `index.html` |
| Social and contact links | `_data/profile.yml` |
| Research entries and links | `_data/research.yml` |
| Experience and education | `_data/timeline.yml` |
| Finished essays | `_posts/` |
| Announced writing status pages | `writing/` |
| Reading topics and paper collections | `_reading/` |
| Historical MRI archive grouping | `_data/mri_archive.yml` |
| Slides page | `slides.html` |
| CV files | `assets/cv/Qijia_Shen_CV.pdf` and `.docx` |
| Site styling | `assets/css/style.css` |

The repository-specific maintenance rules are documented in
`.agents/skills/maintain-quiet-scholar-site/` on the `src` branch.

## Add or edit research

Edit `_data/research.yml`. Keep each summary factual and limited to one concise
sentence.

```yaml
- direction: Agentic AI
  title: "Research title"
  period: "2026"
  tags: "Agent environments · Reinforcement learning"
  summary: "One concise factual summary."
  paper: "https://..."
  code: "https://..."
  featured: false
  order: 10
```

Supported optional links include `paper`, `preprint`, `code`, and
`related_code`. Preserve the direction order:

1. Agentic AI
2. Generative 3D & Vision
3. Medical Imaging & Neuroscience

Do not mark historical MRI or medical-imaging work as ongoing.

## Write and publish a blog post

Create `_posts/YYYY-MM-DD-short-slug.md`:

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

Start article headings at `##`; the layout supplies the page title.

- Use fenced code blocks with a lower-case language identifier.
- Use `$...$` for inline math and `$$...$$` for display math.
- Use `{% cite key %}` for formal citations and add its BibTeX entry to
  `_bibliography/papers.bib`.
- Add descriptive alternative text to meaningful images.

Example article body:

````markdown
## Why this problem matters

Introduce the problem, assumptions, and the main question.

## Minimal implementation

```python
def clipped_objective(ratio, advantage, epsilon=0.2):
    unclipped = ratio * advantage
    clipped = ratio.clip(1 - epsilon, 1 + epsilon) * advantage
    return min(unclipped, clipped)
```

## Mathematical view

For a policy ratio $r_t(\theta)$ and advantage estimate $\hat{A}_t$:

$$
L^{\mathrm{clip}}(\theta)
=
\mathbb{E}_t
\left[
\min\left(
r_t(\theta)\hat{A}_t,
\operatorname{clip}(r_t(\theta),1-\epsilon,1+\epsilon)\hat{A}_t
\right)
\right].
$$

## Evidence and limitations

State what was measured, what remains uncertain, and the practical trade-offs.

## References

Use the citation key in prose: {% cite example2026 %}

{% bibliography --cited %}
````

Add the matching record to `_bibliography/papers.bib`:

```bibtex
@article{example2026,
  title   = {Paper title},
  author  = {Author, A. and Author, B.},
  journal = {arXiv preprint},
  year    = {2026},
  url     = {https://arxiv.org/abs/...}
}
```

For post-specific images:

1. Add the file under `assets/images/<post-slug>/`.
2. Reference it with an absolute site path:

   ```markdown
   ![Description of what the figure shows](/assets/images/<post-slug>/figure.png)
   ```

An unfinished essay may have a stable page in `writing/`, but it must be
clearly labeled **Work in progress** and must not contain placeholder article
content.

When the essay is finished:

1. Add the completed Markdown post to `_posts/`.
2. Remove its work-in-progress card from `writing.html`.
3. Update any homepage card in `index.html` to use the generated post URL.
4. Build locally and check code highlighting, equations, citations, images,
   and mobile layout before pushing.

## Add or edit a reading topic

Use one evolving Markdown file per topic in `_reading/`:

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

Group papers by date or concept. For each paper, include a direct paper link, a
neutral summary, and optionally a short **Quick take**. Reading topics are
collections of related papers, not one page per paper.

## Add or update slides

Only list a real, publicly releasable deck. Remove speaker notes, internal
results, private links, credentials, and demo text before publishing.

### Publish a PDF deck

1. Create `assets/slides/` if it does not exist.
2. Add a clearly named PDF such as
   `assets/slides/terminal-agent-rl-2026.pdf`.
3. Edit `slides.html` on `src`.
4. Remove the current empty-state section after the first public deck is added.
5. Add a section like this:

```html
<section class="section">
  <p class="section-kicker">Talk · Event name · 2026</p>
  <h2>Talk title</h2>
  <p class="page-lead">One factual sentence describing the talk.</p>
  <iframe
    class="slide-frame"
    src="{{ '/assets/slides/terminal-agent-rl-2026.pdf' | relative_url }}"
    title="Talk title slides">
  </iframe>
  <p>
    <a class="text-link"
       href="{{ '/assets/slides/terminal-agent-rl-2026.pdf' | relative_url }}">
      Download PDF
    </a>
  </p>
</section>
```

### Embed a public online deck

Use the provider's public embed URL, not its edit URL. For example:

```html
<section class="section">
  <p class="section-kicker">Talk · Event name · 2026</p>
  <h2>Talk title</h2>
  <p class="page-lead">One factual sentence describing the talk.</p>
  <iframe
    class="slide-frame"
    src="PUBLIC_EMBED_URL"
    title="Talk title slides"
    loading="lazy"
    allowfullscreen>
  </iframe>
  <p><a class="text-link" href="PUBLIC_VIEW_URL">Open slides ↗</a></p>
</section>
```

For every deck, provide a real title, event, date, short description, accessible
iframe title, and a direct PDF or public-view fallback. Test embedded decks in a
private browser window to confirm that visitors do not need your account.

## Update the CV

Replace both files while preserving their exact names:

- `assets/cv/Qijia_Shen_CV.pdf`
- `assets/cv/Qijia_Shen_CV.docx`

Keeping these paths stable prevents existing links from breaking.

## Preview changes locally

```bash
git clone https://github.com/Michaelsqj/Michaelsqj.github.io.git
cd Michaelsqj.github.io
git switch src
bundle install
bundle exec jekyll build
bundle exec jekyll serve
```

Open `http://127.0.0.1:4000/`.

Before publishing, confirm that:

- the build completes;
- navigation and edited links work;
- both CV files are present;
- historical MRI note URLs still build;
- no demo, sample, placeholder, or fabricated public content was added.

Then publish:

```bash
git add <changed-files>
git commit -m "Describe the website update"
git push origin src
```

The GitHub Pages workflow deploys the successful build automatically.
