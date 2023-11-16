# Dockerfile

# ベースイメージを指定
FROM python:3.9

# 作業ディレクトリを設定
WORKDIR /app

# プロジェクトの依存関係をインストール
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクトフォルダをコピー
COPY . /app/

# Djangoアプリの起動コマンド
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
