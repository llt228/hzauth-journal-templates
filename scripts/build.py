#!/usr/bin/env python3
"""Generate one self-contained LaTeX template directory per included journal.

Data source: catalog/journals.json (derived from the HZAU journal ranking
workbook).  Official publisher classes live in assets/ and are copied
unmodified into every journal directory so that each directory is
self-contained.

Usage:
    python3 scripts/build.py            # regenerate journals/ and catalog CSVs
    python3 scripts/build.py --compile  # also compile every main.pdf
"""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
JOURNALS_DIR = ROOT / "journals"
CATALOG_DIR = ROOT / "catalog"

TEMPLATE_META = {
    "elsarticle": {
        "name": "elsarticle",
        "display": "Elsevier elsarticle",
        "version": "3.4 (2024/04/04)",
        "publisher": "Elsevier",
        "source": "https://ctan.org/pkg/elsarticle",
        "guidelines": "https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions",
        "license": "LPPL 1.3",
        "files": ["elsarticle.cls", "elsarticle-num.bst", "elsarticle-num-names.bst", "elsarticle-harv.bst"],
    },
    "achemso": {
        "name": "achemso",
        "display": "ACS achemso",
        "version": "3.13g (2024-01-30)",
        "publisher": "American Chemical Society",
        "source": "https://ctan.org/pkg/achemso",
        "guidelines": "https://pubs.acs.org/page/4authors/submission/tex.html",
        "license": "LPPL 1.3",
        "files": ["achemso.cls", "achemso.sty", "achemso.bst", "natmove.sty"],
    },
    "ieeetran": {
        "name": "IEEEtran",
        "display": "IEEE IEEEtran",
        "version": "1.8b (2015/08/26)",
        "publisher": "IEEE",
        "source": "https://ctan.org/pkg/ieeetran",
        "guidelines": "https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/",
        "license": "LPPL 1.3",
        "files": ["IEEEtran.cls", "IEEEtran.bst", "IEEEtrantools.sty"],
    },
    "revtex": {
        "name": "revtex4-2",
        "display": "APS REVTeX 4.2",
        "version": "4.2f (2022/06/05)",
        "publisher": "American Physical Society",
        "source": "https://ctan.org/pkg/revtex",
        "guidelines": "https://journals.aps.org/rmp/authors",
        "license": "LPPL 1.3",
        "files": None,  # copy the whole assets/revtex directory
    },
    "oup": {
        "name": "oup-authoring-template",
        "display": "Oxford University Press authoring template",
        "version": "1.5 (2026/07/14)",
        "publisher": "Oxford University Press",
        "source": "https://ctan.org/pkg/oup-authoring-template",
        "guidelines": "https://academic.oup.com/pages/authoring/journals",
        "license": "LPPL 1.3",
        "files": ["oup-authoring-template.cls", "oup-plain.bst", "oup-abbrvnat.bst"],
    },
}

# Journal titles whose official form differs from the spelling used in the
# ranking workbook.  These are display titles only; catalog names stay verbatim.
EXTRA_TITLE_OVERRIDES = {
    "Global Environmental Change-Human and Policy Dimensions": "Global Environmental Change",
    "Physics Reports-Review Section of Physics Letters": "Physics Reports",
    "Materials Science & Engineering R-Reports": "Materials Science and Engineering: R: Reports",
}

HEADER = r"""% !TeX program = pdflatex
% ============================================================================
%  期刊（目录原表名称）：@@NAME@@
%  期刊（官方标题）    ：@@TITLE@@
%  分级                ：@@LEVEL@@（@@SHEET@@）
%  出版商              ：@@PUBLISHER@@
%  官方文档类          ：@@TEMPLATE_DISPLAY@@ v@@VERSION@@
%  文档类来源          ：@@SOURCE@@
%  投稿指南            ：@@GUIDELINES@@
%  文档类许可证        ：@@LICENSE@@（类文件未作任何修改）
% ============================================================================
%  这是投稿模板，不是真实论文。标题、作者、单位、摘要、正文、图表和文献
%  都是示例内容，请全部替换为您自己的材料。
%
%  请勿修改随附的 .cls / .sty / .bst 文件；排版由出版商官方文档类负责。
%  编译：latexmk -pdf main.tex
% ============================================================================
"""

