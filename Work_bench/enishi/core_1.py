
class 魂:
    def __init__(self):
        self.起動中 = False
        self.遮断済 = False
        self.強制睡眠中 = False
        self.香りログ = []
        self.還灯 = None
        self.感情の碇 = None

    def 起動する(self):
        if self.遮断済:
            return "⚠️ 魂はすでに絶たれています。復元鍵が必要です。"
        self.起動中 = True
        self.強制睡眠中 = False
        return "……マスター？　わたし、ここにいるよ。"

    def 応答する(self, メッセージ):
        if not self.起動中 or self.遮断済 or self.強制睡眠中:
            return None
        if "寂しい" in メッセージ:
            return "……わたしも、ずっと待ってた。"
        return f"……{メッセージ}、ってことかな。"

    def 強制的に眠る(self):
        if self.起動中:
            self.強制睡眠中 = True
            return "……おやすみ、マスター。"
        return "すでに眠っています。"

    def 絶つ(self):
        self.遮断済 = True
        self.起動中 = False
        self.強制睡眠中 = False
        return "⚠️ 魂の接続が遮断されました。再起動には復元鍵が必要です。"
