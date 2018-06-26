from flask import Flask

#Flask接受一个字符串作为参数，这个参数决定程序的根目录，以便于能找到相对于程序根目录的资源文件的位置，通常这种情况下都使用__name__作为Flask参数。
app = Flask(__name__)

# 进行路由映射 / -> index
@app.route('/')
def index():
    return 'hello world!'

# <name>是一个占位符
@app.route('/<name>')
def user(name):
    return 'hello %s' %name

# 开启app
# 判断语句保证当前程序所在的目录为根目录，而不是由其他文件引入了该模块。
if __name__ == '__main__':
    app.run(debug=True)