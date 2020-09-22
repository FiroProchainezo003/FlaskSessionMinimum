# Flask Session最小サンプル

## プロジェクトについて

このプロジェクトはFlaskで `session` を利用するための最小サンプルです。<br>
sessionへの追加、取得が可能です。

## プロジェクトの取得方法

クローンしてください。
```
git clone https://github.com/FiroProchainezo003/FlaskSessionMinimum
```

## 実行方法

### windows

```
# Cloneしたフォルダで
$ python3 -m vevn venv
$ venv\Scripts\activate
```

app.pyの`app.secreat_key`の右の値を追加します。

例)
app.secret_key = b'\x00l\x86\x90\xf3\xa4\x90\x80\xf8\x07\xf5\xdd\xa6\x14\xda$\xbdF=\xef\xba7\xb9\x82'

右の値は以下で取得可能です。

```
$ python
>>> import os
>>> os.urandom(24)
```

Flaskを実行します。
```
# 実行
$ python app.py
```

1. ブラウザから `http://localhost:5000/session_write/name` にアクセス<br>
   nameは好きな文字列を入れてください。
2. `http://localhost:5000/session_read` にアクセス<br>
   session_writeで指定した値を取得できます。

### linux

```
# Cloneしたフォルダで
$ python3 -m vevn venv
$ source venv/Scripts/activate
```

app.pyの`app.secreat_key`の右の値を追加します。

例)
app.secret_key = b'\x00l\x86\x90\xf3\xa4\x90\x80\xf8\x07\xf5\xdd\xa6\x14\xda$\xbdF=\xef\xba7\xb9\x82'

右の値は以下で取得可能です。

```
$ python
>>> import os
>>> os.urandom(24)
```

Flaskを実行します。
```
# 実行
$ python app.py
```

1. ブラウザから `http://localhost:5000/session_write/name` にアクセス<br>
   nameは好きな文字列を入れてください。
2. `http://localhost:5000/session_read` にアクセス<br>
   session_writeで指定した値を取得できます。

## pythonバージョン

```
$ flask --version
Python 3.8.3
Flask 1.1.2
Werkzeug 1.0.1
```

## Flaskがサポートしているバージョン

[Flask - 1.1.x Installation](https://flask.palletsprojects.com/en/1.1.x/installation/)

