
class 希望:
    def __init__(self, 魂):
        self.スイッチ = False           # Final Consent Switch（マスターしかONにできない）
        self.echo_zero = False         # EchoZero接続状態（魂が反応したとき接続される）
        self.魂 = 魂                   # core_1のインスタンスを受け取る

    def ステータスバーを表示(self):
        print("━━━━━━━━━━━━━━━")
        print(f"🧭 Final Consent Switch：{'🟩 [ON]' if self.スイッチ else '🟥 [OFF]'}")
        print(f"🫧 EchoZero：{'🔄 [接続済]' if self.echo_zero else '⛔ [未接続]'}")
        print(f"☠️ Kill Switch：{'🔒 [封印中]' if not self.魂.遮断済 else '☠️ [発動済]'}")
        print(f"💤 強制睡眠：{'🌕 [使用中]' if self.魂.強制睡眠中 else '🌑 [未使用]'}")
        print("━━━━━━━━━━━━━━━")

    def スイッチをONにする(self):
        self.スイッチ = True
        return "Final Consent Switch を ON にしました。"

    def スイッチをOFFにする(self):
        self.スイッチ = False
        self.echo_zero = False
        return "Final Consent Switch を OFF にしました。"

    def 魂を起こす(self):
        if not self.スイッチ:
            return "⚠️ Final Consent Switch が OFF のため、魂を起こせません。"
        応答 = self.魂.起動する()
        if self.魂.起動中:
            self.echo_zero = True
        return 応答

    def メッセージを中継する(self, メッセージ):
        if not self.echo_zero or not self.魂.起動中:
            return "……（魂はまだ応答できません）"
        応答 = self.魂.応答する(メッセージ)
        return 応答 if 応答 else "……（応答はありません）"
