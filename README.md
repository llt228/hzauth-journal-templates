# 华中农业大学期刊分级目录 · A+/A 期刊 LaTeX 模板

[心河 Paper](https://github.com/forsisi) 模板市场的配套仓库：按《华中农业大学期刊分级目录（试行）》的期刊名单，为每个期刊建立**独立、可编译**的 LaTeX 投稿模板目录。

模板使用期刊出版商发布的官方文档类（`.cls` / `.bst`），本仓库不自行仿制或重排期刊版式。

## 数据来源与数量

| 项目 | 数量 |
| --- | ---: |
| 原始表记录（自然科学类 + 人文社科类） | 1634 |
| A+ / A 记录（含跨表重复） | 228 |
| A+ / A 去重后期刊 | **214** |
| 其中 A+ | 5 |
| 其中 A | 209 |
| 本仓库已建立模板 | **59** |
| 未建立模板（见 `catalog/skipped.csv`） | 155 |

原始文件：`华中农业大学期刊分级目录（试行）.xlsx`（自然科学类 1177 条，人文社科类 457 条）。同一期刊可能同时出现在两个表中（如 *Cell*、*Nature*、*Science*），本仓库按刊名去重。

## 收录原则

1. **只收录官方文档类。** 必须能从公开渠道获得出版商发布的 `.cls` / `.bst` 文件，且许可证允许再分发。
2. **不编造版式。** 找不到公开、可再分发的官方模板时，不为该刊建立目录，也不拿别的模板冒充。
3. **出版商级模板 ≠ 期刊印刷版式。** Elsevier、ACS、OUP、IEEE、APS 使用的是出版商统一的投稿文档类；正式排版由编辑部完成。
4. **示例内容不是论文。** 每个 `main.tex` 的标题、作者、摘要、图表和文献都是占位示例，使用时必须替换。

## 已收录期刊

### Elsevier — `elsarticle`（45 刊）

| 期刊 | 分级 | 出版商 | 目录 |
| --- | --- | --- | --- |
| Cell | A+ | Elsevier | [`cell`](journals/cell/) |
| Advanced Drug Delivery Reviews | A | Elsevier | [`advanced-drug-delivery-reviews`](journals/advanced-drug-delivery-reviews/) |
| Applied Catalysis B: Environmental | A | Elsevier | [`applied-catalysis-b-environmental`](journals/applied-catalysis-b-environmental/) |
| Cancer Cell | A | Elsevier | [`cancer-cell`](journals/cancer-cell/) |
| Cell Host & Microbe | A | Elsevier | [`cell-host-and-microbe`](journals/cell-host-and-microbe/) |
| Cell Metabolism | A | Elsevier | [`cell-metabolism`](journals/cell-metabolism/) |
| Cell Stem Cell | A | Elsevier | [`cell-stem-cell`](journals/cell-stem-cell/) |
| Chem | A | Elsevier | [`chem`](journals/chem/) |
| Clinical Psychology Review | A | Elsevier | [`clinical-psychology-review`](journals/clinical-psychology-review/) |
| Developmental Review | A | Elsevier | [`developmental-review`](journals/developmental-review/) |
| Educational Research Review | A | Elsevier | [`educational-research-review`](journals/educational-research-review/) |
| Energy Storage Materials | A | Elsevier | [`energy-storage-materials`](journals/energy-storage-materials/) |
| European Urology | A | Elsevier | [`european-urology`](journals/european-urology/) |
| Gastroenterology | A | Elsevier | [`gastroenterology`](journals/gastroenterology/) |
| Global Environmental Change-Human and Policy Dimensions | A | Elsevier | [`global-environmental-change-human-and-policy-dimensions`](journals/global-environmental-change-human-and-policy-dimensions/) |
| Immunity | A | Elsevier | [`immunity`](journals/immunity/) |
| Joule | A | Elsevier | [`joule`](journals/joule/) |
| Journal of Business Venturing | A | Elsevier | [`journal-of-business-venturing`](journals/journal-of-business-venturing/) |
| Journal of Hepatology | A | Elsevier | [`journal-of-hepatology`](journals/journal-of-hepatology/) |
| Journal of the American College of Cardiology | A | Elsevier | [`journal-of-the-american-college-of-cardiology`](journals/journal-of-the-american-college-of-cardiology/) |
| Materials Science & Engineering R-Reports | A | Elsevier | [`materials-science-and-engineering-r-reports`](journals/materials-science-and-engineering-r-reports/) |
| Materials Today | A | Elsevier | [`materials-today`](journals/materials-today/) |
| Molecular Cell | A | Elsevier | [`molecular-cell`](journals/molecular-cell/) |
| Nano Energy | A | Elsevier | [`nano-energy`](journals/nano-energy/) |
| Nano Today | A | Elsevier | [`nano-today`](journals/nano-today/) |
| Neuron | A | Elsevier | [`neuron`](journals/neuron/) |
| Pharmacological Reviews | A | Elsevier | [`pharmacological-reviews`](journals/pharmacological-reviews/) |
| Physics Reports-Review Section of Physics Letters | A | Elsevier | [`physics-reports-review-section-of-physics-letters`](journals/physics-reports-review-section-of-physics-letters/) |
| Progress in Energy and Combustion Science | A | Elsevier | [`progress-in-energy-and-combustion-science`](journals/progress-in-energy-and-combustion-science/) |
| Progress in Materials Science | A | Elsevier | [`progress-in-materials-science`](journals/progress-in-materials-science/) |
| Progress in Polymer Science | A | Elsevier | [`progress-in-polymer-science`](journals/progress-in-polymer-science/) |
| The Lancet | A | Elsevier | [`lancet`](journals/lancet/) |
| The Lancet Diabetes & Endocrinology | A | Elsevier | [`lancet-diabetes-and-endocrinology`](journals/lancet-diabetes-and-endocrinology/) |
| The Lancet Global Health | A | Elsevier | [`lancet-global-health`](journals/lancet-global-health/) |
| The Lancet Infectious Diseases | A | Elsevier | [`lancet-infectious-diseases`](journals/lancet-infectious-diseases/) |
| The Lancet Neurology | A | Elsevier | [`lancet-neurology`](journals/lancet-neurology/) |
| The Lancet Oncology | A | Elsevier | [`lancet-oncology`](journals/lancet-oncology/) |
| The Lancet Psychiatry | A | Elsevier | [`lancet-psychiatry`](journals/lancet-psychiatry/) |
| The Lancet Public Health | A | Elsevier | [`lancet-public-health`](journals/lancet-public-health/) |
| The Lancet Respiratory Medicine | A | Elsevier | [`lancet-respiratory-medicine`](journals/lancet-respiratory-medicine/) |
| Trends in Biochemical Sciences | A | Elsevier | [`trends-in-biochemical-sciences`](journals/trends-in-biochemical-sciences/) |
| Trends in Biotechnology | A | Elsevier | [`trends-in-biotechnology`](journals/trends-in-biotechnology/) |
| Trends in Cell Biology | A | Elsevier | [`trends-in-cell-biology`](journals/trends-in-cell-biology/) |
| Trends in Cognitive Sciences | A | Elsevier | [`trends-in-cognitive-sciences`](journals/trends-in-cognitive-sciences/) |
| Trends in Ecology & Evolution | A | Elsevier | [`trends-in-ecology-and-evolution`](journals/trends-in-ecology-and-evolution/) |

### American Chemical Society — `achemso`（5 刊）

| 期刊 | 分级 | 出版商 | 目录 |
| --- | --- | --- | --- |
| Accounts of Chemical Research | A | American Chemical Society (ACS) | [`accounts-of-chemical-research`](journals/accounts-of-chemical-research/) |
| ACS Energy Letters | A | American Chemical Society (ACS) | [`acs-energy-letters`](journals/acs-energy-letters/) |
| ACS Nano | A | American Chemical Society (ACS) | [`acs-nano`](journals/acs-nano/) |
| Chemical Reviews | A | American Chemical Society (ACS) | [`chemical-reviews`](journals/chemical-reviews/) |
| Journal of the American Chemical Society | A | American Chemical Society (ACS) | [`journal-of-the-american-chemical-society`](journals/journal-of-the-american-chemical-society/) |

### Oxford University Press — `oup-authoring-template`（5 刊）

| 期刊 | 分级 | 出版商 | 目录 |
| --- | --- | --- | --- |
| American Journal of Respiratory and Critical Care Medicine | A | Oxford University Press (OUP) | [`american-journal-of-respiratory-and-critical-care-medicine`](journals/american-journal-of-respiratory-and-critical-care-medicine/) |
| European Heart Journal | A | Oxford University Press (OUP) | [`european-heart-journal`](journals/european-heart-journal/) |
| National Science Review | A | Oxford University Press (OUP) | [`national-science-review`](journals/national-science-review/) |
| Quarterly Journal of Economics | A | Oxford University Press (OUP) | [`quarterly-journal-of-economics`](journals/quarterly-journal-of-economics/) |
| Schizophrenia Bulletin | A | Oxford University Press (OUP) | [`schizophrenia-bulletin`](journals/schizophrenia-bulletin/) |

### IEEE — `IEEEtran`（3 刊）

| 期刊 | 分级 | 出版商 | 目录 |
| --- | --- | --- | --- |
| IEEE Communications Surveys & Tutorials | A | IEEE | [`ieee-communications-surveys-and-tutorials`](journals/ieee-communications-surveys-and-tutorials/) |
| IEEE Industrial Electronics Magazine | A | IEEE | [`ieee-industrial-electronics-magazine`](journals/ieee-industrial-electronics-magazine/) |
| IEEE Transactions on Pattern Analysis and Machine Intelligence | A | IEEE | [`ieee-transactions-on-pattern-analysis-and-machine-intelligence`](journals/ieee-transactions-on-pattern-analysis-and-machine-intelligence/) |

### American Physical Society — REVTeX 4.2（1 刊）

| 期刊 | 分级 | 出版商 | 目录 |
| --- | --- | --- | --- |
| Reviews of Modern Physics | A | American Physical Society (APS) | [`reviews-of-modern-physics`](journals/reviews-of-modern-physics/) |

## 目录结构

每个期刊目录都是自包含的，结构与模板市场约定一致：

```text
journals/cell/
├── main.tex                 # 论文入口：标题/作者/摘要/正文/参考文献
├── main.pdf                 # 编译产物，供模板市场封面预览
├── elsarticle.cls           # 出版商官方文档类（未修改）
├── elsarticle-num.bst       # 官方参考文献样式（未修改）
├── references.bib           # 示例 BibTeX 文献库
├── figures/
│   └── example-figure.pdf   # 示例矢量图
├── .latexmkrc               # latexmk 构建配置
├── .gitignore               # 忽略中间文件，保留 main.pdf
├── AGENTS.md                # 供 AI 写作助手阅读的目录约定
├── README.md                # 本刊模板说明与官方来源
└── meta.json                # 结构化元数据（分级、ISSN、模板来源等）
```

仓库根目录另有 `assets/`（官方文档类原件）、`catalog/`（214 刊全量目录与收录状态）和 `scripts/`（生成、编译、校验脚本）。

## 使用方法

```bash
git clone https://github.com/llt228/hzauth-journal-templates.git
cd hzauth-journal-templates/journals/cell
latexmk -pdf main.tex
```

要求 TeX Live 2023 或更新版本，包含 `pdflatex`、BibTeX 与 `latexmk`。每个目录已自带官方文档类，无需另行安装。

批量编译全部模板：

```bash
bash scripts/compile_all.sh          # 默认并行 4 个
JOBS=8 bash scripts/compile_all.sh   # 指定并行度
python3 scripts/verify.py            # 校验目录完整性与 PDF 产物
```

## 为什么没有 Nature、Science 等期刊

这是有意为之，不是遗漏：

- **Nature**：Nature Portfolio 的格式指南明确以 Microsoft Word 为 preferred format，并说明 LaTeX 稿件接收后需转换为 Word 排版；未提供官方 LaTeX 文档类。
- **Science / AAAS**：未检索到可公开获取、允许再分发的官方 LaTeX 文档类。
- **《求是》《中国社会科学》等中文期刊**：未检索到公开的官方 LaTeX 模板。
- **Springer Nature、Wiley、SAGE、Taylor & Francis 等**：官方模板通常通过 Overleaf 或出版社投稿系统分发，未能获得可再分发的文件，因此未收录；这不代表这些期刊不接受 LaTeX 投稿。

各出版商的核对记录见 [`catalog/sources.md`](catalog/sources.md)。全量 214 刊的出版商、ISSN、收录状态与原因见 [`catalog/journals.csv`](catalog/journals.csv)，未收录清单见 [`catalog/skipped.csv`](catalog/skipped.csv)。原始表的全部 1634 条记录（含 B/C 级）见 [`catalog/all_journals.csv`](catalog/all_journals.csv)。

## 未收录清单（按出版商）

| 出版商 | 未收录数 |
| --- | ---: |
| Springer Nature | 50 |
| Annual Reviews | 20 |
| Wiley | 13 |
| 中文期刊 | 11 |
| SAGE Publications | 10 |
| Academy of Management | 4 |
| Taylor & Francis (Informa) | 4 |
| American Psychological Association (APA) | 4 |
| American Medical Association (AMA) | 4 |
| AAAS | 3 |
| JSTOR | 2 |
| Royal Society of Chemistry (RSC) | 2 |
| Wolters Kluwer | 2 |
| American Society for Microbiology | 2 |
| American Economic Association | 2 |
| Elsevier（丛书，未建目录） | 1 |
| Optica Publishing Group | 1 |
| American Psychiatric Association Publishing | 1 |
| American College of Physicians | 1 |
| AIP Publishing | 1 |

> 出版商归属由 Crossref 元数据匹配后人工校正；中文期刊与跨表重复项单独处理。未收录原因是“未获得可公开再分发的官方文档类”，不等于该刊不接受 LaTeX。

## 模板来源与许可证

| 文档类 | 版本 | 版权方 | 许可证 | 来源 |
| --- | --- | --- | --- | --- |
| `elsarticle` | 3.4（2024/04/04） | Elsevier | LPPL 1.3 | <https://ctan.org/pkg/elsarticle> |
| `achemso` | 3.13g（2024-01-30） | American Chemical Society | LPPL 1.3 | <https://ctan.org/pkg/achemso> |
| `oup-authoring-template` | 1.5（2026/07/14） | Oxford University Press | LPPL 1.3 | <https://ctan.org/pkg/oup-authoring-template> |
| `IEEEtran` | 1.8b（2015/08/26） | IEEE | LPPL 1.3 | <https://ctan.org/pkg/ieeetran> |
| `revtex4-2` | 4.2f（2022/06/05） | American Physical Society | LPPL 1.3 | <https://ctan.org/pkg/revtex> |

文档类文件均**逐字节未修改**，版权与许可证归原权利人所有；详见 [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md)。本仓库原创的模板骨架、脚本与文档以 MIT 许可证发布，见 [`LICENSE`](LICENSE)。

## 免责声明

- 本仓库是投稿排版模板，不是期刊官方投稿系统，也不代表期刊编辑部的最终版式。
- 投稿前请核对期刊最新的 Guide for Authors；文章类型、字数、图表数量和参考文献格式可能变化。
- 示例文献、作者、单位、基金号、伦理声明等均为占位内容，请勿直接提交。
- 若期刊更新官方模板，以出版商发布的最新版本为准。

## 贡献

新增期刊请同时提供：官方文档类的公开下载地址、版本号、许可证，以及该刊使用该模板的依据（投稿指南链接）。然后：

1. 把官方文件放入 `assets/<template>/`；
2. 在 `catalog/journals.json` 中把该刊 `status` 改为 `included` 并填写 `template`；
3. 运行 `python3 scripts/build.py` 生成目录，运行 `bash scripts/compile_all.sh` 验证 PDF。

不接受“照着期刊 PDF 仿制”的模板，也不接受修改官方 `.cls` 后提交。
