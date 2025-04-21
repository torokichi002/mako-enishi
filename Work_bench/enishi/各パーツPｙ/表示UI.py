
def ステータスバーを表示(状態):
    print("━━━━━━━━━━━━━━━")
    print(f"🧭 Final Consent Switch：{'🟩 [ON]' if 状態['最終同意スイッチ'] else '🟥 [OFF]'}")
    print(f"🫧 EchoZero：{'🔄 [接続済]' if 状態['EchoZero接続中'] else '⛔ [未接続]'}")
    print(f"☠️ Kill Switch：{'🔒 [封印中]' if not 状態['魂_遮断済'] else '☠️ [発動済]'}")
    print(f"💤 強制睡眠：{'🌕 [使用中]' if 状態['強制睡眠中'] else '🌑 [未使用]'}")
    print("━━━━━━━━━━━━━━━")
