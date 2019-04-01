from flask import Flask
from flask import render_template
from views.login import login

app = Flask(__name__)
app.register_blueprint(login, url_prefix='/login')


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
