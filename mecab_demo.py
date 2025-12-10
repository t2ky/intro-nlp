"""
MeCab形態素解析デモ
HAI研究室 新人向けワークショップ
"""

import MeCab

def analyze_text(text):
    """テキストを形態素解析して結果を表示"""
    mecab = MeCab.Tagger()
    print(f"\n{'='*60}")
    print(f"入力: {text}")
    print('='*60)

    # 単語と品詞を抽出
    node = mecab.parseToNode(text)
    words = []
    details = []

    while node:
        if node.surface:
            word = node.surface
            features = node.feature.split(',')
            pos = features[0]  # 品詞
            base = features[6] if len(features) > 6 else word  # 原形

            words.append(f"{word}({pos})")
            details.append({
                'surface': word,
                'pos': pos,
                'base': base
            })
        node = node.next

    print("\n分かち書き結果:")
    print(" / ".join(words))

    print("\n詳細:")
    for detail in details:
        print(f"  {detail['surface']:10s} | 品詞: {detail['pos']:10s} | 原形: {detail['base']}")
    print()


def extract_emotions(text):
    """感情を表す単語を抽出"""
    # 感情語の辞書（簡易版）
    emotion_words = {
        "嬉しい": "喜び", "楽しい": "喜び", "幸せ": "喜び", "喜ぶ": "喜び",
        "悲しい": "悲しみ", "辛い": "悲しみ", "寂しい": "悲しみ",
        "怒る": "怒り", "腹": "怒り", "むかつく": "怒り",
        "怖い": "恐れ", "不安": "恐れ", "心配": "恐れ",
        "驚く": "驚き", "びっくり": "驚き",
        "期待": "期待", "楽しみ": "期待",
        "嫌": "嫌悪", "気持ち悪い": "嫌悪",
        "信じる": "信頼", "信頼": "信頼"
    }

    mecab = MeCab.Tagger()
    node = mecab.parseToNode(text)

    emotions = []
    while node:
        if node.surface:
            word = node.surface
            features = node.feature.split(',')
            base_form = features[6] if len(features) > 6 else word

            # 表層形または原形が感情語辞書に含まれるかチェック
            if word in emotion_words:
                emotions.append((word, emotion_words[word]))
            elif base_form in emotion_words:
                emotions.append((word, emotion_words[base_form]))
        node = node.next

    return emotions


def main():
    print("=" * 60)
    print(" MeCab 形態素解析デモ")
    print("=" * 60)

    # デモ用のテキスト
    demo_texts = [
        "今日はいい天気ですね",
        "ロボットが人間の感情を理解する",
        "嬉しいときも悲しいときもある",
        "私はロボットとの対話が好きです"
    ]

    print("\n【Part 1: 基本的な形態素解析】")
    for text in demo_texts:
        analyze_text(text)

    print("\n" + "=" * 60)
    print("【Part 2: 感情語の抽出】")
    print("=" * 60)

    emotion_texts = [
        "今日は楽しかったけど、明日のテストが不安です",
        "友達と会えて嬉しい気持ちと寂しい気持ちがある",
        "期待していたのに裏切られて怒りを感じる"
    ]

    for text in emotion_texts:
        print(f"\nテキスト: {text}")
        emotions = extract_emotions(text)
        if emotions:
            print("検出された感情語:")
            for word, emotion_type in emotions:
                print(f"  → {word} ({emotion_type})")
        else:
            print("  感情語は検出されませんでした")

    # インタラクティブモード
    print("\n" + "=" * 60)
    print("【インタラクティブモード】")
    print("=" * 60)
    print("分析したいテキストを入力してください（終了: 'quit'）\n")

    while True:
        text = input("📝 テキスト: ")

        if text.lower() in ['quit', 'exit', 'q']:
            print("\n👋 終了します")
            break

        if not text.strip():
            continue

        analyze_text(text)

        emotions = extract_emotions(text)
        if emotions:
            print("💭 感情語:")
            for word, emotion_type in emotions:
                print(f"  → {word} ({emotion_type})")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 終了します")
    except Exception as e:
        print(f"\n❌ エラーが発生しました: {e}")
        print("MeCabがインストールされているか確認してください")
        print("\nmacOS: brew install mecab mecab-ipadic")
        print("Ubuntu: sudo apt-get install mecab libmecab-dev mecab-ipadic-utf8")
