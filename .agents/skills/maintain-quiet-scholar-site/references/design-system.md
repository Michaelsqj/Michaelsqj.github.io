# Quiet Scholar design system

## Visual character

Use a calm academic/editorial presentation: warm paper background, near-black
ink, muted navy, restrained brown accent, serif prose, sans-serif metadata,
thin borders, and generous whitespace.

Core tokens live at the top of `assets/css/style.css`. Reuse them rather than
introducing one-off colors.

## Structure

- Desktop: sticky 210 px left rail and a broad reading column.
- Mobile: single column; hide the rail navigation only at the existing small
  breakpoint.
- Pages use a clear header, content sections, and a minimal footer.
- Research is grouped by direction, not by a separate Projects section.
- Reading uses topic cards; a topic contains many annotated papers.

## Components

Reuse existing classes:

- `.page`, `.rail`, `.monogram`
- `.masthead`, `.page-header`, `.page-lead`
- `.section`, `.section-head`, `.section-kicker`
- `.work-list`, `.work-item`
- `.direction`, `.research-list`, `.research-entry`
- `.topic-grid`, `.topic-card`, `.topic-article`
- `.archive-groups`, `.archive-group`, `.archive-list`
- `.timeline`, `.timeline-item`
- `.button`, `.text-link`, `.entry-links`

## Avoid

- Decorative identity slogans or location/year labels.
- Fake metrics, testimonials, publication counts, or status badges.
- Demo decks, placeholder articles, planned empty sections.
- Excessive animation, shadows, gradients, glass effects, or saturated color.
- Model-authored decorative SVGs.

## Accessibility

Preserve semantic headings, visible focus states, descriptive links, alt text,
keyboard-operable controls, and responsive layouts. External interface-card
links may open in a new tab; prose links should behave normally.
