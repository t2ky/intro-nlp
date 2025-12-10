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

# 感情のモデル化：4つの代表的理論

<div class="grid grid-cols-2 gap-4 mt-4">

<div v-click class="border p-3 rounded">

### Ekmanの基本6感情 (1992)
怒り、嫌悪、恐れ、喜び、悲しみ、驚き

<div class="text-xs mt-2">基本的情動理論の代表</div>

</div>

<div v-click class="border p-3 rounded">

### Russellの円環モデル (1980)
感情価 (Valence) × 覚醒度 (Arousal)

<div class="text-xs mt-2">2次元空間での表現</div>

</div>

<div v-click class="border p-3 rounded">

### Pankseppの基本感情システム
神経科学的アプローチ

<div class="text-xs mt-2">脳の感情回路に着目</div>

</div>

<div v-click class="border p-3 rounded">

### Plutchikの基本8感情
喜び、信頼、恐れ、驚き、悲しみ、嫌悪、怒り、期待

<div class="text-xs mt-2">
感情の強度と対立関係を表現

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

# MeCab実習 Step 4: 実行してみよう

<div class="mt-4">

## ハンズオン課題 🎯

以下のコードを `mecab_demo.py` として保存し、実行してみましょう：

```python {*}{maxHeight:'320px'}
import MeCab

def analyze_text(text):
    mecab = MeCab.Tagger()
    print(f"入力: {text}\n")

    # 単語と品詞を抽出
    node = mecab.parseToNode(text)
    words = []
    while node:
        if node.surface:
            word = node.surface
            pos = node.feature.split(',')[0]
            words.append(f"{word}({pos})")
        node = node.next

    print("分かち書き結果:")
    print(" / ".join(words))
    print()

# 試してみよう！
texts = [
    "今日はいい天気ですね",
    "ロボットが人間の感情を理解する",
    "嬉しいときも悲しいときもある"
]

for text in texts:
    analyze_text(text)
```

</div>

---
layout: default
---

# MeCab実習 Step 5: 感情語を抽出してみる

<div class="mt-4">

## 感情を表す単語を見つけよう

```python {all|1-7|9-24|26-30|all}{maxHeight:'360px'}
import MeCab

# 感情語の辞書（簡易版）
emotion_words = {
    "嬉しい": "喜び", "楽しい": "喜び", "幸せ": "喜び",
    "悲しい": "悲しみ", "辛い": "悲しみ",
    "怒る": "怒り", "腹が立つ": "怒り",
    "怖い": "恐れ", "不安": "恐れ"
}

def extract_emotions(text):
    mecab = MeCab.Tagger()
    node = mecab.parseToNode(text)

    emotions = []
    while node:
        if node.surface:
            word = node.surface
            base_form = node.feature.split(',')[6]  # 原形
            if base_form in emotion_words:
                emotions.append((word, emotion_words[base_form]))
        node = node.next

    return emotions

# 試してみよう
text = "今日は楽しかったけど、明日のテストが不安です"
print(f"テキスト: {text}")
emotions = extract_emotions(text)
print(f"検出された感情語: {emotions}")
```

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

# DeBERTa実習 Step 2: モデルのロード

<div class="mt-4">

```python {all|1-2|4-6|8-10|12-15|all}
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# モデル名を指定
model_name = "neuralnaut/deberta-wrime-emotions"

# トークナイザーとモデルをロード
print("モデルをロード中...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

print("✅ モデルのロード完了！")
print(f"モデルの出力次元: {model.config.num_labels}")
# → 8 (Plutchikの8感情に対応)
```

<v-click>

<div class="mt-4 p-3 bg-blue-50 rounded text-sm">

💡 初回実行時はモデルのダウンロードに数分かかります（約500MB）

</div>

</v-click>

</div>

---
layout: default
---

# DeBERTa実習 Step 3: 推論関数を作る

<div class="mt-4">