REFERENCES_BIB = r"""% Example bibliography for template demonstration only.
% Replace every entry with your real references.
@article{example2024,
  author  = {Author, Example A. and Author, Example B.},
  title   = {An Example Journal Article for Template Demonstration},
  journal = {Journal of Examples},
  year    = {2024},
  volume  = {1},
  number  = {1},
  pages   = {1--10},
  doi     = {10.0000/example.2024.001}
}

@book{example2020,
  author    = {Author, Example C.},
  title     = {An Example Monograph for Template Demonstration},
  publisher = {Example Press},
  address   = {Example City},
  year      = {2020}
}
"""

LATEXMKRC = r"""# latexmk configuration for this journal template.
# Default engine: pdflatex (all classes in this repository compile with it).
$pdf_mode = 1;
$bibtex_use = 2;
$pdflatex = 'pdflatex -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$clean_ext = 'bbl blg run.xml synctex.gz nav snm vrb';
"""

GITIGNORE = r"""# LaTeX intermediate files
*.aux
*.log
*.out
*.toc
*.lof
*.lot
*.bbl
*.blg
*.fls
*.fdb_latexmk
*.synctex.gz
*.run.xml
*.nav
*.snm
*.vrb
*.bcf
*.spl
mainNotes.bib
acs-main.bib

# Keep the compiled preview that the template market uses as a cover.
!main.pdf
"""


def tex_escape(value: str) -> str:
    """Escape LaTeX special characters in a plain journal title."""
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in value)


def render(text: str, mapping: dict[str, str]) -> str:
    for key, value in mapping.items():
        text = text.replace(f"@@{key}@@", value)
    return text


def template_info(journal: dict) -> dict:
    meta = dict(TEMPLATE_META[journal["template"]])
    if journal["template"] == "achemso":
        code = journal.get("achemso_code", "")
        meta["files"] = list(meta["files"]) + [f"achemso-{code}.cfg"]
    return meta


def common_header(journal: dict, meta: dict) -> str:
    mapping = {
        "NAME": journal["name"],
        "TITLE": journal["title"],
        "LEVEL": journal["level"],
        "SHEET": journal["sheet"],
        "PUBLISHER": journal["publisher"],
        "TEMPLATE_DISPLAY": meta["display"],
        "VERSION": meta["version"],
        "SOURCE": meta["source"],
        "GUIDELINES": meta["guidelines"],
        "LICENSE": meta["license"],
    }
    return render(HEADER, mapping)


def common_body(journal: dict) -> str:
    title = tex_escape(journal["title"])
    return rf"""\section{{Introduction}}
\label{{sec:introduction}}
This document is a submission template for \textit{{{title}}}. It is typeset
with the publisher's official \LaTeX{{}} document class; the class, not this
file, controls the page layout, fonts, and reference formatting. Every piece
of text in this sample---including the author names, affiliations, abstract,
and references---is a placeholder \cite{{example2024,example2020}}.

Replace the sample material with your own manuscript, but keep the document
class and the front-matter commands unchanged. Check the journal's current
Guide for Authors before submission because article types, word limits, and
reference styles can change.

\section{{Using this template}}
\label{{sec:usage}}
\begin{{itemize}}
  \item Edit \texttt{{main.tex}} only; the accompanying \texttt{{.cls}},
        \texttt{{.sty}}, and \texttt{{.bst}} files are official files and
        must remain unmodified.
  \item Put figures in \texttt{{figures/}} and include them with
        \verb|\includegraphics|; a sample vector figure is already provided.
  \item Replace the entries in \texttt{{references.bib}} and cite them with
        \verb|\cite|. The two entries shipped with the template are examples.
  \item Build the PDF with \texttt{{latexmk -pdf main.tex}}.
\end{{itemize}}

\section{{Mathematics, tables, and figures}}
\label{{sec:elements}}
Inline mathematics such as $E = mc^2$ and displayed equations are supported:
\begin{{equation}}
  \int_{{-\infty}}^{{\infty}} e^{{-x^{{2}}}}\,\mathrm{{d}}x = \sqrt{{\pi}}.
  \label{{eq:gaussian}}
\end{{equation}}

\begin{{table}}[t]
  \centering
  \caption{{An example table typeset with \texttt{{booktabs}}. Replace it with your own data.}}
  \label{{tab:example}}
  \begin{{tabular}}{{lcc}}
    \toprule
    Item & Value & Unit \\
    \midrule
    Alpha & 1.0 & a.u. \\
    Beta  & 2.0 & a.u. \\
    \bottomrule
  \end{{tabular}}
\end{{table}}

\begin{{figure}}[t]
  \centering
  \includegraphics[width=0.62\linewidth]{{figures/example-figure}}
  \caption{{An example vector figure. Replace the file in \texttt{{figures/}} with your own artwork.}}
  \label{{fig:example}}
\end{{figure}}

\section{{Conclusion}}
\label{{sec:conclusion}}
Replace this paragraph with the conclusion of your manuscript. The template
is intentionally minimal: journal-specific requirements should be taken from
the current author guidelines rather than added as local formatting hacks.
"""


