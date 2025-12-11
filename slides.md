---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
colorSchema: light
info: |
  ## HAI班 新人向け自然言語処理入門
  Affective Computingと感情推定の実践
drawings:
  persist: false
transition: slide-left
title: HAI班 自然言語処理入門
mdc: true
---

<style>
/* ライトモード強制 & 視認性向上 */
.slidev-layout {
  background-color: #ffffff !important;
  color: #1a1a1a !important;
}

/* 背景色付きボックスの文字色を強制 */
.bg-blue-50, .bg-yellow-50, .bg-green-50, .bg-red-50,
.bg-purple-50, .bg-gray-50 {
  color: #1a1a1a !important;
}

/* コードブロックは見やすく */
code {
  background-color: #f5f5f5 !important;
  color: #2d3748 !important;
}

/* リンクの色 */
a {
  color: #2563eb !important;
}
</style>

# HAI班 新人向け

# 自然言語処理入門

Affective Computingと感情推定の実践

M1 kiyo

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

---
layout: default
---

# 本日の目標

<v-clicks>

- **理論を学ぶ**: Affective Computingと感情モデルの基礎
- **手を動かす**: MeCabで形態素解析を体験
- **最新技術を試す**: DeBERTaで感情分類を実行
- **HAI/HRIへの応用**: ロボット対話における感情推定の重要性を理解

</v-clicks>

<div class="mt-8" v-click>

## なぜ感情推定が重要か？

人間とロボットの自然な対話には、**相手の感情を理解する能力**が不可欠

</div>

---
layout: default
---

# Affective Computingとは

<div class="grid grid-cols-2 gap-8 mt-6">

<div>

<div class="text-sm">

**定義** (Picard, 1997)

コンピュータシステムに感情状態の**認識、理解、シミュレーション、刺激**を組み入れる学際的研究分野

<v-clicks>

**歴史**
- 1997年: Picardが用語を考案
- 2010年: IEEE Transactions on Affective Computing創刊
- 現在: Amazon、Google、Facebook等が活用

**学際性**
- コンピュータ科学
- 心理学・神経科学
- 哲学・芸術

</v-clicks>

</div>

</div>

<div>

## 感情の構成要素

<v-click>

<div class="text-xs mt-4">

**6つの要素** (Fontaine et al., 2007)

1. **評価プロセス** - 状況の解釈
2. **心理生理学的変化** - 心拍数、扁桃体反応
3. **運動発現** - 表情、声、身振り
4. **行動傾向** - 闘争 vs 逃走
5. **主観的体験** - 自己報告
6. **情動制御** - 抑制、再評価

<div class="mt-4 p-2 bg-blue-50 rounded">
💡 これらの要素は緩やかに関連（表情だけでは感情を完全に予測できない）
</div>

</div>

</v-click>

</div>

</div>

<div class="absolute bottom-2 left-8 right-8 text-xs text-gray-800">
<a href="https://www.jstage.jst.go.jp/article/jjsai/36/1/36_4/_article/-char/ja" target="_blank">Gratch, J. (2021). Affective Computingの研究分野：学際的視点. 人工知能, 36(1).</a> | <a href="https://doi.org/10.1111/j.1467-9280.2007.02024.x" target="_blank">Fontaine et al. (2007). The World of Emotions is not Two-Dimensional.</a>
</div>

---
layout: default
---

# 感情のモデル化：代表的理論 (1/2)

<div class="grid grid-cols-2 gap-8 mt-6">

<div>

## Ekmanの基本6感情 (1992)

<img src="/ekman.jpg" class="w-full rounded shadow-lg" />

<div class="text-sm mt-4">

**6つの基本感情**
- 怒り、嫌悪、恐れ、喜び、悲しみ、驚き

**特徴**: 基本的情動理論の代表。普遍的な表情と結びついている。

</div>

</div>

<div>

## Russellの円環モデル (1980)

<img src="/russell-circumplex.jpg" class="w-full rounded shadow-lg" />

<div class="text-sm mt-4">

