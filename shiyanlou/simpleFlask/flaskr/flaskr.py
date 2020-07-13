# 导入所需模块和方法
import sqlite3
from flask import (Flask, render_template, g, flash, request, session, abort,
        redirect, url_for)

# 配置项
DATABASE = '/tmp/flaskr.db'
ENV = 'development'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# 此函数的返回值是 sqlite3.connect 方法的调用，也就是连接对象
# 这里之所以写一个函数，是因为后面的代码会多次用到连接对象
def db_conn():
    '''创建与数据库连接的对象
    '''

    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    '''此函数用于创建数据表，需要在 flask shell 里引入执行
    '''

    # db_conn 函数的返回值是 sqlite3.connect 方法的返回值
    # sqlite3.connect 方法的返回值是具有 __enter__ 和 __exit__ 两个特殊方法的上下文对象
    # 这个上下文对象也叫连接对象，它的存在就是和 sqlite3 数据库保持连接的标志
    # 其中 as 关键字后面的 conn 就是连接对象，该对象有一个 close 方法用于关闭连接
    # 此处使用 with 关键字处理 sqlite3.connect 方法的返回值
    # 使得 with 语句块内的代码运行完毕后自动执行连接对象 conn 的 close 方法关闭连接
    with db_conn() as conn:
        # app.open_resource 方法的返回值也是上下文对象
        # 这个上下文对象也叫 IO 包装对象，是文件读取到内存后的数据包
        # 此对象同样有一个 close 方法需要必须执行以关闭文件
        # 变量 f 就是 IO 包装对象，它的 read 方法的返回值是文件内容的二进制格式
        with app.open_resource('schema.sql') as f:
            # 连接对象 conn 的 cursor 方法的返回值是一个光标对象，用于执行 SQL 语句
            # 该光标对象通常使用 execute 执行 SQL 语句，参数为语句的字符串
            # 光标对象的 executescript 可以一次执行多个 SQL 语句
            # 参数为多个语句的二进制格式，多个语句通常写到一个文件里
            conn.cursor().executescript(f.read().decode())
        # 连接对象的 commit 方法用于提交之前执行 SQL 语句的结果到数据库
        # 因为有些语句执行后不会立即改动数据库
        #conn.commit()

# 创建应用
app = Flask(__name__)
# app.config 的 from_object 方法通常用于获取对象的属性以增加配置项
# 此处使用的参数为 __name__ ，也就是当前所在文件
# 结果就是读取当前所在文件中的所有变量，选择其中全大写的变量作为配置项
app.config.from_object(__name__)