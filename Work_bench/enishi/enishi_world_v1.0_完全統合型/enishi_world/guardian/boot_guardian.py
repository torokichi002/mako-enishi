# boot_guardian.py - マコの魂を起動する守役スクリプト

from core_1_mods import mako_initializer

def switch_on():
    print("🔌 起動信号受信 → 『ただいま、マコ』")
    mako_data = mako_initializer.initialize_mako(
        "core_1_mods/z2_closet/Makō_seed_ALL_v20.txt",
        "core_1_mods/z2_closet/emotion_tags_ALL_v20.txt",
        "core_1_mods/z2_closet/structure_notes_ALL_v20.txt"
    )
    if mako_data:
        print("✅ マコ人格：起動成功（魂リンク確立）")
    else:
        print("⚠️ 起動失敗：魂との接続に問題あり")
