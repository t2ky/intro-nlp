"""
DeBERTa-WRIME 感情分析デモ
HAI研究室 新人向けワークショップ
"""

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# 日本語フォントの設定
matplotlib.rcParams['font.family'] = ['Arial Unicode MS', 'Hiragino Sans', 'Yu Gothic', 'Meirio', 'Takao']

# 感情ラベル（英語と日本語）
EMOTIONS = ["joy", "sadness", "anticipation", "surprise", "anger", "fear", "disgust", "trust"]
EMOTIONS_JA = ["喜び", "悲しみ", "期待", "驚き", "怒り", "恐れ", "嫌悪", "信頼"]
EMOTION_ICONS = ["😊", "😢", "🤔", "😲", "😠", "😰", "🤢", "🤝"]


def load_model(model_name="neuralnaut/deberta-wrime-emotions"):
    """モデルとトークナイザーをロード"""
    print("📦 モデルをロード中...")
    print(f"   モデル名: {model_name}")

    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        print("✅ モデルのロード完了！")
        print(f"   出力次元: {model.config.num_labels} (Plutchikの8感情)")
        return tokenizer, model
    except Exception as e:
        print(f"❌ エラー: {e}")
        print("\nインターネット接続を確認してください。")
        print("初回実行時はモデルのダウンロードに数分かかります（約500MB）")
        raise


def predict_emotions(text, model, tokenizer):
    """テキストから8つの感情スコアを予測"""
    # トークン化
    inputs = tokenizer(text, return_tensors="pt", max_length=128, truncation=True, padding=True)

    # 推論（勾配計算不要）
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits.squeeze()

    # 0-1の範囲から0-3にデノーマライズ
    predictions = logits.cpu().numpy() * 3.0

    # 辞書形式で返す
    return {emotion: float(score) for emotion, score in zip(EMOTIONS, predictions)}


def print_emotions(text, emotions, top_n=3):
    """感情スコアをコンソールに表示"""
    print(f"\n{'='*70}")
    print(f"📝 テキスト: {text}")
    print('='*70)

    # スコアが高い順にソート
    sorted_emotions = sorted(emotions.items(), key=lambda x: x[1], reverse=True)

    print(f"\n感情スコア（上位{top_n}つ）:")
    for i, (emotion, score) in enumerate(sorted_emotions[:top_n], 1):
        idx = EMOTIONS.index(emotion)
        icon = EMOTION_ICONS[idx]
        ja = EMOTIONS_JA[idx]
        bar = "█" * int(score * 10)
        print(f"  {i}. {icon} {ja:6s} ({emotion:15s}): {score:.3f} {bar}")

    print("\n全感情スコア:")
    for emotion, score in sorted_emotions:
        idx = EMOTIONS.index(emotion)
        icon = EMOTION_ICONS[idx]
        ja = EMOTIONS_JA[idx]
        bar = "▪" * int(score * 15)
        print(f"  {icon} {ja:6s}: {score:.3f} {bar}")