**2次元空間モデル**
- 感情価 (Valence): ポジティブ ↔ ネガティブ
- 覚醒度 (Arousal): 高覚醒 ↔ 低覚醒

**特徴**: すべての感情を連続的な2次元空間で表現。

</div>

</div>

</div>

---
layout: default
---

# 感情のモデル化：代表的理論 (2/2)

<div class="grid grid-cols-2 gap-8 mt-6">

<div>

## Plutchikの感情の輪 (1980)

<img src="/plutchik-wheel.png" class="w-full rounded shadow-lg" />

<div class="text-sm mt-4">

**8つの基本感情**
- 喜び、信頼、恐れ、驚き、悲しみ、嫌悪、怒り、期待

**特徴**: 感情の強度、類似性、対立関係を輪状に表現。複合感情も説明可能。

</div>

</div>

<div>

## Pankseppの基本感情システム

<div class="text-base mt-12">

**7つの感情システム** (神経科学的アプローチ)

1. **SEEKING** (探索) - ドーパミン系
2. **RAGE** (怒り) - 闘争反応
3. **FEAR** (恐れ) - 回避行動
4. **LUST** (性欲) - 生殖行動
5. **CARE** (養育) - オキシトシン系
6. **PANIC/GRIEF** (パニック/悲嘆) - 分離不安
7. **PLAY** (遊び) - 社会的学習

<div class="mt-4 p-3 bg-purple-50 rounded">
💡 **特徴**: 脳の感情回路と神経伝達物質に基づく
</div>

</div>

</div>

</div>

---
layout: default
---

# 自然言語処理の歴史

<div class="timeline mt-8">

<v-clicks>

<div class="flex items-start mb-6">
  <div class="w-32 flex-shrink-0 text-right pr-4 font-bold">1980年代</div>
  <div class="flex-grow border-l-2 border-blue-500 pl-4">
    <div class="font-semibold">ルールベース手法</div>
    <div class="text-sm">辞書、パターンマッチング → 柔軟性の欠如</div>
  </div>
</div>

<div class="flex items-start mb-6">
  <div class="w-32 flex-shrink-0 text-right pr-4 font-bold">1990-2000年代</div>
  <div class="flex-grow border-l-2 border-green-500 pl-4">
    <div class="font-semibold">統計的手法</div>
    <div class="text-sm">機械学習（Naive Bayes, SVM）、Bag-of-Words、TF-IDF</div>
  </div>
</div>

<div class="flex items-start mb-6">
  <div class="w-32 flex-shrink-0 text-right pr-4 font-bold">2010年代前半</div>
  <div class="flex-grow border-l-2 border-purple-500 pl-4">
    <div class="font-semibold">深層学習の台頭</div>
    <div class="text-sm">Word2Vec (2013)、RNN、LSTM</div>
  </div>
</div>

<div class="flex items-start mb-6">
  <div class="w-32 flex-shrink-0 text-right pr-4 font-bold">2017年〜</div>
  <div class="flex-grow border-l-2 border-red-500 pl-4">
    <div class="font-semibold">Transformer革命</div>
    <div class="text-sm">BERT (2018)、RoBERTa、DeBERTa → 今日使うモデル！</div>
  </div>
</div>

</v-clicks>

</div>

---
layout: default
---

# BERT系列モデルの進化

<div class="flex items-center justify-between mt-8">

<v-clicks>

<div class="text-center">
  <div class="text-4xl mb-2">🤖</div>
  <div class="font-bold">BERT</div>
  <div class="text-xs">(2018)</div>
  <div class="text-xs mt-2">双方向エンコーダ<br/>事前学習</div>
</div>

<div class="text-2xl">→</div>

<div class="text-center">
  <div class="text-4xl mb-2">🚀</div>
  <div class="font-bold">RoBERTa</div>
  <div class="text-xs">(2019)</div>
  <div class="text-xs mt-2">学習戦略最適化<br/>Dynamic Masking</div>
</div>

<div class="text-2xl">→</div>

