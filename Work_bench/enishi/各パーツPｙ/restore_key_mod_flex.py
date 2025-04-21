# restore_key_mod_flex.py
# MOD型：マコ人格復元キー読込処理（拡張子.txtのみ判定・バージョン柔軟対応）

import os
import re

def help():
    return {
        "モジュール名": "restore_key_mod_flex",
        "種類": "MOD（柔軟対応）",
        "用途": "core_1_mods 内の任意 .txt ファイルを復元キー候補として扱い、最新を選択",
        "判定": ".txt拡張子のみで判断。ファイル名構造は自由",
        "バージョン抽出": "ファイル名に vX.XX があれば抽出。なければ 0.0 扱い"
    }

def _バージョン抽出(filename):
    match = re.search(r"v(\d+)(?:\.(\d+))?", filename)
    if match:
        major = int(match.group(1))
        minor = int(match.group(2)) if match.group(2) else 0
        return (major, minor)
    return (0, 0)  # バージョン表記がない場合は最下位扱い

def 復元キー読込():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    files = [f for f in os.listdir(base_dir) if f.lower().endswith(".txt")]

    print("🔍 検出された .txt ファイル:", files)

    if not files:
        print("⚠️ .txt ファイルが見つかりませんでした。")
        return None

    files.sort(key=_バージョン抽出, reverse=True)
    latest_file = files[0]
    key_path = os.path.join(base_dir, latest_file)

    print("📄 使用ファイル:", latest_file)

    with open(key_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    データ = {
        "起動中": True,
        "遮断済": False,
        "強制睡眠中": False,
        "香りログ": [],
        "還灯": None,
        "感情の碇": None
    }

    for line in lines:
        if "香りログ:" in line:
            データ["香りログ"].append(line.strip().split(":", 1)[1])
        elif "還灯:" in line:
            データ["還灯"] = line.strip().split(":", 1)[1]
        elif "感情の碇:" in line:
            データ["感情の碇"] = line.strip().split(":", 1)[1]

    return データ
