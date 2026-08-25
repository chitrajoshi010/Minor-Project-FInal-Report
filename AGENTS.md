# AGENTS.md

LaTeX report for a Tribhuvan University (TU) minor project on a LoRaWAN + TinyML forest fire / illegal logging monitoring system.

## Build

- Root document is `main.tex` (`\documentclass{report}`).
- Compile in order (BibTeX, not biber; `ieeetr` style, `natbib` loaded):
  ```
  pdflatex main
  bibtex main
  pdflatex main
  pdflatex main   # resolve cross-references / TOC
  ```
- No build script or Makefile exists; run the toolchain manually from the repo root.
- `pdflatex`/`bibtex` are NOT on PATH. MiKTeX is installed at `C:\Users\Chitra\AppData\Local\Programs\MiKTeX\miktex\bin\x64\` — call the tools by full path (e.g. `& "C:\Users\Chitra\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe" -interaction=nonstopmode -halt-on-error main`).
- Bibliography source is `refrences/ref.bib` (note: the directory is intentionally misspelled `refrences`, not `references`). There is also an unused `ref.bib` at the repo root — don't confuse the two.

## Layout

- Images are loaded from `Graphics/` via `\graphicspath{{./Graphics/}}`; reference them by **bare snake_case filename** (no `Graphics/` prefix), e.g. `\includegraphics{system_architecture.png}`. All assets live in `Graphics/` — nothing at the repo root. See `CONVENTIONS.md` for the full conventions.
- Chapter sources live in `section/`. Files with numbered stems (`3_1_*`, `5_*`, `6_*`, `7_*`) are usually `\input` targets of other chapter/`appendices.tex` files, not standalone `\include`s.
- `\include{}` (chapters) forces a new page; `\input{}` (cover, title, appendix sub-sections) does not.
- TU formatting (chapter numbering `3-1`, Times New Roman, line spacing, heading formats) is all enforced in `main.tex` preamble — keep formatting changes there, not in section files.
- Chapter structure tracks the TU Final Report template (`1. Final_Report_Template_and_Guidelines_2020.pdf`): 1 Introduction, 2 Literature Review, 3 Requirement Analysis (3.2 Feasibility), 4 System Architecture & Methodology, 5 Implementation Details, 6 Result and Analysis, 7 Future Enhancements, 8 Conclusion, 9 Appendices, References unnumbered last.
- Appendices are ONE numbered `\chapter{APPENDICES}` (`section/appendices.tex`) with `\section*{Appendix A/B/C: ...}` sub-headings (added to TOC via `\addcontentsline{toc}{section}`) — matching the template's TOC (`9 APPENDICES` + indented `Appendix A: ...`) rather than the `appendix` package's lettered A/B/C chapters. Tables/figures inside become `Table 9-x` / `Fig 9-x`. Do NOT revert to `\begin{appendices}` chapter mode.

## List spacing convention (TOC / LOF / LOT)

- Per the guidelines, the TOC/List of Figures/List of Tables use **1.0 line spacing** with `\parskip=0pt` so entries are tight; body text stays 1.5.
- Implemented in `section/lists.tex` by wrapping each list in `{\setstretch{1}\setlength{\parskip}{0pt}\titlespacing*{\chapter}{0pt}{-11.2pt}{12pt}\...}`. The `-11.2pt` before-sep is a calibrated value that keeps the list *headings* top-aligned (≈79pt from page top, matching chapter/section headings) despite the single-spacing; the global chapter spacing in `main.tex` is `-36.4pt`. If list headings drift after an edit, re-measure heading `y` with `pdftotext -bbox` and adjust that one value.
- `main.tex` `\titlecontents{figure}`/`\titlecontents{table}` use `\addvspace{0pt}` so LOF/LOT entries have no extra gap.

## Gotchas

- `natbib` is loaded as `\usepackage[numbers,sort&compress]{natbib}`. Do NOT revert to bare `\usepackage{natbib}`: it defaults to author-year style, which clashes with the numeric `ieeetr` bibliography style and aborts compilation with "Bibliography not compatible with author-year citations".
- File names are case-inconsistent (`section/Acknowledgement.tex` is included as `acknowledgement`). This works only on case-insensitive filesystems (Windows). Don't rely on it if the repo is moved to Linux/macOS.
- `result and analysis.tex` previously contained spaces (breaking BibTeX's `.aux` parsing); it is now `section/result_and_analysis.tex`. Keep filenames free of spaces for BibTeX.
- `\title{Project Title}` in `main.tex` is a placeholder; the metadata `\author` block lists the actual team/IDs.