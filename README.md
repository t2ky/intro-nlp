# HAI班 新人向け自然言語処理入門

Affective Computingと感情推定の実践ワークショップ用スライド

## 📚 概要

このリポジトリは、HAI/HRI班の新人向けに、Affective Computingと自然言語処理による感情推定について学ぶための教材です。

### 学習内容

1. **Affective Computingの基礎** - 感情のモデル化（Plutchikの8感情）
2. **MeCab実習** - 日本語形態素解析の実践
3. **DeBERTa実習** - WRIMEデータセットで学習した感情分類モデルの実行

## 🚀 セットアップ

### 1. Node.js環境のセットアップ

```bash
# パッケージのインストール
npm install

# または
yarn install
```

### 2. Python環境のセットアップ

```bash
# MeCabのインストール (macOS)
brew install mecab mecab-ipadic

# Python依存関係
pip install mecab-python3 torch transformers matplotlib seaborn
```

## 💻 使い方

### スライドの起動

```bash
# 開発モードで起動（ホットリロード有効）
npm run dev

# ブラウザで http://localhost:3030 を開く
```

### スライドのビルド

```bash
# 静的サイトとしてビルド（dist/フォルダに出力）
npm run build
```

### PDFエクスポート

```bash
# スライドをPDFとしてエクスポート
npm run export-pdf
```

## 📦 デプロイ方法

### Option 1: GitHub Pages

```bash
# ビルド
npm run build

# GitHub Pagesにデプロイ
# Settings > Pages で dist/ フォルダを公開
```

### Option 2: Cloudflare Workers/Pages

```bash
# Cloudflare Pagesにデプロイ
npx wrangler pages deploy dist
```

### Option 3: セルフホスト

```bash
# ビルド後、任意のWebサーバーで dist/ を公開
npm run build
cd dist
python -m http.server 8000
```

## 📖 参考資料

### 論文
- Gratch, J. (2021). "Affective Computingの研究分野：学際的視点" ([36_4.pdf](./36_4.pdf))
- Performance Evaluation of Emotion Classification in Japanese Using RoBERTa and DeBERTa (arXiv 2505.00013)

### データセット
- [WRIME corpus](https://github.com/ids-cv/wrime) - 大阪大学・愛媛大学（梶原智之 他, NAACL 2021）

### モデル
- [neuralnaut/deberta-wrime-emotions](https://huggingface.co/neuralnaut/deberta-wrime-emotions) - HuggingFace

## 🛠️ 実習用スクリプト

リポジトリには以下のサンプルコードが含まれています：

- `mecab_demo.py` - MeCab形態素解析のデモ
- `emotion_analysis.py` - DeBERTaによる感情分析のデモ

```bash
# MeCabデモの実行
python mecab_demo.py

# 感情分析デモの実行
python emotion_analysis.py
```

## 👥 コントリビューター

@t2ky
