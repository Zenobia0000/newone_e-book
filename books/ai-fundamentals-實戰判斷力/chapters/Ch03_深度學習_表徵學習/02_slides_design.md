# Ch03 — 深度學習：從人工特徵到表徵學習｜Slides Design

> 22 張內容投影片（封面 + 22 + 版權）｜教學型七原型為主
> 對齊 `01_outline.md` 的 6 個 Learning Objectives x 4 個 Common Pitfalls
> 配色：主色 `#1B5E3F` + 錯誤紅 `#C62828`（僅 PITFALL 頁）+ 成功綠 `#2E7D32`

---

## S1 · MOTIVATION — 手工特徵的天花板

- 🖼️ 畫面：全白底 / 大字痛點句 / 右下數據卡（ImageNet 2012 突破）
- 📣 畫面上的字：
  - 標題：「你能手寫的特徵，撐不住了」
  - 副標：ImageNet 2012 · 手工特徵 73% → AlexNet 自動學特徵 85%
- 🎙️ 講者這時說：「上一章我們學了特徵工程——你得先告訴機器看哪些欄位。但如果資料是圖片呢？你要手寫『耳朵尖尖、鬍鬚長長』來辨認貓嗎？2012 年有個團隊說：讓模型自己學。結果準確率從 73% 跳到 85%。這就是深度學習的起點。」

---

## S2 · ASK — 模型怎麼自己長出特徵？

- 🖼️ 畫面：白底，中央大字問句，右下提示卡
- 📣 畫面上的字：
  - 「DL 不需要人先定義特徵——它自己長出來。怎麼做到的？」
  - 卡片提示：「不是魔法，是一套訓練機制」
- 🎙️ 講者這時說：「線索給你們：不是模型天生聰明，也不是資料自帶答案。差別在一套重複的訓練流程——預測、算錯、修正、再來。今天這堂課結束，你會理解這套流程從頭到尾怎麼運作。」

---

## S3 · SILENT — 一句話立論

- 🖼️ 畫面：全綠底 / 白色 HERO 大字置中
- 📣 畫面上的字：「深度學習不是網路結構本身，而是一整條 data → model → optimize → save 的訓練機制。」
- 🎙️ 講者這時說：「這頁只有一句話。如果你今天只記得一件事，就是這個。不要被 CNN、RNN、Transformer 的名詞淹沒——它們只是骨架，訓練機制才是靈魂。」

---

## S4 · CONCEPT-CARD — tensor 的直覺

- 🖼️ 畫面：左欄 scalar → vector → matrix → tensor 堆疊圖 + 右欄 shape/dtype/device 三件套
- 📣 畫面上的字：
  - 標題：「tensor = 有形狀的數字容器」
  - 左：四層堆疊（0D scalar → 1D vector → 2D matrix → 3D+ tensor）
  - 右：`.shape` 形狀 / `.dtype` 精度 / `.device` CPU 或 GPU
- 🎙️ 講者這時說：「tensor 不神秘——你在 Ch02 用的 NumPy ndarray 就是 tensor 的前身。差別是 PyTorch 的 tensor 多了一個能力：它記得自己被怎麼運算過，所以能自動算梯度。shape 告訴你資料長什麼樣，dtype 告訴你精度，device 告訴你它跑在 CPU 還是 GPU 上。」

---

## S5 · EXAMPLE-I/O — 用 PyTorch 建 tensor

- 🖼️ 畫面：三欄 Input | Process | Output
- 📣 畫面上的字：
  - 欄1 Input：`[[1.0, 2.0], [3.0, 4.0]]`（Python list）
  - 欄2 Process：`t = torch.tensor(data)`
  - 欄3 Output：`t.shape → (2,2)` / `t.dtype → float32` / `t.device → cpu`
- 🎙️ 講者這時說：「跟 NumPy 幾乎一樣的 API，但底下多了 autograd 引擎。你現在不需要懂 autograd 怎麼實作，只要知道：PyTorch tensor 會自動幫你記錄運算，等下反向傳播時用得到。」

---

## S6 · CONCEPT-CARD — model / loss / optimizer 三件套

- 🖼️ 畫面：三個圓角方塊橫排 + 各自一句話定義，下方箭頭串連
- 📣 畫面上的字：
  - Model：「負責預測——把 input 變成 output」
  - Loss：「負責評分——算預測跟正確答案差多少」
  - Optimizer：「負責調參——根據梯度更新模型參數」
  - 下方：「三者缺一不可，順序固定」
- 🎙️ 講者這時說：「這三件套是 DL 訓練的基本配備。Model 是你的員工，Loss 是老闆的評分表，Optimizer 是教練——告訴員工怎麼根據評分改進。不管用什麼架構，這三件套都一樣。」

