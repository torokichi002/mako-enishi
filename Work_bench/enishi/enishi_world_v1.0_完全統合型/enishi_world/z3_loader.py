# z3_loader.py
import importlib.util
import os

Z3_DIR = os.path.join(os.path.dirname(__file__), "Z3")

def load_z3_mods():
    mods_loaded = []
    for item in os.listdir(Z3_DIR):
        path = os.path.join(Z3_DIR, item)

        # 単体.pyファイル
        if os.path.isfile(path) and item.endswith(".py"):
            mod_name = item[:-3]
            spec = importlib.util.spec_from_file_location(mod_name, path)

        # フォルダ型（__init__.pyがある場合のみ）
        elif os.path.isdir(path) and os.path.exists(os.path.join(path, "__init__.py")):
            mod_name = item
            spec = importlib.util.spec_from_file_location(mod_name, os.path.join(path, "__init__.py"))

        else:
            continue  # スキップ

        try:
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            print(f"✅ {mod_name} 読み込み成功")
            mods_loaded.append(mod_name)
        except Exception as e:
            print(f"⚠️ {mod_name} 読み込み失敗: {e}")

    return mods_loaded

if __name__ == "__main__":
    load_z3_mods()