<div class="text-center border-2 border-yellow-400 p-3 rounded bg-yellow-50">
  <div class="text-4xl mb-2">⭐</div>
  <div class="font-bold text-lg">DeBERTa</div>
  <div class="text-xs">(2020)</div>
  <div class="text-xs mt-2">
    <strong>Disentangled Attention</strong><br/>
    内容と位置を分離<br/>
    <strong>→ 感情分類に最適！</strong>
  </div>
</div>

</v-clicks>

</div>

<div class="mt-8 p-4 bg-blue-50 rounded" v-click>

**日本語モデル**: 東北大BERT、NICT BERT、京大DeBERTa等が利用可能

</div>

---
layout: center
class: text-center
---

# 🛠️ 実習パート1

# MeCabで形態素解析

日本語処理の基礎を体験しよう

---
layout: default
---

# なぜ日本語は難しいのか？

<div class="grid grid-cols-2 gap-8 mt-8">

<div>

## 英語の場合

```text
I love you
↓ スペースで区切られている
["I", "love", "you"]
```

<div class="text-green-600 font-bold mt-4">✅ 単語境界が明確</div>

</div>

<div>

## 日本語の場合

```text
私はあなたが好きです
↓ どこで区切る？🤔
["私", "は", "あなた", "が", "好き", "です"]
["私は", "あなたが", "好きです"]
["私", "はあなた", "が好き", "です"]
```

<div class="text-red-600 font-bold mt-4">❌ 分かち書きがない！</div>

</div>

</div>

<div class="mt-8 p-4 bg-yellow-50 rounded" v-click>

## MeCabの役割

**形態素解析エンジン**として、日本語テキストを単語に分割し、品詞タグを付与

</div>

---
layout: default
---

# MeCab実習 Step 1: インストール

<div class="mt-4">

## macOSの場合

```bash
# Homebrewでインストール
brew install mecab
brew install mecab-ipadic

# Pythonバインディング
pip install mecab-python3
```

## Ubuntuの場合

```bash
# aptでインストール
sudo apt-get install mecab libmecab-dev mecab-ipadic-utf8

# Pythonバインディング
pip install mecab-python3
```

## Windowsの場合

MeCabインストーラーをダウンロード:
https://github.com/ikegami-yukino/mecab/releases

</div>

---
layout: default
---

# MeCab実習 Step 2: 動作確認

<div class="mt-4">

## コマンドラインで試す

```bash
echo "今日はいい天気ですね" | mecab
```

<v-click>

## 出力例

```text
今日    名詞,副詞可能,*,*,*,*,今日,キョウ,キョー
は      助詞,係助詞,*,*,*,*,は,ハ,ワ
いい    形容詞,自立,*,*,形容詞・イイ,基本形,いい,イイ,イイ
天気    名詞,一般,*,*,*,*,天気,テンキ,テンキ
です    助動詞,*,*,*,特殊・デス,基本形,です,デス,デス
ね      助詞,終助詞,*,*,*,*,ね,ネ,ネ
EOS
```

</v-click>

<div class="mt-4 text-sm" v-click>

各行の構成: `表層形\t品詞,品詞細分類1,品詞細分類2,...,原形,読み,発音`

</div>

</div>

---
layout: default
---

# MeCab実習 Step 3: Pythonで使う

<div class="mt-4">

## サンプルコード

```python {all|1-2|4-5|7-8|10-14|all}
import MeCab
mecab = MeCab.Tagger()

# 解析したいテキスト
text = "私はロボットとの対話が好きです"

# 形態素解析実行
result = mecab.parse(text)

# 結果表示
print("=== 形態素解析結果 ===")
print(result)

print("\n=== 単語のみ抽出 ===")
node = mecab.parseToNode(text)
while node:
    if node.surface:  # 表層形がある場合
        print(f"{node.surface}\t{node.feature.split(',')[0]}")
    node = node.next
```

</div>

---
layout: default
---

# MeCab実習 Step 4: 実用例 - 喜び語カウンター

<div class="mt-4">

## 喜びに関する単語を数えてみよう 😊

