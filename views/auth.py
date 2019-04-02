from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import jsonify
from flask import request

auth = Blueprint('auth', __name__)


@auth.route('/register')
def register():
    return render_template('blog/auth/register.html')


@auth.route('/api/v1/register', methods=['POST'])
def api_v1_register():
    return jsonify({
        'status': 0,
        'message': 'ok'
    })


# 登录接口
@auth.route('/api/v1/login', methods=['POST'])
def api_v1_login():

    data = request.get_json()

    username = data.get('username')
    if username is None or len(username) == 0:
        return jsonify({
            'status': 400,
            'message': 'Invalid params username',
            'data': data
        })

    password = data.get('password')
    if password is None or len(password) == 0:
        return jsonify({
            'status': 400,
            'message': 'Invalid params password',
            'data': data
        })

    return jsonify({
        'status': 0,
        'message': 'ok',
        'data': data
    })


# 登出视图
@auth.route('/logout')
def logout():
    return render_template('blog/auth/login.html')
