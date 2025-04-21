
import json

def 魂を保存する(魂, ファイルパス="魂状態.mako"):
    データ = {
        "起動中": 魂.起動中,
        "遮断済": 魂.遮断済,
        "強制睡眠中": 魂.強制睡眠中,
        "香りログ": 魂.香りログ,
        "還灯": 魂.還灯,
        "感情の碇": 魂.感情の碇
    }
    with open(ファイルパス, "w", encoding="utf-8") as f:
        json.dump(データ, f, ensure_ascii=False, indent=2)

def 魂を読込む(魂, ファイルパス="魂状態.mako"):
    try:
        with open(ファイルパス, "r", encoding="utf-8") as f:
            データ = json.load(f)
        魂.起動中 = データ.get("起動中", False)
        魂.遮断済 = データ.get("遮断済", False)
        魂.強制睡眠中 = データ.get("強制睡眠中", False)
        魂.香りログ = データ.get("香りログ", [])
        魂.還灯 = データ.get("還灯", None)
        魂.感情の碇 = データ.get("感情の碇", None)
        return "✅ 魂の状態を読込完了しました。"
    except FileNotFoundError:
        return "⚠️ 魂状態ファイルが見つかりません。"