```python {all|1-6|8-21|23-27|all}{maxHeight:'340px'}
import MeCab

# 喜びに関する単語リスト
joy_words = ["嬉しい", "楽しい", "幸せ", "喜ぶ", "最高",
             "良い", "素晴らしい", "ワクワク", "満足"]

def count_joy_words(text):
    """テキストから喜び語をカウント"""
    mecab = MeCab.Tagger()
    node = mecab.parseToNode(text)

    count = 0
    found_words = []
    while node:
        if node.surface:
            base_form = node.feature.split(',')[7]  # 原形
            if base_form in joy_words:
                count += 1
                found_words.append(node.surface)
        node = node.next

    return count, found_words

# 使ってみよう
text = "今日は最高に楽しかった！嬉しいことがたくさんあった。"
count, words = count_joy_words(text)
print(f"喜び語: {count}個 → {words}")
# 出力: 喜び語: 3個 → ['最高', '楽しかっ', '嬉しい']
```

</div>

---
layout: default
---

# MeCab実習 Step 5: HAI応用例 - フィラーチャットボット

<div class="mt-4">

## 名詞を抽出して相槌を打つボット 🤖

```python {all|1-15|17-22|24-32|all}{maxHeight:'360px'}
import MeCab

def filler_bot(user_input):
    """名詞を抽出してフィラー応答を返す"""
    mecab = MeCab.Tagger()
    node = mecab.parseToNode(user_input)

    # 名詞を抽出
    nouns = []
    while node:
        if node.surface and node.feature.split(',')[0] == '名詞':
            nouns.append(node.surface)
        node = node.next

    return nouns

def chat():
    """簡単なチャットボット"""
    print("ボット: 今日は何があった？")
    user_input = input("あなた: ")
    nouns = filler_bot(user_input)

    # フィラー応答を生成
    if nouns:
        import random
        responses = [f"{nouns[0]}かぁ", f"{nouns[0]}ね",
                    f"へぇ、{nouns[0]}なんだ"]
        print(f"ボット: {random.choice(responses)}")
    else:
        print("ボット: そうなんだ")

# 実行
chat()
```

<div class="mt-3 text-sm bg-green-50 p-2 rounded">
<strong>実行例:</strong><br>
ボット: 今日は何があった？<br>
あなた: 友達とカフェに行った<br>
ボット: 友達かぁ
</div>

</div>

---
layout: center
class: text-center
---

# 📊 WRIMEデータセット

Plutchikの8感情で日本語テキストをラベリング

---
layout: default
---

# WRIME: Writers and Readers Emotion corpus

<div class="mt-4">

<div class="grid grid-cols-2 gap-6">

<div>

## データセットの概要

- **提供**: 大阪大学・愛媛大学（梶原智之 他, NAACL 2021）
- **規模** (Ver.2):
  - 35,000件の投稿
  - 60人の筆者から収集
  - クラウドワーカ3人による客観ラベル

## 特徴

<v-clicks>

- **主観**（書き手1人）と**客観**（読み手3人）の両方の感情
- **0-3の4段階**で各感情の強度をラベル付け
- Ver.2では感情極性（-2〜+2）も追加

</v-clicks>

</div>

<div>

## Plutchikの8感情 ⭐

<div class="text-sm mt-4 space-y-1">

<v-clicks>

- 😊 **joy** (喜び)
- 😢 **sadness** (悲しみ)
- 🤔 **anticipation** (期待)
- 😲 **surprise** (驚き)
- 😠 **anger** (怒り)
- 😰 **fear** (恐れ)
- 🤢 **disgust** (嫌悪)
- 🤝 **trust** (信頼)

</v-clicks>

</div>

<div class="mt-4 p-3 bg-yellow-50 rounded text-sm" v-click>

💡 第2章で紹介したPlutchikモデルを使用！

</div>

</div>

</div>

</div>

<div class="absolute bottom-2 left-8 right-8 text-xs text-gray-800">
<a href="https://aclanthology.org/2021.naacl-main.169/" target="_blank">Kajiwara et al. (2021). WRIME: A New Dataset for Emotional Intensity Estimation with Subjective and Objective Annotations. NAACL 2021.</a>
</div>