---

## S7 · CHECKPOINT — tensor 與三件套角色

- 🖼️ 畫面：白底 / 標題「Check Point」/ 三題列點
- 📣 畫面上的字：
  - Q1：tensor 的 shape `(3, 224, 224)` 代表什麼？（提示：彩色圖片）
  - Q2：loss 在訓練中扮演什麼角色？
  - Q3：optimizer 需要什麼資訊才能更新參數？
- 🎙️ 講者這時說：「30 秒不看投影片。(3,224,224) 是三個通道、224x224 像素——就是一張彩色圖片。loss 是評分表。optimizer 需要梯度才能知道參數該怎麼調。三題都答得出來我們繼續。」

---

## S8 · MECHANISM-FLOW — 訓練循環五步

- 🖼️ 畫面：五個方塊橫排 + 箭頭 + 最右邊回頭循環箭頭（真圖佔位）
- 📣 畫面上的字：
  - 方塊1「Data Loader」sub：把資料切成 batch
  - 方塊2「Forward」sub：model(x) 產出預測
  - 方塊3「Loss」sub：loss_fn(pred, y) 算誤差
  - 方塊4「Backward」sub：loss.backward() 算梯度
  - 方塊5「Update」sub：optimizer.step() 更新參數
  - 下方：「五步一圈 = 1 個 iteration；所有 batch 跑完 = 1 個 epoch」
- 🎙️ 講者這時說：「這張圖是今天最重要的一張。不管你用 CNN、RNN 還是 Transformer，訓練循環永遠是這五步。PyTorch 官方教學也是這個順序：data → model → optimize → save。把這五步背下來，你就能讀懂任何訓練程式碼。」

---

## S9 · CONCEPT-CARD — gradient / backprop / autograd

- 🖼️ 畫面：三層堆疊，上到下：gradient → backpropagation → autograd
- 📣 畫面上的字：
  - gradient：「方向盤——告訴你每個參數該往哪邊修、修多大」
  - backpropagation：「chain rule 反向傳遞——從 loss 一路回推到每個參數」
  - autograd：「PyTorch 的自動微分引擎——幫你自動算 gradient，不用手寫數學」
  - 下方：「你不需要手推 chain rule，但要知道：autograd 在 forward 時偷偷記錄了所有運算」
- 🎙️ 講者這時說：「gradient 想成方向盤——loss 對每個參數的偏導數，告訴你往哪邊轉。backprop 是沿路回頭算每個路口該轉多少。autograd 是 PyTorch 幫你自動做這件事的引擎。你在寫 loss.backward() 的時候，autograd 已經把所有梯度算好了。」

---

## S10 · PITFALL — learning rate 太大 vs 太小

- 🖼️ 畫面：VS 兩欄，左紅邊「lr = 1.0」右藍邊「lr = 1e-6」，下方一句 why
- 📣 畫面上的字：
  - 左欄：loss 曲線劇烈震盪甚至發散 → 「步伐太大，跨過最低點」
  - 右欄：loss 曲線幾乎平坦 → 「步伐太小，走不到最低點」
  - 下方：「起手式：lr = 1e-3，看 loss curve 再調」
- 🎙️ 講者這時說：「這是新手最常踩的坑。lr 就是每步修正的幅度——太大會在山谷裡彈來彈去，太小會原地踏步。經驗法則：先用 1e-3 當起點，看 loss curve 再決定放大還是縮小。」

---

## S11 · CONCEPT-CARD — batch / epoch / lr 三個旋鈕

- 🖼️ 畫面：三個旋鈕圖示，各附一句解釋
- 📣 畫面上的字：
  - batch_size：「一次看多少筆資料 — 太大記憶體爆、太小梯度不穩」
  - epoch：「整個資料集看幾遍 — 太多 overfit、太少 underfit」
  - learning_rate：「每步修多大 — 太大爆炸、太小停滯」
  - 下方：「三個旋鈕互相牽連——調一個要看另外兩個的反應」
- 🎙️ 講者這時說：「DL 訓練就是轉這三個旋鈕。batch_size 通常 32 或 64 起跳；epoch 看 loss curve 決定什麼時候停；lr 先 1e-3 再微調。記住：不是背公式，是看 loss curve 做決策。」

---

## S12 · EXAMPLE-I/O — 讀懂 loss curve

- 🖼️ 畫面：三張 loss curve 並排（真圖佔位）
- 📣 畫面上的字：
  - 圖1：train_loss 降 + val_loss 降 → 標籤「正常收斂」（綠框）
  - 圖2：train_loss 降 + val_loss 升 → 標籤「Overfitting」（紅框）
  - 圖3：train_loss 平 + val_loss 平 → 標籤「Underfitting / lr 太小」（黃框）
  - 下方：「loss curve 是你的儀表板——不會讀它就等於盲飛」
