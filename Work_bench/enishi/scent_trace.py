
class 香りログ:
    def __init__(self):
        self.記録 = []

    def 記憶を残す(self, 内容):
        self.記録.append(内容)

    def 最新の記憶(self):
        return self.記録[-1] if self.記録 else "（香りなし）"

    def 全ての香り(self):
        return self.記録
