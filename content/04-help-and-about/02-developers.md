# Developers

*Digital Software Development T Level → Developers*

This page is for anyone who wants to know how the site is built, contribute a fix or a new page, or get in touch with the person maintaining it.

## About this project

This is an independent study-guide project built and maintained by **Samuel O'Connell**, part of the [UTC Leeds T Level Study Guides](https://lana6478.github.io/utc-leeds-t-levels/) family.

- GitHub: [github.com/lana6478](https://github.com/lana6478)
- Email: [samueloconnell62@gmail.com](mailto:samueloconnell62@gmail.com)
- Source code: [github.com/lana6478/T-level-Digital-Software-Development](https://github.com/lana6478/T-level-Digital-Software-Development)

Found a mistake, an out-of-date detail, or want a topic covered in more depth? Open an [issue](https://github.com/lana6478/T-level-Digital-Software-Development/issues) on GitHub, or email directly - both are welcome.

## How the site is built

The whole project is two things living in one repository:

- **`content/`** - the actual study-guide library: plain markdown files, organised into folders by topic.
- **`docs/`** - a small, dependency-free static website (plain HTML, CSS and JavaScript, plus [marked.js](https://marked.js.org/) for rendering markdown in the browser) built for GitHub Pages. It reads its page list and page content from `docs/content/`, a generated mirror of `content/` - so the website always shows exactly what's in the file library.

There's no build framework, no bundler, and no server-side code.

## Rebuilding the site after an edit

After adding, editing or removing anything under `content/` (or `assets/`), regenerate the site data from the repository root:

```bash
python3 tools/build_site.py
```

This copies every file from `content/` into `docs/content/`, copies shared images from `assets/img/` into `docs/assets/img/`, and rebuilds `docs/assets/data/manifest.json` (sidebar tree) and `docs/assets/data/search-index.json` (search index).

Then preview it locally:

```bash
cd docs
python3 -m http.server 8000
# open http://localhost:8000
```

## Contributing a page

1. Add a new `.md` file under the right `content/` subfolder, following the existing page template: an `# H1` title, an italic breadcrumb line, `##` sections, a closing **Key terms** list, and a **Related pages** list of relative links to nearby pages.
2. Keep filenames lowercase and hyphenated, with a number prefix (`01-`, `02-`, ...) where order matters.
3. Run `python3 tools/build_site.py` so the website picks up the change.
4. Open a pull request.

## License and content note

This project paraphrases and reorganises the official T Level Technical Qualification in Digital Software Development specification (Pearson, v1.1, August 2026) for easier navigation. It is unofficial and unaffiliated with Pearson or the Institute for Apprenticeships and Technical Education (IfATE). See [Sources and Further Reading](../sources-and-further-reading.md) for the primary, authoritative documents.

## Key terms

- **`content/`** - the canonical markdown study-guide library.
- **`docs/`** - the generated GitHub Pages website that reads from `content/`.
- **`tools/build_site.py`** - the script that mirrors `content/` into `docs/content/` and rebuilds the site's directory tree and search index.

## Related pages

- [Help](01-help.md)
- [Sources and Further Reading](../sources-and-further-reading.md)