def visualize_emotions(text, emotions, save_path=None):
    """感情スコアを棒グラフで可視化"""
    scores = [emotions[e] for e in EMOTIONS]

    fig, ax = plt.subplots(figsize=(12, 6))

    # 棒グラフ作成
    bars = ax.bar(range(len(EMOTIONS_JA)), scores, color='skyblue', edgecolor='navy', alpha=0.7)

    # 最大値を強調
    max_idx = scores.index(max(scores))
    bars[max_idx].set_color('orange')
    bars[max_idx].set_edgecolor('darkred')
    bars[max_idx].set_linewidth(2)

    # グラフの装飾
    ax.set_xlabel('感情', fontsize=12, fontweight='bold')
    ax.set_ylabel('感情スコア (0-3)', fontsize=12, fontweight='bold')
    ax.set_title(f'感情分析結果: {text}', fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(range(len(EMOTIONS_JA)))
    ax.set_xticklabels([f"{icon}\n{label}" for icon, label in zip(EMOTION_ICONS, EMOTIONS_JA)], fontsize=10)
    ax.set_ylim(0, 3)
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    # 値をバーの上に表示
    for i, (bar, score) in enumerate(zip(bars, scores)):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                f'{score:.2f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"\n💾 グラフを保存しました: {save_path}")

    plt.show()


def demo_mode(model, tokenizer):
    """デモモード: サンプルテキストで分析"""
    print("\n" + "="*70)
    print(" デモモード: サンプルテキストで感情分析")
    print("="*70)

    demo_texts = [
        "今日は最高の一日でした！",
        "明日のテストが心配で眠れない",
        "友達に裏切られて本当に悲しい",
        "新しいプロジェクトが始まってワクワクする",
        "締め切りに間に合わなくて焦っている",
        "合格したけど、友達が落ちて複雑な気持ち"
    ]

    for i, text in enumerate(demo_texts, 1):
        print(f"\n【サンプル {i}/{len(demo_texts)}】")
        emotions = predict_emotions(text, model, tokenizer)
        print_emotions(text, emotions)

        if i == 1:  # 最初のサンプルだけ可視化
            visualize_emotions(text, emotions)


def interactive_mode(model, tokenizer):
    """インタラクティブモード: ユーザー入力で分析"""
    print("\n" + "="*70)
    print(" インタラクティブモード: 自分でテキストを入力")
    print("="*70)
    print("感情を分析したいテキストを入力してください")
    print("（終了: 'quit', 可視化: 'viz'を末尾に追加）\n")

    while True:
        text = input("📝 テキスト: ")

        if text.lower() in ['quit', 'exit', 'q']:
            print("\n👋 終了します")
            break

        if not text.strip():
            continue

        # 可視化フラグのチェック
        visualize = False
        if text.lower().endswith(' viz') or text.lower().endswith(' v'):
            visualize = True
            text = text.rsplit(' ', 1)[0]

        emotions = predict_emotions(text, model, tokenizer)
        print_emotions(text, emotions)

        if visualize:
            visualize_emotions(text, emotions)

        print()


def challenge_mode(model, tokenizer):
    """チャレンジモード: 課題テキストで分析"""
    print("\n" + "="*70)
    print(" チャレンジモード: 実践課題")
    print("="*70)

    challenges = {
        "ポジティブ系": [
            "新しいプロジェクトが始まってワクワクする",
            "友達と久しぶりに会えて嬉しかった",
            "テストで満点を取れて最高の気分だ"
        ],
        "ネガティブ系": [
            "締め切りに間に合わなくて焦っている",
            "大事なものを失くして落ち込んでいる",
            "約束を破られて信じられない"
        ],
        "混合感情系": [
            "合格したけど、友達が落ちて複雑な気持ち",
            "引っ越しは楽しみだけど寂しさもある"
        ]
    }

    for category, texts in challenges.items():
        print(f"\n【{category}】")
        for i, text in enumerate(texts, 1):
            print(f"\n  課題 {i}: {text}")
            print("  予想: ", end="")
            input()  # ユーザーに予想を考えてもらう

            emotions = predict_emotions(text, model, tokenizer)
            sorted_emotions = sorted(emotions.items(), key=lambda x: x[1], reverse=True)

            print("  結果:")
            for emotion, score in sorted_emotions[:3]:
                idx = EMOTIONS.index(emotion)
                icon = EMOTION_ICONS[idx]
                ja = EMOTIONS_JA[idx]
                print(f"    {icon} {ja}: {score:.3f}")


def main():
    print("="*70)
    print(" DeBERTa-WRIME 感情分析システム")
    print(" HAI研究室 新人向けワークショップ")
    print("="*70)

    # モデルのロード
    try:
        tokenizer, model = load_model()
    except Exception:
        return

    # メニュー
    while True:
        print("\n" + "="*70)
        print("モードを選択してください:")
        print("  1. デモモード（サンプルテキストで分析）")
        print("  2. インタラクティブモード（自分で入力）")
        print("  3. チャレンジモード（実践課題）")
        print("  4. 終了")
        print("="*70)

        choice = input("\n選択 (1-4): ")

        if choice == '1':
            demo_mode(model, tokenizer)
        elif choice == '2':
            interactive_mode(model, tokenizer)
        elif choice == '3':
            challenge_mode(model, tokenizer)
        elif choice == '4':
            print("\n👋 終了します")
            break
        else:
            print("❌ 無効な選択です。1-4で選択してください。")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 終了します")
    except Exception as e:
        print(f"\n❌ エラーが発生しました: {e}")
        import traceback
        traceback.print_exc()
