# ベースイメージとしてPython 3.9 Alpineを使用
FROM python:3.9-alpine

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係のファイルをコピー
COPY requirements.txt .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# main.pyを起動ポイントとして設定
CMD ["python", "main.py"]
