from flask import Flask
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()   # 如果是 POST 方法就执行登录操作
    else:
        show_the_login_form()   # 如果是 GET 方法就展示登录表单