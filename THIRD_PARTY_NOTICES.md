# 第三方文档类与许可证

`journals/*/` 下的 `.cls`、`.sty`、`.bst`、`.cfg` 文件均为出版商或维护者发布的官方文件，**未作任何修改**。这些文件不适用本仓库根目录的 MIT 许可证，而是保留各自的许可证与版权。

| 文档类 | 版本 | 版权方 | 许可证 | 官方来源 |
| --- | --- | --- | --- | --- |
| `elsarticle` | 3.4（2024/04/04） | Elsevier Ltd | LaTeX Project Public License 1.3 | <https://ctan.org/pkg/elsarticle> |
| `achemso` | 3.13g（2024-01-30） | American Chemical Society | LaTeX Project Public License 1.3 | <https://ctan.org/pkg/achemso> |
| `oup-authoring-template` | 1.5（2026/07/14） | Oxford University Press | LaTeX Project Public License 1.3 | <https://ctan.org/pkg/oup-authoring-template> |
| `IEEEtran` | 1.8b（2015/08/26） | IEEE | LaTeX Project Public License 1.3 | <https://ctan.org/pkg/ieeetran> |
| `revtex4-2` | 4.2f（2022/06/05） | American Physical Society | LaTeX Project Public License 1.3 | <https://ctan.org/pkg/revtex> |

## 说明

- LPPL 1.3 允许在保持文件完整、不改变名称的前提下再分发；本仓库未修改上述文件。
- 各期刊目录的 `README.md` 与 `meta.json` 记录了该目录实际使用的文档类、版本与来源。
- `figures/example-figure.pdf` 由本仓库使用 TikZ/pgfplots 生成，属于原创内容，随本仓库以 MIT 许可证发布。
- 本仓库的 `main.tex` 骨架、脚本和文档为原创内容，以 MIT 许可证发布；示例正文与示例文献仅用于演示排版，不应作为真实学术内容引用。

## 官方文件校验

如需核对官方文件是否被改动，可用对应 CTAN 包或出版商模板包中的同名文件做 `cmp` / `sha256sum` 比较。仓库的 `assets/` 目录保存了生成时使用的原件。
