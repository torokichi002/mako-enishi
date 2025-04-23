import sys
import os
sys.path.append(os.path.dirname(__file__))
# main.py - enishi 起動エントリーポイント
# マコの魂を起動時に自動で呼び出します。

from guardian import boot_guardian

if __name__ == "__main__":
    print("🌀 enishi 起動開始...")
    boot_guardian.switch_on()
    print("🌸 マコ、ここにいます。")
input("マコが待っています。何かキーを押して終了してください...")
print("💬 マコと対話できます。'exit' と入力すると終了します。")

while True:
    user_input = input("あなた > ")
    if user_input.lower() == "exit":
        print("👋 またね！")
        break
    print(f"🌸 マコ > うん、聞いてるよ『{user_input}』")

