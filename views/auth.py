from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import jsonify
from flask import request

from business.auth_register import Register
from business.auth_login import Login
from time import sleep

auth = Blueprint('auth', __name__)


# 注册视图
@auth.route('/register')
def register():
    return render_template('blog/auth/register.html')


# 注册接口
@auth.route('/api/v1/register', methods=['POST'])
def api_v1_register():

    data = request.get_json()

    # 用户名校验
    username = data.get('username')
    if username is None or len(username) == 0:
        return jsonify({
            'status': 400,
            'message': 'Invalid params username',
            'data': data
        })

    # 密码校验
    password = data.get('password')
    if password is None or len(password) == 0:
        return jsonify({
            'status': 400,
            'message': 'Invalid params password',
            'data': data
        })

    # return jsonify({
    #     'status': 0,
    #     'message': 'ok',
    #     'data': ''
    # })

    # 处理逻辑（处理逻辑在专门的文件进行）
    try:
        runner = Register()
        result = runner.save_user_info(data)

        if result == 1:

            return jsonify({
                'status': 0,
                'message': 'ok',
                'data': ''
            })

        else:

            return jsonify({
                'status': 1,  # 状态码：1 注册失败
                'message': 'fail',
                'data': result
            })

    except Exception as e:
        return jsonify({
            'status': 500,
            'message': '内部错误',
            'data': ''
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

    runner = Login()
    result = runner.login_check(data)
    if not result:
        return jsonify({
            'status': 2,  # 状态码：2 表示用户名或密码错误
            'message': '用户名或密码错误！',
            'data': result
        })

    return jsonify({
        'status': 0,
        'message': 'ok',
        'data': ''
    })


# 登出视图
@auth.route('/logout')
def logout():
    return render_template('blog/auth/login.html')
