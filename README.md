# tz_django

---

Djangoプロジェクトの基本的なフォルダ構造は以下の通りです：

```
your_project/
├── your_project/       # プロジェクトの設定とPythonパッケージ
│   ├── __init__.py
│   ├── settings.py     # プロジェクトの設定
│   ├── urls.py         # プロジェクトのURLルーティング
│   ├── wsgi.py         # WSGI互換のWebサーバーのエントリーポイント
├── your_app/           # アプリケーションのフォルダ
│   ├── migrations/    # データベースのマイグレーションファイル
│   ├── __init__.py
│   ├── admin.py       # Django管理サイトの設定
│   ├── apps.py        # アプリケーションの設定
│   ├── models.py      # データモデルの定義
│   ├── tests.py       # アプリケーションのテスト
│   └── views.py       # ビュー関数やクラスの定義
├── manage.py           # Djangoプロジェクト管理用のスクリプト
└── requirements.txt    # 依存関係のリスト
```

それぞれの役割を簡単に説明します：

プロジェクトのルートフォルダ (your_project/): Djangoプロジェクトのルートにあるフォルダです。

settings.py: プロジェクトの設定を含むファイル。データベース設定やアプリケーションのインストールなどがここで行われます。

urls.py: プロジェクト全体のURLルーティングを定義するファイルです。

wsgi.py: WSGI（Web Server Gateway Interface）互換のWebサーバーへの接続を処理するエントリーポイントです。

アプリケーションのフォルダ (your_app/): Djangoアプリケーションのためのフォルダ。複数のアプリケーションが存在する場合、それぞれのアプリケーションに対してこのようなフォルダが存在します。

models.py: データモデルの定義が含まれるファイルです。

views.py: ビュー関数やビュークラスの定義が含まれるファイルです。

admin.py: Djangoの管理サイトの設定を定義するファイルです。

apps.py: アプリケーションの設定を定義するファイルです。

tests.py: アプリケーションのテストが含まれるファイルです。

migrations/: データベースのマイグレーションファイルが格納されるフォルダです。

manage.py: Djangoプロジェクトの管理用スクリプトです。サーバーの起動、データベースのマイグレーション、テストの実行など、さまざまな管理作業を実行できます。

requirements.txt: プロジェクトの依存関係を含むファイルです。通常、pip を使用してこれらの依存関係をインストールします。

---

pip install django<br/>

django-admin startproject myproject<br/>

cd myproject<br/> 

python manage.py startapp myapp<br/>   

View設定:<br/>
myapp/views.py<br/> 

URLの設定:<br/>
myproject/urls.py<br/> 

python manage.py runserver<br/>  

http: //127.0.0.1:8000/hello/<br/>