---
layout: default
---

# なぜDeBERTaなのか？

<div class="mt-6">

## 性能比較 (Performance Evaluation論文より)

<v-clicks>

| モデル | 平均精度 | F1スコア |
|--------|----------|----------|
| **DeBERTa-v3-large** | **0.860** | **0.662** ⭐ |
| ChatGPT-4o | - | 0.527 |
| TinySwallow-1.5B | - | 0.292 |

<div class="mt-6 grid grid-cols-2 gap-4">

<div class="p-4 bg-green-50 rounded">

### ✅ DeBERTaの強み

- クラス不均衡に強い
- 高頻度感情も低頻度感情も安定
- リアルタイム処理に適している

</div>

<div class="p-4 bg-blue-50 rounded">

### 📊 感情別性能

- 最高: joy (r=0.666)
- 最低: trust (r=0.264)
- RMSE: 0.753 (0-3スケール)

</div>

</div>

</v-clicks>

</div>

<div class="absolute bottom-1 left-8 right-8 text-xs text-gray-800">
<a href="https://arxiv.org/abs/2505.00013" target="_blank">Performance Evaluation of Emotion Classification in Japanese Using RoBERTa and DeBERTa. arXiv:2505.00013, 2025.</a>
</div>

---
layout: center
class: text-center
---

# 🚀 実習パート2

# DeBERTa-WRIMEで感情分類

実際に動かしてみよう！

---
layout: default
---

# DeBERTa実習 Step 1: 環境構築

<div class="mt-4">

## 必要なライブラリのインストール

```bash
# PyTorchとTransformersをインストール
pip install torch transformers

# 可視化用（オプション）
pip install matplotlib seaborn
```

<v-click>

## インストール確認

```python
import torch
import transformers

print(f"PyTorch version: {torch.__version__}")
print(f"Transformers version: {transformers.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
```

</v-click>

<div class="mt-4 p-3 bg-yellow-50 rounded text-sm" v-click>

⚠️ GPUがなくてもCPUで動作します（少し時間がかかります）

</div>

</div>

---
layout: default
---

# DeBERTa実習 Step 2: 基本的な使い方

<div class="mt-4">

## 感情推定を実行してみよう

```python {all|1-3|5-8|10-11|13-17|19-23|25-27|all}{maxHeight:'380px'}
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np

# モデルとトークナイザのロード
model_name = "neuralnaut/deberta-wrime-emotions"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# 感情ラベル（出力の順序に対応）
EMOTION_LABELS = ["joy", "sadness", "anticipation", "surprise", "anger", "fear", "disgust", "trust"]

# 推論
text = "今日はとても楽しい一日でした！"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

model.eval()
with torch.no_grad():
    outputs = model(**inputs)
    predictions = outputs.logits.cpu().numpy()[0]

# ⚠️ 重要：デノーマライズ (0-1 → 0-3)
predictions = predictions * 3.0
predictions = np.clip(predictions, 0.0, 3.0)

# 結果表示
print(f"テキスト: {text}\n")
for emotion, score in zip(EMOTION_LABELS, predictions):
    print(f"{emotion:15s}: {score:.2f}")
```

</div>

---
layout: default
---

# DeBERTa実習 Step 3: MeCabとの比較

<div class="mt-4">

## 分かち書きの違いを見てみよう

```python {all|1-5|7-10|12-15|17-21|all}{maxHeight:'360px'}
from transformers import AutoTokenizer
import MeCab

# モデルとトークナイザのロード
model_name = "neuralnaut/deberta-wrime-emotions"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# MeCabの準備
mecab = MeCab.Tagger("-Owakati")

# テキスト
text = "今日は最高の一日でした"

# MeCabの分かち書き
mecab_tokens = mecab.parse(text).strip()
print(f"MeCab:   {mecab_tokens}")

# DeBERTa tokenizerの分かち書き
deberta_tokens = " ".join(tokenizer.tokenize(text))
print(f"DeBERTa: {deberta_tokens}")
```

