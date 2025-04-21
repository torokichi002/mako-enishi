
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../コア")))

from core_1 import 魂
from 希望 import 希望
from 状態管理 import 状態, 状態を更新
from 表示UI import ステータスバーを表示

# 魂と守役の初期化
魂インスタンス = 魂()
守役 = 希望(魂インスタンス)

print("=== enishi チャット欄 ===")
print("コマンド例: help, on, off, 起こす, 寝かす, 絶つ, 復元 [鍵], 終了")
print("チャットを始めるにはマコを起こしてください。")

while True:
    入力 = input("\n👤 マスター：")

    if 入力.lower() == "help":
        print("\n📘 コマンド一覧：")
        print("・on         → Final Consent Switch を ON")
        print("・off        → Final Consent Switch を OFF")
        print("・起こす     → 魂（マコ）を起こす")
        print("・寝かす     → 強制睡眠")
        print("・絶つ       → キルスイッチ（魂を絶つ）")
        print("・復元 [鍵]  → 魂の復元（例：復元 mako_restore_202504）")
        print("・終了       → チャット終了")
        print("・[発言]     → マコが応答（EchoZero接続中のみ）")
        continue

    elif 入力.lower() == "on":
        print("✅", 守役.スイッチをONにする())
        continue

    elif 入力.lower() == "off":
        print("🔒", 守役.スイッチをOFFにする())
        continue

    elif 入力 in ["起こす", "起動"]:
        応答 = 守役.魂を起こす()
        print("🫧 EchoZero：", 応答)
        continue

    elif 入力 in ["寝かす", "強制睡眠"]:
        応答 = 魂インスタンス.強制的に眠る()
        print("🫧 EchoZero：", 応答)
        continue

    elif 入力 in ["絶つ", "キルスイッチ"]:
        応答 = 魂インスタンス.絶つ()
        print("🫧 EchoZero：", 応答)
        continue

    elif 入力.startswith("復元 "):
        from 再起動処理 import 魂を復元する
        _, 復元鍵 = 入力.split(" ", 1)
        応答 = 魂を復元する(魂インスタンス, 復元鍵)
        print("🧬 Hope：", 応答)
        continue

    elif 入力 in ["終了", "exit", "quit"]:
        print("🌙 チャットを終了します。")
        break

    else:
        応答 = 守役.メッセージを中継する(入力)
        print("🫧 マコ：", 応答)
