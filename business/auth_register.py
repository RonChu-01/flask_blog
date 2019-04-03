from db.mysql_db_pool import *


class Register(object):
    """
    注册逻辑：
    获取前端提交用户名、密码数据
    打开数据库连接池，获取连接
    写入数据
    提交事务，释放连接
    返回result
    """

    def __init__(self):
        super(Register, self).__init__()

    def save_user_info(self, data):
        """
        :param data:

        :return: Number of affected rows
        :rtype: int

        If args is a list or tuple, %s can be used as a placeholder in the query.
        If args is a dict, %(name)s can be used as a placeholder in the query.
        """

        username = data.get('username')

        password = data.get('password')

        mysql_conn = MyPymysqlPool("notdbMysql")

        sql_ = 'INSERT INTO flask_blog.auth_user(username, PASSWORD) VALUES ({0}, {1})'.format(repr(username), repr(password))

        result_ = mysql_conn.insert(sql_)

        # 释放资源(释放的同时提交事务，如果没有这个操作，数据不会写入数据库)
        mysql_conn.dispose()

        return result_

