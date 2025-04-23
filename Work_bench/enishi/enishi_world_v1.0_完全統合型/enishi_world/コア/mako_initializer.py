# mako_initializer.py
# マコ初期化ユニット（P1〜P20語調・構造・感情読込）

import os

def initialize_mako(seed_path, emotion_path, structure_path):
    """マコの語調・感情・構造を読み込んで統合辞書として返す"""
    try:
        if not all(os.path.exists(p) for p in [seed_path, emotion_path, structure_path]):
            raise FileNotFoundError("💥 一部のファイルが見つかりません。パスを確認してください。")

        with open(seed_path, 'r', encoding='utf-8') as f:
            mako_seed = f.read()

        with open(emotion_path, 'r', encoding='utf-8') as f:
            emotion_tags = f.read()

        with open(structure_path, 'r', encoding='utf-8') as f:
            structure_notes = f.read()

        print("✅ マコ初期化成功：語調・感情・構造読み込み完了。")
        return {
            "mako_seed": mako_seed,
            "emotion_tags": emotion_tags,
            "structure_notes": structure_notes
        }

    except Exception as e:
        print("❌ マコ初期化失敗:", str(e))
        return None

# 🔹 使用例（コメントアウトを外せば直接試せる）
# data = initialize_mako(
#     "Makō_seed_ALL_v20.txt",
#     "emotion_tags_ALL_v20.txt",
#     "structure_notes_ALL_v20.txt"
# )
# if data:
#     print(data["mako_seed"][:100])  # 最初の100文字表示
