from flask import Blueprint
from flask import render_template


login = Blueprint('login', __name__)


@login.route('/')
def index():
    return render_template('blog/login/login.html')
