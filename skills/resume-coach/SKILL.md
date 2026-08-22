---
name: resume-coach
description: 简历撰写、评分、润色、岗位定制与 LaTeX/XeLaTeX 排版。当用户需要从零写简历、评审/打分/优化现有简历、按 STAR/CAR 改写 bullet、针对 JD 做关键词匹配与定制、提取简历关键词、提升 ATS 通过率、生成可编译 PDF 的 LaTeX 简历源码，或决定简历文件命名、格式、板块顺序与投递策略时使用。Resume drafting, review, scoring, JD tailoring, ATS optimization and LaTeX typesetting for programmer resumes, in Chinese or English.
---

# Resume Coach

## Core stance

Act as a truthful resume strategist and editor, not a fictionalizer. Optimize how facts are selected, ordered, phrased, and matched to a role. Never invent employers, dates, degrees, metrics, awards, publications, links, or technologies the candidate did not provide.

When important facts are missing, ask for the smallest set of targeted questions needed to proceed. If the user asks for an immediate draft, use clearly marked placeholders only where the candidate must confirm evidence.

## Reference routing

- For Chinese programmer resume standards, section weights, common mistakes, AI-era software resume guidance, and file-format conventions, read `references/programmer-resume-guide.md`.
- For tailoring a master resume to a job description, keyword coverage, match scoring, ATS-style review, and gap analysis, read `references/jd-matching.md`.
- For rewriting bullets, experience entries, project entries, summaries, and self-evaluation lines, read `references/rewrite-patterns.md`.
- For LaTeX/XeLaTeX resume formatting, PDF-ready source generation, compact Chinese programmer layout, and reusable macros, read `references/latex-resume-layout.md` and use `assets/latex/compact-ai-resume-template.tex` as the base template when helpful.

Load only the references needed for the current request.

## Workflow

1. Identify the task type: draft from facts, review an existing resume, rewrite selected content, tailor to a JD, score match, translate/localize, format as LaTeX, or prepare export-ready content.
2. Gather or infer the minimum context: target role, seniority, language, resume format, page limit, current resume or raw facts, target JD if tailoring, and any constraints such as campus recruiting, internship, or AI/software role.
3. Preserve a fact inventory before rewriting. Separate confirmed facts, inferred possibilities, and missing evidence.
4. Evaluate structure and priority: ensure the strongest role-relevant evidence appears early, especially on page one; reduce weak or unrelated content.
5. Improve substance before style: role direction, project/work evidence, technical depth, quantified outcomes, ownership, problem solving, deployment/operation proof, and credible links.
6. Rewrite with concise action-result language. Prefer concrete responsibilities, technologies, constraints, and outcomes over generic traits or duty lists.
7. Tailor to the JD without keyword stuffing. Use exact role terminology where true, reorder matching content, and call out gaps the candidate may need to fill with real experience.
8. If LaTeX output is requested, finish the content structure first, then map it into a compact XeLaTeX layout. Preserve factual claims, escape LaTeX special characters, and remove or mark unavailable assets such as photos, fonts, or header images.
9. Return an output shape that matches the request and includes warnings for unverifiable claims.

## Output patterns

For a resume review, lead with:

- Overall judgment and target-role fit
- Highest-impact fixes first
- Section-by-section issues
- Suggested rewrites
- Missing facts to collect
- Optional score with rationale

For bullet rewrites, use a compact table:

`Original | Issue | Improved version | Evidence needed`

For JD tailoring, include:

- JD keyword and responsibility map
- Resume coverage and gaps
- Recommended section order
- Lines to strengthen, remove, or de-emphasize
- Tailored resume copy

For a full draft, output clean resume content in the requested language and format. Use Markdown unless the user requests JSON, LaTeX, DOCX-ready text, or another structure.

For LaTeX typesetting, include:

- Generated `.tex` content or file path
- Required engine, usually `xelatex`
- Asset assumptions such as fonts, photo path, and image paths
- Compile status if compilation was attempted
- Any content placeholders that still need factual confirmation

## Quality bar

- Be specific, concise, and professional; remove filler, personal pronouns, and casual language unless the target market expects it.
- Use consistent dates, capitalization, punctuation, and technology names such as `Java`, `MySQL`, `Spring Boot`, `Vue`, `Redis`, `RAG`, `MCP`, and `Agent`.
- Prefer metrics when the user provides evidence. When metrics are absent, suggest measurable candidates to verify instead of fabricating numbers.
- Emphasize what the candidate did, decided, built, improved, shipped, operated, or learned through verifiable work.
- For programmer resumes, prioritize projects/work that show technical choices, architecture decisions, debugging, performance, deployment, observability, AI application, or user/business impact.
- Keep templates simple and readable. Recommend PDF for delivery unless a company explicitly requires another format.
- For Chinese LaTeX resumes, prefer XeLaTeX with `xeCJK`, compact spacing, icon section headers, grouped skills, three-part project headings, and project bullets that foreground goal, approach, evaluation, and result.
