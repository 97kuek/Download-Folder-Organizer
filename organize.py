import os
import shutil
from pathlib import Path
from datetime import datetime

# ==========================================
# 設定エリア
# ==========================================

# ★修正点: 実行したユーザーの「ダウンロード」フォルダを自動取得
# (WindowsでもMacでも動作します)
TARGET_DIR = Path.home() / "Downloads"

# もし別の場所を指定したい場合は、ここを書き換えてください
# TARGET_DIR = Path(r"C:\Users\User\Desktop\Target") 

# 仕分けルール
EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv", ".epub"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Audio": [".mp3", ".wav", ".aac", ".m4a"],
    "Video": [".mp4", ".mov", ".avi", ".mkv"],
    "Programs": [".exe", ".msi", ".dmg", ".pkg", ".py", ".html", ".js", ".css"],
}
# ※ブログ公開用にフォルダ名を英語(Imagesなど)にしておくと、
# 海外の人も見やすくなりますが、日本語のままでもOKです。

# ==========================================
# プログラム本体
# ==========================================

def organize_files():
    target_path = Path(TARGET_DIR)

    if not target_path.exists():
        print(f"Directory not found: {target_path}")
        return

    print(f"Scanning: {target_path}")

    for item in target_path.iterdir():
        if item.is_file() and not item.name.startswith('.'):
            # 自分自身（organize.py）は移動しないようにガード
            if item.name == Path(__file__).name:
                continue

            file_ext = item.suffix.lower()
            
            for folder_name, ext_list in EXTENSIONS.items():
                if file_ext in ext_list:
                    # 更新日時から 年/月 を取得
                    mtime = item.stat().st_mtime
                    dt = datetime.fromtimestamp(mtime)
                    year_str = dt.strftime('%Y')
                    month_str = dt.strftime('%m')

                    # 階層: カテゴリ / 年 / 月
                    dest_folder = target_path / folder_name / year_str / month_str
                    
                    dest_folder.mkdir(parents=True, exist_ok=True)
                    dest_file = dest_folder / item.name

                    try:
                        if not dest_file.exists():
                            shutil.move(str(item), str(dest_file))
                            print(f"Moved: {item.name}")
                    except Exception as e:
                        print(f"Error: {e}")
                    
                    break 

if __name__ == "__main__":
    organize_files()