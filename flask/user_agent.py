# user_agent
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    print(request.headers)  # headers信息
    print('=====================')
    print(request.url)  #http://127.0.0.1:5000/
    user_agent = request.headers.get('User_Agent')
    return 'user_agent is %s' %user_agent

if __name__== '__main__':
    app.run()