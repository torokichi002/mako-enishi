import os

legacy_artifacts = [
    "mod_ui.py", "hope_initializer.py", "view_ui.py", "logs_ui.py",
    "hope_thread_manager.py", "hope_emotion_bridge.py",
    "legacy_emotion_dict.txt", "hope_structure_notes.txt"
]

def run_check_multiple(base_paths):
    found = False
    for base_path in base_paths:
        print(f"\n🔎 チェック中: {base_path}")
        for root, dirs, files in os.walk(base_path):
            for artifact in legacy_artifacts:
                if artifact in files:
                    full_path = os.path.join(root, artifact)
                    print(f"⚠️ 残留構造検出：{full_path}")
                    found = True

    if not found:
        print("\n✅ クリーンです！Hope系構造は見つかりませんでした。")
    else:
        print("\n🧼 整合性を保つには、退避・削除を検討してください。")

if __name__ == "__main__":
    run_check_multiple([
        "core_1_mods",
        "mods_ground",
        "guardian",
        "コア"
    ])