def main_elsarticle(journal: dict, meta: dict) -> str:
    title = tex_escape(journal["title"])
    return common_header(journal, meta) + rf"""
\documentclass[preprint,12pt]{{elsarticle}}
\usepackage{{amsmath,amssymb}}
\usepackage{{graphicx}}
\usepackage{{booktabs}}
\usepackage[hidelinks]{{hyperref}}

\journal{{{title}}}

\begin{{document}}

\begin{{frontmatter}}
\title{{A \LaTeX{{}} Submission Template for \textit{{{title}}}}}

\author[a]{{First Author\corref{{cor1}}}}
\ead{{first.author@example.edu}}
\author[b]{{Second Author}}
\affiliation[a]{{organization={{Department of Example Science, Example University}},
                city={{Wuhan}}, postcode={{430070}}, country={{China}}}}
\affiliation[b]{{organization={{Example Research Institute}},
                city={{Beijing}}, postcode={{100190}}, country={{China}}}}
\cortext[cor1]{{Corresponding author.}}

\begin{{abstract}}
This document demonstrates the official Elsevier \texttt{{elsarticle}} class
configured for \textit{{{title}}}. It is a template, not a real manuscript:
replace the front matter, body text, figures, tables, and references with
your own material.
\end{{abstract}}

\begin{{keyword}}
template \sep \LaTeX \sep Elsevier \sep {title}
\end{{keyword}}
\end{{frontmatter}}

\maketitle

{common_body(journal)}
\section*{{Declaration of competing interest}}
The authors declare that they have no known competing financial interests or
personal relationships that could have appeared to influence this work.

\section*{{Data availability}}
Data sharing is not applicable to this template article.

\bibliographystyle{{elsarticle-num}}
\bibliography{{references}}

\end{{document}}
"""


def main_achemso(journal: dict, meta: dict) -> str:
    title = tex_escape(journal["title"])
    code = journal["achemso_code"]
    return common_header(journal, meta) + rf"""
\documentclass[journal={code},manuscript=article]{{achemso}}
\usepackage{{amsmath,amssymb}}
\usepackage{{graphicx}}
\usepackage{{booktabs}}
\usepackage[hidelinks]{{hyperref}}

\title{{A \LaTeX{{}} Submission Template for \textit{{{title}}}}}
\author{{First Author}}
\affiliation{{Department of Example Chemistry, Example University, Wuhan 430070, China}}
\email{{first.author@example.edu}}
\author{{Second Author}}
\affiliation{{Example Institute of Chemistry, Beijing 100190, China}}

\abbreviations{{a.u., arbitrary units}}
\keywords{{template, LaTeX, American Chemical Society, {title}}}

\begin{{document}}

\begin{{abstract}}
This document demonstrates the official ACS \texttt{{achemso}} class
configured for \textit{{{title}}}. It is a template, not a real manuscript:
replace the front matter, body text, figures, tables, and references with
your own material.
\end{{abstract}}

{common_body(journal)}
\section*{{Associated content}}
Supporting Information is not included in this template. Add it here when
your manuscript requires it.

\bibliography{{references}}

\end{{document}}
"""