```python {all|1-3|5-7|9-12|14-16|18-22|all}
def predict_emotions(text, model, tokenizer):
    """テキストから8つの感情スコアを予測"""

    # トークン化
    inputs = tokenizer(text, return_tensors="pt",
                      max_length=128, truncation=True,
                      padding=True)

    # 推論（勾配計算不要）
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits.squeeze()

    # 0-1の範囲から0-3にデノーマライズ
    predictions = logits.cpu().numpy() * 3.0

    # 感情ラベル（WRIMEの順序）
    emotions = ["joy", "sadness", "anticipation", "surprise",
                "anger", "fear", "disgust", "trust"]

    # 辞書形式で返す
    return {emotion: float(score) for emotion, score in zip(emotions, predictions)}
```

</div>

---
layout: default
---

# DeBERTa実習 Step 4: 実行してみよう（基本編）

<div class="mt-4">

```python {all|1-3|5-9|11-14|all}{maxHeight:'260px'}
# サンプルテキスト
texts = [
    "今日は最高の一日でした！",
    "明日のテストが心配で眠れない",
    "友達に裏切られて本当に悲しい"
]

# 各テキストで予測
for text in texts:
    print(f"\n📝 テキスト: {text}")
    emotions = predict_emotions(text, model, tokenizer)

    # スコアが高い順にソート
    sorted_emotions = sorted(emotions.items(),
                            key=lambda x: x[1], reverse=True)

    print("感情スコア（上位3つ）:")
    for emotion, score in sorted_emotions[:3]:
        print(f"  {emotion}: {score:.3f}")
```

<v-click>

## 出力例

```text
📝 テキスト: 今日は最高の一日でした！
感情スコア（上位3つ）:
  joy: 2.456
  anticipation: 1.234
  trust: 0.987
```

</v-click>

</div>

---
layout: default
---

# DeBERTa実習 Step 5: 可視化してみよう

<div class="mt-4">

```python {all|1-2|4-16|18-20|all}{maxHeight:'400px'}
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_emotions(text, emotions):
    """感情スコアを棒グラフで可視化"""

    # 日本語表示用のラベル
    labels_ja = ["喜び", "悲しみ", "期待", "驚き",
                 "怒り", "恐れ", "嫌悪", "信頼"]

    scores = list(emotions.values())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels_ja, scores, color='skyblue', edgecolor='navy')
    plt.title(f'感情分析結果: {text}', fontsize=14, pad=20)
    plt.ylabel('感情スコア (0-3)', fontsize=12)
    plt.ylim(0, 3)
    plt.grid(axis='y', alpha=0.3)

    # 最大値を強調
    max_idx = scores.index(max(scores))
    bars[max_idx].set_color('orange')

    plt.tight_layout()
    plt.show()

# 使ってみよう
text = "今日は最高の一日でした！"
emotions = predict_emotions(text, model, tokenizer)
visualize_emotions(text, emotions)
```

</div>

---
layout: default
---

# DeBERTa実習 Step 6: 自分で試してみよう

<div class="mt-4">

## インタラクティブ版

```python {all|1-19|21-24|all}{maxHeight:'360px'}
def interactive_emotion_analysis():
    """対話的に感情分析を実行"""

    print("=" * 50)
    print("DeBERTa 感情分析システム")
    print("=" * 50)
    print("感情を分析したいテキストを入力してください")
    print("（終了するには 'quit' と入力）")
    print()

    while True:
        text = input("📝 テキスト: ")

        if text.lower() == 'quit':
            print("👋 終了します")
            break

        if not text.strip():
            continue

        emotions = predict_emotions(text, model, tokenizer)

        print("\n感情スコア:")
        for emotion, score in sorted(emotions.items(),
                                     key=lambda x: x[1], reverse=True):
            bar = "█" * int(score * 10)
            print(f"  {emotion:15s}: {score:.3f} {bar}")
        print()

# 実行
interactive_emotion_analysis()
```

</div>

---
layout: default
---

# DeBERTa実習 Step 7: 実践課題 🎯

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