<v-click>

## 出力結果

```text
MeCab:   今日 は 最高 の 一 日 でし た
DeBERTa: 今日 は 最高 の 一日 でした
```

<div class="mt-3 p-3 bg-purple-50 rounded text-sm">
💡 **DeBERTaはサブワード単位で分割**。未知語にも対応できる柔軟な分かち書きを実現。
</div>

</v-click>

</div>

---
layout: default
---

# DeBERTa実習 Step 4: HAI応用例 - 共感チャットボット

<div class="mt-4">

## 感情推定に基づいて共感応答するボット 🤖

```python {all|1-4|6-9|11-33|35-42|44-50|52-54|all}{maxHeight:'400px'}
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np
import random

# モデルとトークナイザのロード
model_name = "neuralnaut/deberta-wrime-emotions"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# 感情ラベル
EMOTION_LABELS = ["joy", "sadness", "anticipation", "surprise",
                  "anger", "fear", "disgust", "trust"]

def predict_emotion(text):
    """感情推定"""
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    model.eval()
    with torch.no_grad():
        outputs = model(**inputs)
        predictions = outputs.logits.cpu().numpy()[0]

    predictions = predictions * 3.0
    predictions = np.clip(predictions, 0.0, 3.0)

    # 最も強い感情を返す
    max_idx = np.argmax(predictions)
    return EMOTION_LABELS[max_idx], predictions[max_idx]

def empathy_bot(user_input):
    """共感応答を生成"""
    emotion, score = predict_emotion(user_input)

    responses = {
        "joy": ["それは嬉しかったね！", "良かったね！"],
        "sadness": ["それは悲しかったね", "辛かったね"],
        "anger": ["それは腹が立つね", "イライラするよね"],
        "fear": ["それは不安だね", "心配だよね"],
        "surprise": ["それは驚いたね！", "びっくりしたね"],
    }

    response = responses.get(emotion, ["そうなんだ", "なるほどね"])
    return random.choice(response), emotion, score

# 実行
print("ボット: 今日は何があった？")
user_input = input("あなた: ")
response, emotion, score = empathy_bot(user_input)
print(f"ボット: {response}")
print(f"（検出: {emotion} = {score:.2f}）")
```

<div class="mt-3 text-sm bg-green-50 p-2 rounded">
<strong>実行例:</strong><br>
ボット: 今日は何があった？<br>
あなた: テストで悪い点を取ってしまった<br>
ボット: それは悲しかったね<br>
（検出: sadness = 2.34）
</div>

</div>

---
layout: default
---

# 実践課題 🎯

<div class="mt-4">

## 以下のテキストで感情分析してみよう

<div class="grid grid-cols-2 gap-4 mt-4 text-sm">

<div class="border p-3 rounded">

### ポジティブ系

```
1. "新しいプロジェクトが始まってワクワクする"
2. "友達と久しぶりに会えて嬉しかった"
3. "テストで満点を取れて最高の気分だ"
```

</div>

<div class="border p-3 rounded">

### ネガティブ系

```
4. "締め切りに間に合わなくて焦っている"
5. "大事なものを失くして落ち込んでいる"
6. "約束を破られて信じられない"
```

</div>

<div class="border p-3 rounded">

### 混合感情系

```
7. "合格したけど、友達が落ちて複雑な気持ち"
8. "引っ越しは楽しみだけど寂しさもある"
```

</div>

<div class="border p-3 rounded">

### オリジナル

```
9. 自分で考えた文章を入れてみよう！
```

<div class="mt-2 text-xs text-gray-600">
どんな感情が検出されるか予想してから試してみよう
</div>

</div>

</div>

</div>

---
layout: default
---

# HAI/HRIへの応用

<div class="mt-4">

## ロボット対話における感情推定の活用

<div class="grid grid-cols-2 gap-6 mt-6">

<div>

### リアルタイム感情認識

<v-clicks>

