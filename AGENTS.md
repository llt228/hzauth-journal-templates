# AGENTS.md — hzauth-journal-templates

面向 AI 编码/写作助手的仓库约定。语言：中文。

## 1. 仓库用途

本仓库是 [心河 Paper](https://github.com/forsisi) 模板市场的配套模板库：按《华中农业大学期刊分级目录（试行）》的 A+/A 期刊名单，为每个期刊提供一份**使用出版商官方文档类**的 LaTeX 投稿模板。

核心原则：

1. **官方优先**：只使用出版商发布、许可证允许再分发的 `.cls` / `.bst` / `.sty`。
2. **不编造版式**：找不到公开官方模板的期刊不建目录，不用别的模板冒充。
3. **示例内容必须替换**：`main.tex` 里的作者、单位、摘要、图表、文献都是占位内容。
4. **官方文件只读**：`journals/*/` 下的 `.cls`、`.sty`、`.bst`、`.cfg` 必须与 `assets/` 中的原件逐字节一致。

## 2. 目录结构

```text
.
├── journals/<slug>/          # 每个期刊一个自包含目录（已提交 main.pdf）
├── assets/                   # 官方文档类原件，按模板名分组
├── catalog/
│   ├── journals.json         # 全量 214 刊 + 收录状态（生成的唯一数据源）
│   ├── journals.csv          # 同上，便于查阅
│   ├── all_journals.csv      # 原始表全部 1634 条（含 B/C 级）
│   ├── included.csv          # 已收录 59 刊
│   ├── skipped.csv           # 未收录 155 刊及原因
│   ├── template-map.csv      # 59 刊 → 模板/来源/版本/许可证/入口文件
│   ├── sources.md            # 各出版商官方模板检索记录
│   └── stats.json            # 统计数字
├── scripts/
│   ├── build.py              # 从 catalog/journals.json 生成 journals/*
│   ├── compile_all.sh        # 批量编译
│   └── verify.py             # 目录完整性与 PDF 校验
├── README.md                 # 仓库说明
├── THIRD_PARTY_NOTICES.md    # 第三方文档类来源与许可证
└── LICENSE                   # 本仓库原创内容的 MIT 许可证
```

## 3. 写作与修改约定

- **只改内容文件**：`main.tex`、`references.bib`、`figures/`。
- **不要改官方文件**：`*.cls`、`*.sty`、`*.bst`、`*.cfg`。它们有独立版权和许可证。
- **不要用 `geometry` / `titlesec` / `fontspec` 等宏包私自改版式**；版式由官方文档类决定。
- **参考文献用 BibTeX**：写在 `references.bib`，不要手写 `thebibliography`。
- **图片放 `figures/`**，用相对路径 `figures/xxx` 引用。
- **不虚构**：基金号、伦理批号、利益冲突声明、数据可用性声明必须来自作者真实信息。
- **中文写作**默认使用中文；英文期刊的正文语言按目标期刊要求。

## 4. 构建

单刊：

```bash
cd journals/<slug>
latexmk -pdf main.tex
```

全量：

```bash
bash scripts/compile_all.sh
python3 scripts/verify.py
```

要求 TeX Live 2023+（`pdflatex`、BibTeX、`latexmk`）。每个期刊目录自带官方文档类，正常 TeX Live 环境下无需额外安装。

> 本仓库在受限沙箱中生成时，需要把 `TEXMFVAR` 指向可写目录（例如
> `TEXMFVAR=$PWD/.texmf-var`），否则缺失的 EC/TS1 位图字体无法生成。该目录已在
> 根 `.gitignore` 中忽略。

## 5. 新增期刊

1. 确认该刊的出版商提供了**公开可下载、许可证允许再分发**的官方 LaTeX 文档类；记录来源 URL、版本、许可证。
2. 把官方文件放入 `assets/<template>/`，在 `scripts/build.py` 的 `TEMPLATE_META` 中登记。
3. 在 `catalog/journals.json` 中把该刊 `status` 改为 `included`，填写 `template`（必要时补 `achemso_code`）。
4. 运行 `python3 scripts/build.py` 生成目录；检查 `main.tex` 的期刊名与文档类选项。
5. 运行 `bash scripts/compile_all.sh`，确认 `main.pdf` 成功生成。
6. 更新根 `README.md` 的统计与表格（或重新生成）。

不接受：

- 照着期刊 PDF 手工仿制的版式；
- 修改官方 `.cls` 后提交；
- 没有官方来源、只写“参考某模板”的目录。

## 6. 数据来源

- 原始表：《华中农业大学期刊分级目录（试行）.xlsx》，自然科学类 1177 条 + 人文社科类 457 条，共 1634 条。
- A+/A：228 条记录，按刊名去重后 214 个期刊（A+ 5、A 209）。
- 出版商：Crossref 元数据匹配 + 人工校正；中文期刊不在 Crossref 覆盖范围内。
- 收录状态与原因：见 `catalog/journals.csv`、`catalog/skipped.csv`。

## 7. 提交前检查

- `git status` 中不应出现 `.aux`、`.log`、`.bbl`、`.blg`、`.fls`、`.fdb_latexmk` 等中间文件。
- `main.pdf` 应保留（模板市场封面预览）。
- 新增/修改的 `main.tex` 必须能通过 `latexmk -pdf`。
- 官方文件与 `assets/` 中的原件保持一致（`cmp` 或 `sha256sum` 校验）。
