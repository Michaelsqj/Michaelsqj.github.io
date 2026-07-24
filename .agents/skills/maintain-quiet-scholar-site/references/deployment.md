# Build and deployment

## Branch model

- `src` is the maintained Jekyll source and deployment branch.
- GitHub Actions builds `_site` and deploys the Pages artifact.
- Do not manually edit or force-push `gh-pages`.
- The retired Travis and branch-rewrite deployment scripts have been removed.
  Do not reintroduce them.

## Local validation

```bash
bundle install
bundle exec jekyll build
bundle exec jekyll serve
```

The local site is available at `http://127.0.0.1:4000/`.

## Publish

1. Review `git status` and the diff.
2. Build successfully.
3. Commit source changes.
4. Push `src`.
5. Watch `.github/workflows/pages.yml` with `gh run watch`.
6. Verify `https://michaelsqj.github.io/`.

GitHub repository Pages settings must use **GitHub Actions** as the source.

## Failure handling

- Build failures: inspect the workflow log, fix source, and push a new commit.
- Broken links: correct source data; never patch generated `_site`.
- Unsupported plugins: keep the custom Actions build rather than switching to
  branch-based GitHub Pages.
- Never commit `_site`, `vendor`, local caches, or credentials.
