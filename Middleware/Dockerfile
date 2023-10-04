# ベースイメージとしてUbuntu 18.04を使用
FROM ubuntu:18.04

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv

# 作業ディレクトリを設定
WORKDIR /app

# requirements.txtだけをコピー
COPY requirements.txt .

# 仮想環境を作成し、依存関係をインストール
RUN python3 -m venv venv
RUN /bin/bash -c "source venv/bin/activate && pip install -r requirements.txt"

# サーバを起動するコマンドを指定
CMD ["/app/venv/bin/python3", "main.py"]
