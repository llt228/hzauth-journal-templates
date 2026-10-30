# 图目录是怎么来的

本目录记录《华中农业大学期刊分级目录（试行）》的解析结果，以及 A+/A 期刊模板的收录判断。

## 1. 原始数据

源文件：`华中农业大学期刊分级目录（试行）.xlsx`（52.6 MB）。

工作簿包含两个工作表：

| 工作表 | 表头行 | 数据行 | 记录数 |
| --- | --- | --- | ---: |
| 自然科学类 | 第 2 行（序号 / 期刊名称 / 级别 / 2022） | 第 3–1179 行 | 1177 |
| 人文社科类 | 第 2 行（序号 / 期刊名称 / 级别） | 第 3–459 行 | 457 |

合计 **1634** 条。`sheet1.xml` 解压后约 420 MB，其中绝大部分是带格式的空单元格，解析时使用 OOXML 流式读取，仅保留非空单元格。

## 2. A+/A 清单

- 级别分布（记录数）：自然科学类 A+ 3、A 154、B 217、C 803；人文社科类 A+ 5、A 66、B 88、C 298。
- A+/A 共 **228 条记录**。
- 跨表重复 74 个刊名（如 *Cell*、*Nature*、*Science*），同一表内重复 1 条；按刊名小写去重后为 **214 个期刊**（A+ 5、A 209）。

## 3. 出版商判定

对 214 个刊名逐个查询 Crossref：

```text
GET https://api.crossref.org/works?query.container-title=<刊名>&rows=20
```

- 先做 HTML 实体反转义（`&amp;` → `&`），再按规范化标题（小写、`&` → `and`、去掉标点）做相似度匹配。
- 相似度 ≥ 0.97 视为精确匹配；0.90–0.97 视为模糊匹配并人工抽查；其余保留空值。
- 167 个精确匹配、12 个模糊匹配、35 个未匹配。未匹配项中，*Cell*、*Nature*、*Science*、Lancet 系列、部分中文期刊等通过人工核对补全；中文期刊不在 Crossref 覆盖范围内，单独标记。
- 出版商字段反映 Crossref 的 `publisher` 元数据，可能与期刊实际出版学会/机构不同（例如学会期刊由大学出版社托管）。本仓库只把它作为“模板归属”的依据，不把它当作期刊版权归属。

## 4. 收录判定

只有同时满足以下条件的期刊才建立目录：

1. 出版商或维护者公开发布了官方 LaTeX 文档类；
2. 该文档类的许可证允许再分发（本仓库收录的五种均为 LPPL 1.3）；
3. 能在公开渠道获得可核验的 `.cls` / `.bst` 文件。

本仓库使用的五种官方文档类：

| 模板键 | 文档类 | 覆盖出版商 | 收录刊数 |
| --- | --- | --- | ---: |
| `elsarticle` | Elsevier elsarticle | Elsevier（含 Cell Press、Lancet 系列） | 45 |
| `achemso` | ACS achemso | American Chemical Society | 5 |
| `oup` | oup-authoring-template | Oxford University Press | 5 |
| `ieeetran` | IEEEtran | IEEE | 3 |
| `revtex` | REVTeX 4.2 | American Physical Society | 1 |

以下情况**不建立目录**：

- 出版商没有公开的官方 LaTeX 文档类（Nature Portfolio 明确以 Word 为 preferred format；Science/AAAS、AMA、APA、Annual Reviews、中文期刊等未检索到公开模板）；
- 官方模板只通过 Overleaf、投稿系统或出版社登录分发，无法获得可再分发的文件（Springer Nature、Wiley、SAGE、Taylor & Francis 等）；
- 条目是丛书而非期刊（*Advances in Experimental Social Psychology*）。

## 5. 字段说明

`journals.csv` / `journals.json`：

| 字段 | 说明 |
| --- | --- |
| `name` | Excel 中的期刊名（去首尾空格） |
| `title` | 用于模板标题的展示名；个别期刊使用官方写法（如 *The Lancet*） |
| `slug` | 目录名，小写、`&` → `and`、非字母数字转连字符 |
| `level` | `A+` 或 `A` |
| `sheet` | `自然科学类` 或 `人文社科类` |
| `publisher` | Crossref 出版商 + 人工校正 |
| `issn` | Crossref ISSN（可能多个，分号分隔；缺失为空） |
| `status` | `included` / `skipped` |
| `template` | 已收录期刊使用的模板键 |
| `reason` | 未收录原因 |

## 6. 检索记录

各出版商的官方模板页面、可获取性与处理决定见 [`sources.md`](sources.md)。

## 7. 已知局限

- Crossref 的出版商字段有时是托管平台而非学会，个刊的投稿指南可能与本仓库使用的出版商统一模板不同；投稿前必须以期刊 Guide for Authors 为准。
- 未逐刊抓取 214 个期刊的投稿页面；“未收录”只表示未获得可公开再分发的官方文档类，不表示该刊不接受 LaTeX。
- 中文期刊的英文名、ISSN 与主办单位未做进一步核对；这些期刊目前均未建立模板。
- 同一刊名在不同年份可能更换出版商（如 FEMS 系列），本仓库以当前 Crossref 记录为准。