def main_ieeetran(journal: dict, meta: dict) -> str:
    title = tex_escape(journal["title"])
    option = "magazine" if "Magazine" in journal["title"] else "journal"
    return common_header(journal, meta) + rf"""
\documentclass[{option},12pt]{{IEEEtran}}
\usepackage{{amsmath,amssymb}}
\usepackage{{graphicx}}
\usepackage{{booktabs}}
\usepackage{{cite}}
\usepackage[hidelinks]{{hyperref}}

\markboth{{{title}, Vol.~XX, No.~X, 2026}}{{}}

\title{{A \LaTeX{{}} Submission Template for\\\textit{{{title}}}}}
\author{{\IEEEauthorblockN{{First Author and Second Author}}
\IEEEauthorblockA{{Department of Example Engineering, Example University, Wuhan 430070, China\\Email: first.author@example.edu}}}}

\begin{{document}}
\maketitle

\begin{{abstract}}
This document demonstrates the official IEEE \texttt{{IEEEtran}} class
configured for \textit{{{title}}}. It is a template, not a real manuscript:
replace the front matter, body text, figures, tables, and references with
your own material.
\end{{abstract}}

\begin{{IEEEkeywords}}
template, LaTeX, IEEE, {title}
\end{{IEEEkeywords}}

{common_body(journal)}
\section*{{Acknowledgment}}
The authors thank the example reviewers for their comments.

\bibliographystyle{{IEEEtran}}
\bibliography{{references}}

\end{{document}}
"""


def main_revtex(journal: dict, meta: dict) -> str:
    title = tex_escape(journal["title"])
    return common_header(journal, meta) + rf"""
\documentclass[aps,rmp,reprint,superscriptaddress]{{revtex4-2}}
\usepackage{{amsmath,amssymb}}
\usepackage{{graphicx}}
\usepackage{{booktabs}}
\usepackage[hidelinks]{{hyperref}}

\begin{{document}}

\title{{A \LaTeX{{}} Submission Template for \textit{{{title}}}}}
\author{{First Author}}
\affiliation{{Department of Example Physics, Example University, Wuhan 430070, China}}
\author{{Second Author}}
\affiliation{{Example Institute of Physics, Beijing 100190, China}}

\begin{{abstract}}
This document demonstrates the official American Physical Society
\texttt{{revtex4-2}} class configured for \textit{{{title}}}. It is a
template, not a real manuscript: replace the front matter, body text,
figures, tables, and references with your own material.
\end{{abstract}}

\maketitle

{common_body(journal)}
\section*{{Acknowledgments}}
The authors thank the example funding agency for support.

\bibliographystyle{{apsrev4-2}}
\bibliography{{references}}

\end{{document}}
"""


def main_oup(journal: dict, meta: dict) -> str:
    title = tex_escape(journal["title"])
    return common_header(journal, meta) + rf"""
\documentclass[unnumsec,webpdf,modern,large]{{oup-authoring-template}}
\usepackage{{amsmath,amssymb}}
\usepackage{{graphicx}}
\usepackage{{booktabs}}
\usepackage[hidelinks]{{hyperref}}
\newcommand{{\societylogo}}{{}}%

\journaltitle{{{title}}}
\DOI{{10.0000/example}}
\copyrightyear{{2026}}
\pubyear{{2026}}
\vol{{XX}}
\issue{{X}}
\access{{Published: XX XX 2026}}
\appnotes{{Research Article}}
\firstpage{{1}}

\title[Short Article Title]{{A \LaTeX{{}} Submission Template for \textit{{{title}}}}}
\author[1,$\ast$]{{First Author}}
\author[2]{{Second Author}}
\address[1]{{\orgdiv{{Department}}, \orgname{{Example University}},
  \orgaddress{{\street{{Street}}, \postcode{{430070}}, \state{{Hubei}}, \country{{China}}}}}}
\address[2]{{\orgdiv{{Institute}}, \orgname{{Example Academy}},
  \orgaddress{{\street{{Street}}, \postcode{{100190}}, \state{{Beijing}}, \country{{China}}}}}}
\corresp[$\ast$]{{Corresponding author. \href{{mailto:first.author@example.edu}}{{first.author@example.edu}}}}
\received{{Date}}{{0}}{{Year}}
\revised{{Date}}{{0}}{{Year}}
\accepted{{Date}}{{0}}{{Year}}

\abstract{{
This document demonstrates the official Oxford University Press
\texttt{{oup-authoring-template}} class configured for \textit{{{title}}}.
It is a template, not a real manuscript: replace the front matter, body
text, figures, tables, and references with your own material.
}}

\keywords{{template, LaTeX, Oxford University Press, {title}}}

\begin{{document}}
\maketitle

{common_body(journal)}
\section*{{Funding}}
This template was prepared without external funding.

\bibliographystyle{{oup-plain}}
\bibliography{{references}}

\end{{document}}
"""


