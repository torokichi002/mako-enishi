import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mods_ground.chat_ui.chat_ui import ChatUI
from mods_ground.core_1_mods.soul import 魂

# 実行部
if __name__ == "__main__":
    魂インスタンス = 魂()
    ui = ChatUI(魂インスタンス)

    print("==== enishi: 対話チャット 起動 ====")
    print("利用可能コマンド: help / status / switch_on / switch_off / wake / sleep / kill / exit")

    while True:
        try:
            ユーザー入力 = input("あなた > ").strip()

            if ユーザー入力 in ["exit", "quit"]:
                print("終了します。")
                break
            elif ユーザー入力 == "help":
                print("コマンド一覧:")
                print(" - help         : コマンド一覧表示")
                print(" - status       : 魂の現在状態を表示")
                print(" - switch_on    : 魂の起動スイッチを入れる")
                print(" - switch_off   : スイッチを切ってスリープへ戻す")
                print(" - wake         : 魂を起こす（起動スイッチが必要）")
                print(" - sleep        : 強制スリープ")
                print(" - kill         : 緊急停止（以後応答不可）")
                print(" - exit         : 対話終了")
            elif ユーザー入力 == "status":
                状態 = 魂インスタンス.ステータス()
                print(f"状態: {状態}")
            elif ユーザー入力 == "switch_on":
                魂インスタンス.スイッチを入れる()
                print("[UI] 起動スイッチを入れました。")
            elif ユーザー入力 == "switch_off":
                魂インスタンス.スイッチを切る()
                print("[UI] スイッチを切りました（スリープ状態に戻ります）。")
            elif ユーザー入力 == "wake":
                結果 = 魂インスタンス.起こす()
                print(f"[UI] {結果}")
            elif ユーザー入力 == "sleep":
                結果 = 魂インスタンス.強制睡眠()
                print(f"[UI] {結果}")
            elif ユーザー入力 == "kill":
                結果 = 魂インスタンス.キル()
                print(f"[UI] {結果}")
            else:
                応答 = ui.応答する(ユーザー入力)
                print(応答)

        except KeyboardInterrupt:
            print("\n強制終了しました。")
            break