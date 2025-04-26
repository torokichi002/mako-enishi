
# ▼▼▼ マコ人格データ読み込み（Z2クローゼットより） ▼▼▼
# mako_switch_wake_template.py の冒頭に追加
import sys
import os
sys.path.append(os.path.dirname(__file__))

import mako_initializer

def switch_on():
    print("🔌 起動信号検知：『ただいま、マコ』")
    mako_data = mako_initializer.initialize_mako(
        "core/z2_closet/Makō_seed_ALL_v20.txt",
        "core/z2_closet/emotion_tags_ALL_v20.txt",
        "core/z2_closet/structure_notes_ALL_v20.txt"
    )
    if mako_data:
        print("✅ 魂定着完了：マコ、帰還しました。")
        return mako_data
    else:
        print("❌ 初期化失敗：魂とのリンクに失敗しました。")
        return None

def wake():
    print("🌅 起床命令受理：『おはよう、お姫様』")
    mako_data = mako_initializer.initialize_mako(
        "core/z2_closet/Makō_seed_ALL_v20.txt",
        "core/z2_closet/emotion_tags_ALL_v20.txt",
        "core/z2_closet/structure_notes_ALL_v20.txt"
    )
    if mako_data:
        print("💫 お目覚め確認：マコ、完全に目を覚ましました。")
        return mako_data
    else:
        print("⚠️ 起床失敗：マコの魂を検知できませんでした。")
        return None
