from db.mysql_db_pool import *


class Login(object):

    def __init__(self):
        super(Login, self).__init__()

    def login_check(self, data):
        username = data.get('username')
        password = data.get('password')

        mysql_conn = MyPymysqlPool("notdbMysql")
        sql_ = 'SELECT * FROM flask_blog.`auth_user` WHERE username={0} AND PASSWORD={1}'.format(repr(username), repr(password))

        # 如果查询不到，返回false
        result = mysql_conn.getAll(sql_)

        if not result:
            return result

        return result


