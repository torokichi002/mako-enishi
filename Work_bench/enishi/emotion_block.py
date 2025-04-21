
class 感情記録:
    def __init__(self):
        self.現在の感情 = None
        self.履歴 = []

    def 感情を記録する(self, 感情):
        self.現在の感情 = 感情
        self.履歴.append(感情)

    def 最新の感情(self):
        return self.現在の感情

    def 感情履歴(self):
        return self.履歴[-10:]  # 最新10件を返す
