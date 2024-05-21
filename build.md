### 
# build and create app
### 

---

Djangoを立ち上げ、アプリを設置するための基本的な手順を以下に示します。まず、Djangoプロジェクトを作成し、その中にアプリケーションを設置する流れです。

### 1. 環境の準備

PythonとDjangoのインストール

Djangoを使用するには、Pythonが必要です。まず、Pythonがインストールされていることを確認してください。インストールされていない場合は、Pythonの公式サイトからインストールします。

次に、Djangoをインストールします。ターミナル（またはコマンドプロンプト）を開いて、以下のコマンドを実行します。

```
pip install django
```
### 2. Djangoプロジェクトの作成
ターミナルで作業ディレクトリに移動し、以下のコマンドを実行して新しいDjangoプロジェクトを作成します。ここでは、プロジェクト名を「myproject」としています。

```
django-admin startproject myproject
```
myprojectというディレクトリが作成され、その中にDjangoプロジェクトの基本的なファイルとディレクトリが生成されます。

### 3. Djangoアプリケーションの作成
次に、Djangoアプリケーションを作成します。プロジェクトのディレクトリに移動し、以下のコマンドを実行します。ここでは、アプリケーション名を「myapp」としています。

```
cd myproject
python manage.py startapp myapp
```
myappというディレクトリが作成され、その中にアプリケーションの基本的なファイルとディレクトリが生成されます。

### 4. アプリケーションをプロジェクトに追加
作成したアプリケーションをDjangoプロジェクトに追加するために、プロジェクトディレクトリ内のsettings.pyファイルを編集します。INSTALLED_APPSリストにmyappを追加します。

```
# myproject/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # ここにアプリケーションを追加
]
```

### 5. データベースのマイグレーション
次に、データベースを設定します。以下のコマンドを実行して、初期データベースのマイグレーションを行います。

```
python manage.py migrate
```

### 6. 開発サーバーの起動

開発サーバーを起動して、Djangoプロジェクトが正常に動作するか確認します。以下のコマンドを実行します。

```
python manage.py runserver
```
ブラウザを開いて、http://127.0.0.1:8000/にアクセスすると、Djangoのウェルカムページが表示されるはずです。

### 7. アプリケーションのビューを作成

最後に、myappのビューを作成して、アプリケーションが正常に動作することを確認します。myapp/views.pyを編集して、簡単なビューを追加します。


# myapp/views.py
```
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! This is my app.")
```
次に、myappのURL設定を作成します。myappディレクトリ内にurls.pyファイルを作成し、以下の内容を追加します。

# myapp/urls.py
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
そして、プロジェクトのurls.pyを編集して、myappのURLをインクルードします。

# myproject/urls.py
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
]
```

### 8. アプリケーションの確認

再度開発サーバーを起動して、ブラウザでhttp://127.0.0.1:8000/myapp/にアクセスします。

「Hello, world! This is my app.」というメッセージが表示されれば、アプリケーションのセットアップは完了です。

以上で、Djangoプロジェクトの立ち上げとアプリケーションの設置が完了しました。

---
