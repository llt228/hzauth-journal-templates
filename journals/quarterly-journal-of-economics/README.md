# Quarterly Journal of Economics

华中农业大学期刊分级目录：**A**（人文社科类）。

| 项目 | 内容 |
| --- | --- |
| 目录中的期刊名 | Quarterly Journal of Economics |
| 出版商 | Oxford University Press (OUP) |
| 官方文档类 | Oxford University Press authoring template `oup-authoring-template` |
| 文档类版本 | 1.5 (2026/07/14) |
| 文档类来源 | <https://ctan.org/pkg/oup-authoring-template> |
| 投稿指南 | <https://academic.oup.com/pages/authoring/journals> |
| 文档类许可证 | LPPL 1.3 |

## 编译

```bash
latexmk -pdf main.tex
```

默认使用 `pdflatex` + BibTeX，产物为 `main.pdf`。本目录自带官方
`.cls` / `.sty` / `.bst` 文件，无需额外安装（TeX Live 2023 或更新版本）。

## 文件说明

- `main.tex`：论文入口，模板示例内容都在这里，替换为你的稿件。
- `main.pdf`：编译产物，供模板市场预览。
- `oup-authoring-template.cls` 等：出版商官方文档类及其依赖，**请勿修改**。
- `references.bib`：示例文献库，请替换为真实文献。
- `figures/example-figure.pdf`：示例矢量图，替换为你的图片。
- `.latexmkrc`：latexmk 构建配置。
- `AGENTS.md`：供 AI 写作助手阅读的本目录约定。

## 说明

本模板的版式完全由出版商官方文档类决定；示例正文、作者、单位和
文献均为占位内容，不是真实论文。投稿前请以期刊最新的 Guide for
Authors 为准。