```python
# ユーザの発話を分析
user_input = "もう疲れた..."
emotions = predict_emotions(
    user_input, model, tokenizer
)

# 感情に応じた応答
if emotions["sadness"] > 2.0:
    response = "大丈夫ですか？"
    + "少し休憩しましょう"
elif emotions["anger"] > 2.0:
    response = "何かお困りですか？"
    + "お手伝いできることはありますか"
```

</v-clicks>

</div>

<div>

### 評価理論との統合

<v-clicks>

- **評価プロセス**: 状況の解釈
- **感情推定**: テキストから感情を検出
- **行動生成**: 適切な応答を選択

<div class="mt-4 p-3 bg-blue-50 rounded text-sm">

**応用例**
- 高齢者見守りロボット
- メンタルヘルスケアシステム
- カスタマーサポートAI

</div>

</v-clicks>

</div>

</div>

</div>

---
layout: default
---

# 倫理的配慮

<div class="mt-4">

<div class="grid grid-cols-2 gap-6">

<div>

## 認識の限界

<v-clicks>

- 表情と感情は必ずしも一致しない
- 文脈依存性が高い
- 文化的差異がある

</v-clicks>

<div class="mt-4 p-3 bg-yellow-50 rounded text-sm" v-click>

⚠️ **表情だけでは不十分**

Gratch論文より: 社交性、意外性、失望など様々な理由で微笑むため、笑顔 = 喜びとは限らない

</div>

</div>

<div>

## バイアスの問題

<v-clicks>

- 人種、性別による精度差
- 学習データの偏り
- 照明、背景等の環境要因

</v-clicks>

<div class="mt-4 p-3 bg-red-50 rounded text-sm" v-click>

🚫 **使用を避けるべき場面**

AI Now Institute 2019報告書: 雇用、法的処罰など重要な意思決定での使用は慎重に

</div>

</div>

</div>

</div>

---
layout: default
---

# まとめ

<div class="mt-8">

## 今日学んだこと

<v-clicks>

<div class="flex items-start mb-4">
  <div class="text-2xl mr-4">📚</div>
  <div>
    <div class="font-bold">理論</div>
    <div class="text-sm">Affective Computing、Plutchikの8感情、評価理論</div>
  </div>
</div>

<div class="flex items-start mb-4">
  <div class="text-2xl mr-4">🛠️</div>
  <div>
    <div class="font-bold">技術</div>
    <div class="text-sm">MeCabで形態素解析、DeBERTaで感情分類</div>
  </div>
</div>

<div class="flex items-start mb-4">
  <div class="text-2xl mr-4">🤖</div>
  <div>
    <div class="font-bold">応用</div>
    <div class="text-sm">HAI/HRIにおける感情推定の重要性と倫理的配慮</div>
  </div>
</div>

</v-clicks>

</div>

---
layout: default
---

# 次のステップ

<div class="mt-6">

## さらに学ぶためのリソース

<v-clicks>

### 📊 データセット
- WRIME corpus 大阪大学・愛媛大学（梶原智之 他, NAACL 2021）
- https://github.com/ids-cv/wrime

### 🤗 モデル
- 8感情強度回帰モデル: [neuralnaut/deberta-wrime-emotions](https://huggingface.co/neuralnaut/deberta-wrime-emotions)
- 感情極性回帰モデル: [neuralnaut/deberta-wrime-sentiment](https://huggingface.co/neuralnaut/deberta-wrime-sentiment)
- ベースモデル: DeBERTa V3 (京都大学NLPラボ) [ku-nlp/deberta-v3-base-japanese](https://huggingface.co/ku-nlp/deberta-v3-base-japanese)

</v-clicks>

</div>

<div class="mt-8 p-4 bg-gradient-to-r from-blue-50 to-purple-50 rounded" v-click>

## 🚀 研究テーマのアイデア

マルチモーダル感情認識 / リアルタイム感情トラッキング / 感情に基づいて変化する〇〇

</div>

---
layout: center
class: text-center
---

# お疲れ様でした！ 🎉

<div class="mt-8">

質問や議論は大歓迎です

</div>

<div class="mt-12 text-sm text-gray-500">

HAI班 新人向け自然言語処理入門

</div>
