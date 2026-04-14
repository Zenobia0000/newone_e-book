# M0 — 開場：Python 與 AI 系統全景

本目錄採 SOP 對齊結構（見 `shared/design_system/投影片生成_SOP_Agent工作流.md` §3），
但目前處於**過渡階段**：部分 agent-produced 檔案尚未自動化，由現有手寫實作代替。

## 檔案對照

| SOP 檔名 | 本目錄狀態 | 說明 |
|---------|----------|------|
| `00_skeleton.yaml` | ✅ 在此 | 人類 H-1 契約輸入；pipeline 唯一真實來源 |
| `01_outline.md` | ⬜ 未建 | 選填；若 M0 有特殊教學需求可補 |
| `02_slides_design.md` | ✅ 在此 | 審閱用全稿；即舊 `slides_consult_pilot.md` |
| `03_layout_spec.json` | ⬜ 未建 | Agent-B 未實作；目前由 `../../slides_build/slides/m0_deck.py` 代替（人類直接用 Python 呼叫 primitives） |
| `04_image_placeholders.yaml` | ✅ 在此 | 3 個 pending；H-2 補真圖後更新 status |
| `05_mvk.md` | ✅ 在此 | 30 分鐘 MVK 速學卡 13 張 |
| `06_review_prose.md` | ⬜ 未建 | 選填；Agent-A 尚未自動產 |
| `07_build_manifest.json` | ⬜ 未建 | Agent-D 未產；過渡期由 `../../slides_build/output/_image_placeholders_M0.yaml` 提供部分 audit |
| `08_qa_report.md` | ⬜ 未建 | Agent-E 未實作；目前由 `../../slides_build/tests/test_m0.py` 跑 25 項檢查代替 |
| `09_change_log.md` | ⬜ 未建 | 尚無多 agent 接力；暫以 git commit history 代替 |
| `assets/` | ⬜ 未建 | H-2 補真圖時才建；依 `04_image_placeholders.yaml` 清單 |

## 如何重建 .pptx

```bash
cd books/python-data-ai-foundations
python -m slides_build.build --module M0
```

產出路徑：`slides_build/output/M0_開場_Python與AI系統全景.pptx`

## 如何跑穩固性測試

```bash
cd books/python-data-ai-foundations
python -m slides_build.tests.test_m0
```

25 項自動檢查，含 schema / build / structure / 視覺紀律 / 內容一致性 / 佔位符 / PDF 渲染。

## 過渡到完整 pipeline

當 Agent-B / D / E 實作完成後：

1. `m0_deck.py` 退役，由 Agent-B 從 `02_slides_design.md` 自動產 `03_layout_spec.json`
2. Agent-D 從 `03` 讀 layout 呼叫 primitives，產 `.pptx` + `07_build_manifest.json`
3. `test_m0.py` 的邏輯併入 Agent-E，產 `08_qa_report.md`
4. 每次 agent 動作追加一行到 `09_change_log.md`

詳見 SOP §5 流水線。
