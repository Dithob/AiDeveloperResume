# LaTeX Resume Layout

Use this reference when the user asks to format, typeset, convert, or export a resume as LaTeX, especially for Chinese programmer resumes.

## Layout model

Use XeLaTeX for Chinese resumes. Prefer `article` with `10pt`, `geometry`, `fontspec`, `xeCJK`, `fontawesome5`, `titlesec`, `enumitem`, `hyperref`, `xcolor`, `graphicx`, and optional `tikz` for a full-width contact bar.

The compact AI/software resume layout should use:

- A4 paper with tight but readable margins, usually left/right around `1.0-1.2cm`, top around `0.7-0.9cm`, bottom around `0.8-1.0cm`.
- No paragraph indentation, no page numbers, compact line spacing around `1.05-1.10`.
- Section headings with a colored icon, bold title, and a thin horizontal rule.
- Top contact strip for phone, email, GitHub, homepage, or portfolio.
- Personal information and education in a left minipage; optional photo in a right minipage.
- Project and work headings in a three-part line: item name, role, dates.
- Dense but readable `itemize` settings: small left margin, low `itemsep`, low `topsep`.

Use `assets/latex/compact-ai-resume-template.tex` as the base when the user wants a full LaTeX file.

## Content-to-layout mapping

Map structured resume content to sections in this order unless the target role suggests otherwise:

1. Personal information and target role
2. Education
3. Professional skills
4. Internship or work experience
5. Project experience
6. Awards, certificates, papers, patents, or selected achievements
7. Optional self-evaluation only when evidence-backed

For AI/software roles, foreground the role direction in personal information and make `AI 应用开发`, `RAG`, `Agent`, `MCP`, `模型微调`, `推理部署`, `工程交付`, and relevant backend/full-stack skills discoverable in the skills and project sections when true.

## Style choices to preserve

Borrow these strengths from the reference resume:

- Clear first-screen positioning: name, school, degree, and target role are immediately visible.
- Contact information is compact and visually separated from content.
- Icons help scanning without taking much space.
- Skills are grouped by capability, not by a raw keyword pile.
- Experience bullets start with bold labels such as `项目目标`, `应用架构设计`, `评估与自修正闭环`.
- Project bullets combine scenario, technical approach, and measurable result.
- Awards and papers are compressed into one concise section.
- Optional sections are commented out rather than forced into the visible resume.

## LaTeX generation rules

When producing LaTeX:

- Escape special characters in user content: `#`, `$`, `%`, `&`, `_`, `{`, `}`, `~`, `^`, and backslashes unless intentionally writing LaTeX commands.
- Use `\href{mailto:...}{...}` for email and `\href{https://...}{...}` for links.
- Use `--` for date ranges such as `2025.06--2025.09`.
- Use `\%` for percentages in metrics.
- Keep Chinese punctuation consistent.
- Do not hard-code local image or font paths unless the user provides them.
- If the user has no photo or image assets, remove the photo minipage and let the information block take the full width.
- If a contact-bar background image is unavailable, use a colored `tikz` rectangle or a plain text contact row instead.
- Keep commented alternative projects only when the user explicitly wants a master resume source; otherwise generate a clean final file.

## Compile guidance

For Chinese resumes, recommend:

```bash
xelatex resume.tex
```

If compilation fails:

- Check whether the CJK font exists and either switch to a system font or use a bundled font path.
- Check image paths for the contact bar and photo.
- Check unescaped `%`, `_`, `&`, or `#` in resume content.
- Check that `fontawesome5` is installed; if not, remove icons or use text headings.

When asked to create a PDF and a TeX engine is available, run XeLaTeX and inspect warnings/errors. If not available, still produce a clean `.tex` file and tell the user it has not been compiled.

## Output shape

For a LaTeX conversion request, return:

- The generated `.tex` file path when writing files
- Any required assets or missing placeholders
- Compile command
- A brief list of assumptions, especially omitted photo, missing metrics, or unverified links
