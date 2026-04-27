# Contributing

Thank you for your interest in this ISO/IEC 27017 + 27018 Cloud Security Toolkit. Contributions are welcome under the project's MIT licence.

## Ways to contribute

- **Issues:** Report errors, gaps, or improvement ideas via GitHub Issues.
- **Pull Requests:** Submit additions or corrections.
- **Discussions:** Share implementation patterns, lessons learned, or maturity examples.

## Standards alignment

All contributed content should:

1. Reference relevant clauses / controls (ISO/IEC 27001:2022, 27017:2015, 27018:2019, 27701:2019, 27002:2022) where applicable.
2. Use the existing footer pattern: `Document ID | Version | Classification | Owner | Review`.
3. Use UK-English spelling (the rest of the toolkit follows this convention).
4. Stay vendor-neutral where possible (avoid hard-coding to a single CSP).

## Pull request process

1. Fork the repository.
2. Create a feature branch (`feat/short-description`).
3. Make changes, ensuring documents render correctly in GitHub Markdown.
4. Update the Document Master List (06-SUPPORT) if a controlled document is added or removed.
5. Submit a PR with a clear description and any cross-references to ISO clauses.
6. The maintainers review for technical accuracy, consistency, and copyright compliance.

## Style guide

- Headings use sentence case (except for ISO standard names and acronyms).
- Tables preferred over long bullet lists when comparing items.
- Avoid quoting ISO standard text verbatim — paraphrase and reference the clause/control number.
- Avoid copying long passages from other public sources.

## Code contributions (`13-SCRIPTS/`)

- Python 3.9+; standard library where possible.
- PEP 8 + type hints.
- Tests welcomed under `tests/`.

## Code of conduct

Be kind. We follow a standard "be respectful, assume good faith, no harassment" policy. Reports may be sent to the maintainers via GitHub.

## Licence

By contributing you agree your contributions are licensed under the MIT Licence in this repository.

## Acknowledgements

This toolkit benefits from the work of standards bodies, the broader privacy and cloud-security community, and contributors who share generously.
