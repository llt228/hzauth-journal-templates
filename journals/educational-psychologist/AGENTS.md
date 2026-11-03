# AGENTS.md — Educational Psychologist

本目录是 *Educational Psychologist* 的 LaTeX 投稿模板，由 Taylor & Francis 官方 Word 模板转换。

- 官方 Word 模板：`TF_Template_Word_Windows_2016.dotx`
- 来源：https://authorservices.taylorandfrancis.com/publishing-your-research/writing-your-paper/formatting-and-templates/
- LaTeX 文档类：`tandf.cls`（按官方 docx 的 A4 页面、上下 2.5 cm / 左右 3 cm 页边距、Times 12 pt 双倍行距、14 pt 标题、11 pt 摘要和标题层级重建）
- 编译：`latexmk -pdf main.tex`

## 约定

- `tandf.cls` 是官方 Word 模板的 LaTeX 重建，不是 Taylor & Francis 发布的 LaTeX 类；不要把它当成期刊最终排版。
- 正文、作者、摘要、关键词均为官方 Word 模板中的占位示例，写作时全部替换。
- 参考文献样式暂用 `plainnat`，投稿前按目标刊的 Guide for Authors 替换。
- 图片放 `figures/`，文献放 `references.bib`。
- `plainnat.bst` 来自 natbib（LPPL），仅作占位文献样式；投稿前按目标刊要求替换。
- `main.pdf` 是编译产物，保留供预览。