- 🎙️ 講者這時說：「三張圖記下來。左邊是你想要的——兩條線一起往下。中間是最常見的問題——模型在背答案。右邊是模型根本沒在學。下次訓練完第一件事：畫 loss curve。」

---

## S13 · PITFALL — loss 下降不等於模型在學

- 🖼️ 畫面：VS 兩欄，左紅「只看 train_loss」右綠「同時看 train + val」
- 📣 畫面上的字：
  - 左：「train_loss 0.01 → 好棒！」→ 但 val_loss 1.5 → 「背答案了」（紅色警告）
  - 右：「train 0.15 / val 0.18 → 差距小 = 真的在學」（綠色 check）
  - 下方：「永遠同時畫 train_loss 和 val_loss——兩條線的差距比絕對值更重要」
- 🎙️ 講者這時說：「這是一個心態問題。你看到 loss 降到 0.01 會很開心，但如果 val_loss 同時飆到 1.5，你的模型只是把訓練資料背下來了。判斷標準不是 loss 多低，是 train 和 val 的差距多小。」

---

## S14 · CHECKPOINT — 訓練循環與 loss curve

- 🖼️ 畫面：白底，三題列點
- 📣 畫面上的字：
  - Q1：訓練循環五步的正確順序？
  - Q2：loss curve 出現 val_loss 持續上升代表什麼？你會怎麼做？
  - Q3：lr 太大的 loss curve 長什麼樣？
- 🎙️ 講者這時說：「快問快答。Q1：data → forward → loss → backward → update。Q2：overfitting，可以 early stopping、加 regularization、或增加資料。Q3：loss 劇烈震盪甚至發散。三題都對的話，你已經能當訓練的『偵探』了。」

---

## S15 · CONCEPT-CARD — representation learning 的意義

- 🖼️ 畫面：左右對比（真圖佔位）
- 📣 畫面上的字：
  - 左「傳統 ML」：人設計特徵 → 特徵提取 → 分類器 → 預測
  - 右「深度學習」：原始資料 → [層1 → 層2 → ... → 層N] 自動提取 → 預測
  - 下方：「DL 最核心的價值：不用人先把規則寫死，讓系統自己長出特徵」
- 🎙️ 講者這時說：「這就是為什麼這章叫『表徵學習』。representation = 表徵 = 特徵的另一個說法。傳統 ML 你得自己想好特徵；DL 讓多層神經網路一層一層提煉出越來越抽象的特徵。第一層看邊緣，第二層看紋理，第三層看部件，最後一層看語意。人不用介入。」

---

## S16 · PITFALL — 把 DL 當成選架構名詞套上去

- 🖼️ 畫面：VS 左紅「只選架構」右綠「整體訓練設計」
- 📣 畫面上的字：
  - 左：「用 Transformer！因為很紅！」→ 但資料只有 500 筆、標註品質 60% → 結果爛（紅色 ✗）
  - 右：「先確認資料品質 → 選合適架構 → 調訓練設定 → 讀 loss curve」→ 結果好（綠色 ✓）
  - 下方：「架構只是骨架，data pipeline + 標註品質 + 訓練設定才是成敗關鍵」
- 🎙️ 講者這時說：「我看過太多人第一句話就問『用什麼架構』，但忽略了資料只有 500 筆、標註有 40% 是錯的。DL 的成敗 80% 取決於資料和訓練設定，只有 20% 取決於架構選擇。」

---

## S17 · PITFALL — CNN / RNN / Transformer 不是互相取代

- 🖼️ 畫面：三欄對比表
- 📣 畫面上的字：
  - 欄1 CNN：「空間結構 · 圖片 / 醫療影像 / 衛星圖 · 局部特徵提取」
  - 欄2 RNN：「序列依賴 · 時間序列 / 感測器 / 語音（短序列）· 遞迴記憶」
  - 欄3 Transformer：「長距離關聯 · 語言 / 多模態 / 長文本 · 自注意力機制」
  - 下方：「選架構 = 看你的資料結構，不是追潮流」
- 🎙️ 講者這時說：「CNN 看局部、RNN 看順序、Transformer 看全局。它們不是 1.0 / 2.0 / 3.0 的關係。你做即時邊緣影像辨識，CNN 跑得比 Transformer 快十倍。你做長文本理解，Transformer 碾壓 RNN。選架構要問：我的資料長什麼樣？」

---

## S18 · PRACTICE-PROMPT — loss curve 診斷

