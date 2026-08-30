---
theme: default
class: text-center
highlighter: shiki
lineNumbers: false
colorSchema: light
info: |
  ## Development of Frailty Experience System
  フレイル体験システムの開発
drawings:
  persist: false
transition: slide-left
title: Development of Frailty Experience System
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
.bg-purple-50, .bg-gray-50, .bg-orange-50 {
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

/* 日英併記用のスタイル */
.ja-small {
  font-size: 0.75em;
  color: #555;
  margin-top: 0.1rem;
  line-height: 1.2;
}

/* 日英併記の親要素の行間を詰める */
h1, h2, h3, h4, p, li {
  line-height: 1.4;
}
</style>

# Development of Frailty Experience System
<div class="ja-small">フレイル体験システムの開発</div>

Multimodal Aging Simulation through Voice and Facial Features
<div class="ja-small">音声・表情の老化特徴統合による予防啓発アプローチ</div>

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

---
layout: default
---

<div class="ja-small">Master's Thesis Roadmap</div>

<div class="mt-4">

```mermaid
graph TB
    Start["Bachelor(卒論)<br/>発話内容に基づく表情生成"] --> M1

    Frailty["Frailty(今回)<br/>個人性の排除・再現"]
    NTT["NTT<br/>文脈に基づくジェスチャー分析"]

    M1["Expression Generation"] --> M2

    Frailty --> M2["Individuality Control"]
    M2 --> M3

    NTT --> M3["Real-time Agent Motion"]

    style Start fill:#bbdefb,stroke:#1976d2,stroke-width:2px
    style M1 fill:#e3f2fd,stroke:#1976d2,stroke-width:3px
    style M2 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:3px
    style M3 fill:#e8f5e9,stroke:#388e3c,stroke-width:3px
    style Frailty fill:#e1bee7,stroke:#7b1fa2,stroke-width:2px
    style NTT fill:#c8e6c9,stroke:#388e3c,stroke-width:2px
```

</div>

---
layout: default
---

# Background: What is Frailty?

<v-clicks>

- **Frailty (虚弱)**: Intermediate state between healthy aging and requiring care
  <div class="ja-small">健康な老化と要介護状態の中間段階</div>

- Age-related decline in physiological reserves → Increased vulnerability
  <div class="ja-small">加齢に伴う予備能力の低下 → ストレスに対する脆弱性の増加</div>

- **Key point: Reversible with appropriate intervention**
  <div class="ja-small">重要：適切な介入により可逆的に改善可能</div>

</v-clicks>

<v-click>

<div class="mt-8 text-center">

```mermaid
graph LR
    A[Healthy<br/>健康] -->|Aging<br/>加齢| B[Frailty<br/>フレイル]
    B -->|Neglect<br/>放置| C[Care-dependent<br/>要介護]
    B -.Intervention<br/>介入.-> A
    style A fill:#90EE90
    style B fill:#FFB6C1
    style C fill:#FFA07A
```

</div>

<div class="absolute bottom-2 left-8 right-8 text-xs text-gray-800">
<a href="https://www.jpn-geriat-soc.or.jp/publications/other/pdf/review_51_6_497.pdf" target="_blank">荒井秀典. "フレイルの意義." 日老医誌 51.6 (2014): 497-501.</a>
</div>

</v-click>

---
layout: default
---

# Purpose of This Research
<div class="ja-small">本研究の目的</div>

<v-clicks>

- **Challenge**: Frailty is "a distant future" for young people
  <div class="ja-small">課題：若年層にとってフレイルは「遠い未来の話」</div>

- **Approach**: Awareness through experience - making it personal
  <div class="ja-small">アプローチ：体験を通じた気づきにより、自分ごととして捉えてもらう</div>

- **Goal**: Simulating future self to promote preventive behaviors
  <div class="ja-small">目標：将来の自分の姿を疑似体験することで予防行動を促進</div>

</v-clicks>

<v-click>

<div class="grid grid-cols-2 gap-6 mt-8">
<div class="p-4 bg-green-50 rounded border-2 border-green-400">

### ✅ This System IS

- Experience-based awareness tool
  <div class="ja-small">体験型の啓発ツール</div>
- Motivating healthy behaviors
  <div class="ja-small">健康行動への動機づけ</div>

</div>
<div class="p-4 bg-red-50 rounded border-2 border-red-400">

### ❌ This System is NOT

- NOT a diagnostic system
  <div class="ja-small">診断システムではない</div>
- Does not predict individual risk
  <div class="ja-small">個人のリスク予測はしない</div>

</div>
</div>

</v-click>

---
layout: default
---

# System Approach
<div class="ja-small">システムアプローチ</div>

<div class="text-center mb-8">

## Multimodal Aging Simulation
<div class="ja-small">マルチモーダルな老化シミュレーション</div>

</div>

<div class="grid grid-cols-3 gap-6">
<div class="text-center p-6 bg-purple-50 rounded">

### 🎤 Voice Aging
<div class="ja-small">音声老化</div>

<v-click>

**Bruno's Research**
<div class="ja-small">Brunoさんの研究</div>

- VOICEVOX synthesis
  <div class="ja-small">VOICEVOX音声合成</div>
- Reduced speech rate
  <div class="ja-small">話速の低下</div>
- Lower pitch/intonation
  <div class="ja-small">ピッチ・抑揚の低下</div>

</v-click>

</div>
<div class="text-center p-6 bg-blue-50 rounded">

### 👴 Facial Aging
<div class="ja-small">表情老化</div>

<v-click>

**FLAN Implementation**
<div class="ja-small">FLAN実装</div>

- UNet256 model
  <div class="ja-small">UNet256モデル</div>
- MediaPipe detection
  <div class="ja-small">MediaPipe顔検出</div>
- Wrinkle generation
  <div class="ja-small">しわ・たるみ生成</div>

</v-click>

</div>
<div class="text-center p-6 bg-green-50 rounded">

### 🎬 Integration
<div class="ja-small">統合</div>

<v-click>

**Our Contribution**
<div class="ja-small">本研究の貢献</div>

- Audio-visual fusion
  <div class="ja-small">音声・映像融合</div>
- Offline pipeline
  <div class="ja-small">オフライン処理</div>
- Lip-sync adjustment
  <div class="ja-small">リップシンク調整</div>

</v-click>

</div>
</div>

<v-click>

<div class="mt-8 p-4 bg-yellow-50 rounded text-center">

**Concept**: Combining voice and facial aging for realistic, immersive experience
<div class="ja-small">コンセプト：音声老化と表情老化を組み合わせ、リアルで没入感のある体験を実現</div>

</div>

</v-click>

---
layout: default
---

# Processing Pipeline
<div class="ja-small">処理パイプライン</div>

<div class="mt-8">

```mermaid
graph LR
    A[Video<br/>Recording<br/>動画録画] --> B[Transcription<br/>文字起こし<br/>Whisper]
    B --> C[Aged Voice<br/>Generation<br/>老化音声生成<br/>VOICEVOX]
    C --> D[Lip-sync<br/>Adjustment<br/>リップシンク<br/>調整]
    D --> E[Facial<br/>Aging<br/>表情老化<br/>FLAN/UNet256]
    E --> F[Audio-Video<br/>Integration<br/>音声映像<br/>統合]

    style A fill:#e3f2fd
    style B fill:#fff3e0
    style C fill:#fce4ec
    style D fill:#f3e5f5
    style E fill:#e8f5e9
    style F fill:#fff9c4
```

</div>

<v-click>

<div class="mt-8 grid grid-cols-2 gap-6">
<div class="p-4 bg-blue-50 rounded">

### Input
<div class="ja-small">入力</div>

- User records short video (5-10 sec)
  <div class="ja-small">ユーザーが短い動画を録画（5-10秒）</div>
- Speaking naturally to camera
  <div class="ja-small">カメラに向かって自然に話す</div>

</div>
<div class="p-4 bg-green-50 rounded">

### Output
<div class="ja-small">出力</div>

- Aged video with synchronized audio
  <div class="ja-small">音声同期された老化動画</div>
- Realistic aging features (voice + face)
  <div class="ja-small">リアルな老化特徴（音声+顔）</div>

</div>
</div>

</v-click>

---
layout: default
---

<div class="grid grid-cols-2 gap-8">
<div class="text-center">

## Before (Original)
<div class="ja-small">元動画</div>

<div>
  <video src="/before.mov" controls class="w-full rounded-lg border-2 border-gray-400"></video>
</div>

<v-click>

<div class="mt-4 text-sm text-left">

- Young voice & facial expressions
  <div class="ja-small">若年層の声・表情</div>
- Natural speech rate
  <div class="ja-small">自然な話速</div>
- Smooth facial changes
  <div class="ja-small">滑らかな表情変化</div>

</div>

</v-click>

</div>
<div class="text-center">

## After (Aged)
<div class="ja-small">老化処理後</div>

<div>
  <video src="/after.mp4" controls class="w-full rounded-lg border-2 border-gray-400"></video>
</div>

<v-click>

<div class="mt-4 text-sm text-left">

- Elderly voice (lower, slower)
  <div class="ja-small">老人的な声（低い・ゆっくり）</div>
- Wrinkles and sagging
  <div class="ja-small">しわ・たるみのある表情</div>
- Lip-sync adjusted
  <div class="ja-small">リップシンク調整済み</div>

</div>

</v-click>

</div>
</div>

---
layout: default
---

# Future Work
<div class="ja-small">今後の課題</div>

<v-clicks>

## 1. Lip-sync Refinement
<div class="ja-small">1. リップシンクの精緻化</div>

- **Challenge**: Different speaker speeds between original and aged voice
  <div class="ja-small">課題：元音声と老化音声で話者速度が異なる</div>
- Current: Simple speech region detection + speed adjustment
  <div class="ja-small">現在：シンプルな有声区間検出+速度調整</div>
- Future: Word-level lip-sync mapping for better accuracy
  <div class="ja-small">今後：単語レベルのリップシンクマッピングでより高精度に</div>

## 2. Real-time Processing
<div class="ja-small">2. リアルタイム処理</div>

- Current: Offline video pipeline (~1-2 min processing time)
  <div class="ja-small">現在：オフライン動画処理（処理時間1-2分程度）</div>
- Future: Integration with Bruno's real-time system + real-time face aging
  <div class="ja-small">今後：Brunoさんのリアルタイムシステム統合+リアルタイム顔老化</div>

</v-clicks>

---
layout: default
---

# Future Work
<div class="ja-small">今後の課題</div>

<v-clicks>

## 3. User Study & Evaluation
<div class="ja-small">3. ユーザー評価</div>

- Measure awareness improvement before/after experience
  <div class="ja-small">体験前後での意識変化の測定</div>

</v-clicks>


---
layout: default
---

# Gesture Classification Framework
<div class="ja-small">ジェスチャー分類の理論的枠組み</div>

<v-clicks>

## Kendon's Continuum
<div class="ja-small">Kendonの連続体</div>

<div class="mt-4">

```mermaid
graph LR
    A[Gesticulation<br/>ジェスティキュレーション] --> B[Language-like<br/>言語的ジェスチャー]
    B --> C[Pantomime<br/>パントマイム]
    C --> D[Emblems<br/>エムブレム]
    D --> E[Sign Language<br/>手話]

    style A fill:#e3f2fd,stroke:#1976d2
    style B fill:#f3e5f5,stroke:#7b1fa2
    style C fill:#e8f5e9,stroke:#388e3c
    style D fill:#fff9c4,stroke:#f57f17
    style E fill:#ffccbc,stroke:#d84315
```

<div class="text-sm mt-2">
身体動作が言語的性質を帯びる度合いによる連続体 (Kendon, 2004)
</div>

</div>

</v-clicks>

<v-click>

<div class="mt-6 p-4 bg-yellow-50 rounded">

**分析の課題**: 言語的性質が低いほど、解析が困難になる
<div class="ja-small">Gesticulation（左側）は発話との関係が曖昧で、文脈依存的な分析が必要</div>

</div>

</v-click>

---
layout: default
---

# McNeill's Classification of Gestures
<div class="ja-small">McNeillのジェスチャー分類</div>

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="p-3 bg-blue-50 rounded">

### Iconic
<div class="ja-small">アイコニック</div>

<v-click>

- Depicts physical form or action
  <div class="ja-small">物体や動作の形状を模写</div>
- Example: Tracing spiral for "spiral staircase"
  <div class="ja-small">例：「螺旋階段」で螺旋を描く</div>

</v-click>

</div>

<div class="p-3 bg-purple-50 rounded">

### Metaphoric
<div class="ja-small">メタフォリック</div>

<v-click>

- Abstract concepts as physical forms
  <div class="ja-small">抽象概念を物理的形状で表現</div>
- Example: Timeline gesture (left to right)
  <div class="ja-small">例：時間の流れ（左→右）</div>

</v-click>

</div>

<div class="p-3 bg-green-50 rounded">

### Deictic
<div class="ja-small">デイクティック</div>

<v-click>

- Pointing to objects or locations
  <div class="ja-small">対象物や方向への指差し</div>
- Resolves references ("that", "there")
  <div class="ja-small">指示代名詞の内容を確定</div>

</v-click>

</div>

<div class="p-3 bg-yellow-50 rounded">

### Beat
<div class="ja-small">ビート</div>

<v-click>

- Rhythmic movements with speech
  <div class="ja-small">発話のリズムに合わせた動き</div>
- Emphasizes discourse structure
  <div class="ja-small">談話構造の強調</div>

</v-click>

</div>

</div>

<v-click>

<div class="mt-6 p-4 bg-gray-50 rounded text-sm">

**Growth Point Theory** (McNeill, 2005): Gesture and speech emerge simultaneously from the same mental representation
<div class="ja-small">成長点理論：ジェスチャーと発話は同一の思考単位から同時に分化する</div>

**Synchrony Rules**: Gesture stroke synchronizes with pitch accent, shares semantic/pragmatic function with speech
<div class="ja-small">同期規則：ストロークは強勢音節と同期し、発話と意味・語用論的機能を共有</div>

</div>

</v-click>

---
layout: default
---


<v-clicks>

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="p-4 bg-red-50 rounded border-2 border-red-400">

**Context-Gesture Disconnection**
<div class="ja-small">文脈とジェスチャーの紐付け困難</div>

- Existing methods analyze gestures in isolation
  <div class="ja-small">既存手法はジェスチャーを単独で分析</div>
- Cannot capture relationship with dialogue context
  <div class="ja-small">対話文脈との関係性を捉えられない</div>

</div>

<div class="p-4 bg-red-50 rounded border-2 border-red-400">

**Temporal Motion Analysis Gap**
<div class="ja-small">時系列モーション分析の欠如</div>

- Pose analysis methods exist
  <div class="ja-small">ポーズ分析手法は存在する</div>
- No established methods for temporal motion sequences
  <div class="ja-small">時系列モーションデータの分析手法は未確立</div>

</div>

</div>

</v-clicks>

<v-click>

<div class="mt-8 p-6 bg-green-50 rounded border-2 border-green-400">

## Our Objective
<div class="ja-small">本研究の目的</div>

**Develop a model that bridges context and motion, enabling systematic gesture analysis**
<div class="ja-small">文脈とモーションを紐付けるモデルを構築し、体系的なジェスチャー分析を可能にする</div>

</div>

</v-click>

---
layout: center
class: text-center
---

<div class="text-4xl font-bold mt-20">

Thank you for your attention
<div class="ja-small text-2xl mt-4">ご清聴ありがとうございました</div>

</div>

<div class="mt-16 text-xl text-gray-600">

Questions?
<div class="ja-small">質問はありますか？</div>

</div>
