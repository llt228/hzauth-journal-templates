# AGENTS.md — The Lancet Public Health

本目录是《华中农业大学期刊分级目录（试行）》中 **A**
期刊 *The Lancet Public Health* 的 LaTeX 投稿模板。面向 AI 编码/写作助手。

## 权威来源

- 官方文档类：Elsevier elsarticle `elsarticle`（3.4 (2024/04/04)）
- 来源：https://ctan.org/pkg/elsarticle
- 投稿指南：https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions
- 许可证：LPPL 1.3

## 写作约定

1. 只编辑 `main.tex`、`references.bib` 和 `figures/` 下的文件。
2. **不要修改** `elsarticle.cls`、`.sty`、`.bst` 等官方文件；它们
   必须与出版商发布的版本逐字节一致。
3. 正文使用文档类提供的命令，不要用 `geometry`、`titlesec` 等宏包
   私自改动页面尺寸、字体或章节格式。
4. 文献放在 `references.bib`，用 BibTeX 生成；不要手写
   `thebibliography` 环境。
5. 图片放 `figures/`，用 `\includegraphics` 引用；不要把图片放到
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