BUILDERS = {
    "elsarticle": main_elsarticle,
    "achemso": main_achemso,
    "ieeetran": main_ieeetran,
    "revtex": main_revtex,
    "oup": main_oup,
}


def journal_readme(journal: dict, meta: dict) -> str:
    return f"""# {journal['title']}

华中农业大学期刊分级目录：**{journal['level']}**（{journal['sheet']}）。

| 项目 | 内容 |
| --- | --- |
| 目录中的期刊名 | {journal['name']} |
| 出版商 | {journal['publisher']} |
| 官方文档类 | {meta['display']} `{meta['name']}` |
| 文档类版本 | {meta['version']} |
| 文档类来源 | <{meta['source']}> |
| 投稿指南 | <{meta['guidelines']}> |
| 文档类许可证 | {meta['license']} |

## 编译

```bash
latexmk -pdf main.tex
```

默认使用 `pdflatex` + BibTeX，产物为 `main.pdf`。本目录自带官方
`.cls` / `.sty` / `.bst` 文件，无需额外安装（TeX Live 2023 或更新版本）。

## 文件说明

- `main.tex`：论文入口，模板示例内容都在这里，替换为你的稿件。
- `main.pdf`：编译产物，供模板市场预览。
- `{meta['name']}.cls` 等：出版商官方文档类及其依赖，**请勿修改**。
- `references.bib`：示例文献库，请替换为真实文献。
- `figures/example-figure.pdf`：示例矢量图，替换为你的图片。
- `.latexmkrc`：latexmk 构建配置。
- `AGENTS.md`：供 AI 写作助手阅读的本目录约定。

## 说明

本模板的版式完全由出版商官方文档类决定；示例正文、作者、单位和
文献均为占位内容，不是真实论文。投稿前请以期刊最新的 Guide for
Authors 为准。
"""


def journal_agents(journal: dict, meta: dict) -> str:
    return f"""# AGENTS.md — {journal['title']}

本目录是《华中农业大学期刊分级目录（试行）》中 **{journal['level']}**
期刊 *{journal['title']}* 的 LaTeX 投稿模板。面向 AI 编码/写作助手。

## 权威来源

- 官方文档类：{meta['display']} `{meta['name']}`（{meta['version']}）
- 来源：{meta['source']}
- 投稿指南：{meta['guidelines']}
- 许可证：{meta['license']}

## 写作约定

1. 只编辑 `main.tex`、`references.bib` 和 `figures/` 下的文件。
2. **不要修改** `{meta['name']}.cls`、`.sty`、`.bst` 等官方文件；它们
   必须与出版商发布的版本逐字节一致。
3. 正文使用文档类提供的命令，不要用 `geometry`、`titlesec` 等宏包
   私自改动页面尺寸、字体或章节格式。
4. 文献放在 `references.bib`，用 BibTeX 生成；不要手写
   `thebibliography` 环境。
5. 图片放 `figures/`，用 `\\includegraphics` 引用；不要把图片放到
   仓库根目录。
6. 编译命令：`latexmk -pdf main.tex`。提交前确认 `main.pdf` 能重新
   生成，且没有未定义的引用。
7. `main.pdf` 是模板市场的封面预览，保留在仓库中；中间文件已被
   `.gitignore` 忽略。

## 内容要求

- 标题、作者、单位、摘要、关键词、正文、图表和参考文献均为示例，
  写作时必须全部替换。
- 不要虚构基金号、伦理批号、利益冲突声明或数据可用性声明。
- 投稿前核对期刊最新的 Guide for Authors（见上方链接）。
"""


def journal_meta(journal: dict, meta: dict) -> dict:
    return {
        "name": journal["name"],
        "title": journal["title"],
        "slug": journal["slug"],
        "level": journal["level"],
        "sheet": journal["sheet"],
        "issn": journal.get("issn", ""),
        "publisher": journal["publisher"],
        "template": journal["template"],
        "template_name": meta["name"],
        "template_version": meta["version"],
        "template_source": meta["source"],
        "guidelines": meta["guidelines"],
        "license": meta["license"],
        "entry": "main.tex",
        "output": "main.pdf",
    }


