# CONVENTIONS.md

Project conventions for the Tribhuvan University (TU) minor project report: a
LoRaWAN + TinyML forest fire / illegal logging monitoring system.

## Directory layout

- `main.tex` — root document (`\documentclass{report}`).
- `section/` — chapter and prefatory sources, included via `\include` /
  `\input` from `main.tex`.
- `Graphics/` — **all** image assets. Kept here exclusively; nothing is stored
  at the repo root.
- `refrences/ref.bib` — bibliography (note: the directory name is intentionally
  misspelled `refrences`, not `references`). The root `ref.bib` is unused —
  do not confuse the two.

## Image (graphics) convention

- Every image lives in `Graphics/`; none are kept in the repo root.
- File names are `snake_case`:
  - lowercase, underscores between words (`system_architecture.png`).
  - no spaces, no mixed-case, no title case.
- Format reflects content: `.png` for raster, `.pdf` for vector.
- Reference images by **bare filename** — do **not** prefix paths. The
  preamble sets `\graphicspath{{./Graphics/}}`, so bare names resolve into
  `Graphics/`:
  ```latex
  \includegraphics[width=\textwidth]{system_architecture.png}
  ```
  (not `Graphics/system_architecture.png`).
- `\includegraphics` is placed inside a `figure` environment with `\centering`,
  a `\caption`, and a `\label` of the form `fig:snake_case`.

## Naming outside images

- Referenced figures/tables use snake_case labels (`fig:ldse-epoch`,
  `tab:memory-budget`), mirroring the image filenames.

## Build

Compile in order (BibTeX, not biber; `ieeetr` style, `natbib` loaded as
`\usepackage[numbers,sort&compress]{natbib}`):

```
pdflatex main
bibtex main
pdflatex main
pdflatex main   # resolve cross-references / TOC
```

- `pdflatex` / `bibtex` are not on PATH. Call them by full MiKTeX path:
  `C:\Users\Chitra\AppData\Local\Programs\MiKTeX\miktex\bin\x64\`.
- No build script or Makefile exists.

## Chapter vs. subsection include rule

- `\include{}` (chapters) forces a new page; `\input{}` (cover, title, appendix
  sub-sections, numbered section-subsections like `3_1_*`) does not.

## TU formatting

All TU formatting (chapter numbering `3-1`, Times New Roman via `mathptmx`,
line spacing, heading formats) is enforced in the `main.tex` preamble. Keep
formatting changes there, not in `section/` files.