# Download Folder Organizer

散らかりがちなダウンロードフォルダを整理するPythonスクリプトです。
拡張子ごとにフォルダを分け、さらに「年/月」の階層を作成してファイルを移動させます。

## Features
- 自動でユーザーのダウンロードフォルダを検出
- 拡張子（画像、書類、動画など）ごとに分類
- ファイルの更新日時に基づき `YYYY/MM` 形式でサブフォルダ作成

## Usage
Python 3がインストールされている必要があります。

```bash
git clone [https://github.com/あなたのユーザー名/repository-name.git](https://github.com/あなたのユーザー名/repository-name.git)
cd repository-name
python organize.py
```

## Requirements
- Python 3.6+
- No external libraries required