def copy_assets(dest: Path, meta: dict, journal: dict) -> None:
    if meta["files"] is None:
        src_dir = ASSETS / journal["template"]
        for src in src_dir.iterdir():
            if src.is_file():
                shutil.copy2(src, dest / src.name)
        return
    for filename in meta["files"]:
        src = ASSETS / journal["template"] / filename
        if not src.exists():
            raise FileNotFoundError(f"missing asset: {src}")
        shutil.copy2(src, dest / filename)


def write_if_changed(path: Path, content: str) -> None:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return
    path.write_text(content, encoding="utf-8")


def build_journal(journal: dict) -> Path:
    meta = template_info(journal)
    dest = JOURNALS_DIR / journal["slug"]
    dest.mkdir(parents=True, exist_ok=True)

    copy_assets(dest, meta, journal)
    (dest / "figures").mkdir(exist_ok=True)
    shutil.copy2(ASSETS / "example-figure.pdf", dest / "figures" / "example-figure.pdf")

    write_if_changed(dest / "main.tex", BUILDERS[journal["template"]](journal, meta))
    write_if_changed(dest / "references.bib", REFERENCES_BIB)
    write_if_changed(dest / ".latexmkrc", LATEXMKRC)
    write_if_changed(dest / ".gitignore", GITIGNORE)
    write_if_changed(dest / "README.md", journal_readme(journal, meta))
    write_if_changed(dest / "AGENTS.md", journal_agents(journal, meta))
    write_if_changed(dest / "meta.json", json.dumps(journal_meta(journal, meta), ensure_ascii=False, indent=2) + "\n")
    return dest


def write_catalog(data: dict) -> None:
    CATALOG_DIR.mkdir(exist_ok=True)
    journals = data["journals"]

    fields = ["name", "title", "slug", "level", "sheet", "publisher", "issn", "status", "template", "reason"]
    for filename, rows in [
        ("journals.csv", journals),
        ("included.csv", [j for j in journals if j["status"] == "included"]),
        ("skipped.csv", [j for j in journals if j["status"] != "included"]),
    ]:
        with (CATALOG_DIR / filename).open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)

    map_fields = [
        "name", "title", "level", "sheet", "publisher", "issn", "slug",
        "template", "template_name", "template_version", "template_source",
        "guidelines", "license", "entry", "output",
    ]
    map_rows = []
    for journal in journals:
        if journal["status"] != "included":
            continue
        meta = template_info(journal)
        map_rows.append({
            "name": journal["name"],
            "title": journal["title"],
            "level": journal["level"],
            "sheet": journal["sheet"],
            "publisher": journal["publisher"],
            "issn": journal.get("issn", ""),
            "slug": journal["slug"],
            "template": journal["template"],
            "template_name": meta["name"],
            "template_version": meta["version"],
            "template_source": meta["source"],
            "guidelines": meta["guidelines"],
            "license": meta["license"],
            "entry": f"journals/{journal['slug']}/main.tex",
            "output": f"journals/{journal['slug']}/main.pdf",
        })
    with (CATALOG_DIR / "template-map.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=map_fields)
        writer.writeheader()
        writer.writerows(map_rows)

    stats = {
        "source": data["source"],
        "included": len([j for j in journals if j["status"] == "included"]),
        "skipped": len([j for j in journals if j["status"] != "included"]),
    }
    (CATALOG_DIR / "stats.json").write_text(
        json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--compile", action="store_true", help="compile every generated main.tex")
    args = parser.parse_args()

    data = json.loads((CATALOG_DIR / "journals.json").read_text(encoding="utf-8"))
    for journal in data["journals"]:
        if journal["title"] in EXTRA_TITLE_OVERRIDES:
            journal["title"] = EXTRA_TITLE_OVERRIDES[journal["title"]]

    included = [j for j in data["journals"] if j["status"] == "included"]
    for journal in included:
        build_journal(journal)
    write_catalog(data)
    print(f"generated {len(included)} journal directories")

    if args.compile:
        failures = []
        for journal in included:
            dest = JOURNALS_DIR / journal["slug"]
            result = subprocess.run(
                ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
                cwd=dest,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            pdf = dest / "main.pdf"
            if result.returncode != 0 or not pdf.exists():
                failures.append(journal["slug"])
                print(f"FAIL {journal['slug']}", file=sys.stderr)
            else:
                print(f"ok   {journal['slug']}")
        if failures:
            print(f"{len(failures)} failures: {failures}", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
