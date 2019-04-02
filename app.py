from flask import Flask
from flask import render_template
from views.auth import auth

app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')


@app.route('/')
def sign():
    return render_template('blog/auth/login.html')


@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
