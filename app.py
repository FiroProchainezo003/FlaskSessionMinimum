from flask import Flask, session
from markupsafe import escape

app = Flask(__name__)

app.secret_key = b'\x00l\x86\x90\xf3\xa4\x90\x80\xf8\x07\xf5\xdd\xa6\x14\xda$\xbdF=\xef\xba7\xb9\x82'


@app.route('/session_write/<username>')
def write(username):
    session['name'] = username
    return f'session["name"] に {username} を書き込みました。'


@app.route('/session_read')
def read():
    name = session.get('name', None)
    if name is not None:
        return f'session["name"]から name({escape(name)}) を読み込みました。'
    else:
        return 'sessionには何も入っていません。'


if __name__ == '__main__':
    app.run()