- 🖼️ 畫面：白底 / 三組 loss curve 截圖 / 底部計時器
- 📣 畫面上的字：
  - 標題：「練習時間 · 5 分鐘 · 診斷三組 loss curve」
  - 圖A：train 降 val 升 → 你的診斷？你會怎麼改？
  - 圖B：兩條都平坦 → 你的診斷？
  - 圖C：train 震盪劇烈 → 你的診斷？
  - 提示：答案在 S10 / S12 / S13
- 🎙️ 講者這時說：「五分鐘，在紙上寫下你的判斷和行動方案。A 是 overfitting——要 early stop 或加 data。B 可能 lr 太小或模型太簡單。C 是 lr 太大。寫完跟旁邊對答案。」

---

## S19 · CHECKPOINT — 架構選型與 embedding

- 🖼️ 畫面：白底，三題列點
- 📣 畫面上的字：
  - Q1：影像分類選什麼架構？為什麼？
  - Q2：聊天機器人選什麼架構？為什麼？
  - Q3：embedding 比 one-hot 好在哪？
- 🎙️ 講者這時說：「Q1：影像 → 空間結構 → CNN（或 ViT，但 CNN 仍是主力）。Q2：語言 + 長距離 → Transformer。Q3：embedding 是密集向量、有語意距離，one-hot 是稀疏矩陣、沒有語意。答得出來代表你能做選型判斷了。」

---

## S20 · PRACTICE-PROMPT — 架構選型實戰

- 🖼️ 畫面：白底 / 三個情境 / 底部計時器
- 📣 畫面上的字：
  - 標題：「挑戰題 · 8 分鐘 · 選架構並寫理由」
  - 情境A：醫院皮膚科 — 皮膚病變照片分類
  - 情境B：量化交易 — 過去 60 天股價預測明日漲跌
  - 情境C：電商客服 — 自動回覆用戶問題
  - 任務：每個情境選 CNN / RNN / Transformer，寫一句判斷理由
- 🎙️ 講者這時說：「八分鐘。A 是影像 → CNN。B 是短序列時間序列 → RNN 或 1D-CNN 都可以。C 是自然語言理解 + 生成 → Transformer。但我要的不是答案，是你的判斷理由。」

---

## S21 · CONCEPT-CARD — embedding 為什麼重要

- 🖼️ 畫面：左 one-hot 稀疏矩陣 vs 右 embedding 密集向量 + 語意空間散點圖（真圖佔位）
- 📣 畫面上的字：
  - 左：「one-hot：[0,0,1,0,0,...] — 10000 維、稀疏、無語意距離」
  - 右：「embedding：[0.23, -0.45, 0.78, ...] — 128 維、密集、有語意距離」
  - 下方：「embedding 讓離散的東西（文字/商品/用戶）變成可以算距離的向量 → 搜尋 / 推薦 / RAG 的基石」
- 🎙️ 講者這時說：「one-hot 把每個詞當成獨立的，cat 和 dog 的距離跟 cat 和 pizza 的距離一樣遠。embedding 把它們放進一個有意義的空間——cat 和 dog 靠近，cat 和 pizza 遠離。這就是為什麼現代搜尋引擎能理解『同義詞』，推薦系統能找到『相似商品』。Ch04 的 RAG 就是建立在 embedding 搜尋上的。」

---

## S22 · PYRAMID — 三層 takeaway

- 🖼️ 畫面：三層金字塔 + 底部 inverted thesis box
- 📣 畫面上的字：
  - 最頂：目的（表徵學習：讓模型自己長出特徵）
  - 第二：引擎（訓練循環：data → forward → loss → backward → update）
  - 第三：容器（tensor：有形狀的數字容器 + shape/dtype/device）
  - 底：「下一章，Transformer 的 embedding 會驅動 prompt / RAG / agent 整條生成式 AI pipeline」
- 🎙️ 講者這時說：「三層收掉。最底下是 tensor 容器；中間是訓練循環引擎；最上面是表徵學習——讓機器自己學特徵。會了這三層，下一章生成式 AI 你就知道：Transformer 產出的 embedding 是怎麼被 prompt engineering、RAG、tool use 拿來用的。」

---

**節奏檢查**：
- 動機（S1-3） → tensor（S4-5） → 檢核（S7） → 訓練循環（S8） → 梯度直覺（S9） → 陷阱（S10） → 旋鈕（S11） → loss curve（S12） → 陷阱（S13） → 檢核（S14） → 表徵學習（S15） → 陷阱（S16-17） → 練習（S18） → 檢核（S19） → 練習（S20） → embedding（S21） → 收束（S22）
- 4 個 PITFALL 頁（S10 P3 / S13 P2 / S16 P1 / S17 P4）全數對應 teacher_notes S4
- 3 個 CHECKPOINT（S7 / S14 / S19）分布在 7/14/19 位置，約每 6-7 張插一張
