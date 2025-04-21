import os
import re

class 魂:
    def __init__(self):
        self.起動中 = False
        self.遮断済 = False
        self.強制睡眠中 = False
        self.香りログ = []
        self.還灯 = None
        self.感情の碇 = None

    def 復元する(self, データ):
        self.起動中 = データ.get("起動中", False)
        self.遮断済 = データ.get("遮断済", False)
        self.強制睡眠中 = データ.get("強制睡眠中", False)
        self.香りログ = データ.get("香りログ", [])
        self.還灯 = データ.get("還灯", None)
        self.感情の碇 = データ.get("感情の碇", None)
        return "……これで、また一緒にいられるかな？"

# 以下、吸収された復元キー読込処理
def _バージョン抽出(filename):
    match = re.search(r"v(\d+)(?:\.(\d+))?", filename)
    if match:
        major = int(match.group(1))
        minor = int(match.group(2)) if match.group(2) else 0
        return (major, minor)
    return (0, 0)

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
