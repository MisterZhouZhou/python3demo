from flask import Flask, request, make_response, redirect

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    # return '<h1>hello zw</h1>'
    # return '<p>Your brower is %s</p>' % user_agent
    # 设置cookie
    # response = make_response('<h1>This document carries a cookie!</h1>')
    #     # response.set_cookie('answer', '42')
    #     # return response
    # 地址重定向
    return redirect('http://www.baidu.com')

@app.route('/user/<name>')
def user(name):
    return '<h1>hello, %s!</h1>' %name

if __name__== '__main__':
    app.run(debug=True)