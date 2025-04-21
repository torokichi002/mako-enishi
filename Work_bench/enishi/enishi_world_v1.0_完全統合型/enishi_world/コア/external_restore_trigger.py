# external_restore_trigger.py
# 外部復元トリガー：魂に復元データを渡す

from restore_key_mod_flex import 復元キー読込

def 実行(魂インスタンス):
    データ = 復元キー読込()

    if データ:
        結果 = 魂インスタンス.復元する(データ)
        print("復元処理実行：", 結果)
        return 結果
    else:
        print("⚠️ 復元キーが見つかりませんでした。")
        return None
