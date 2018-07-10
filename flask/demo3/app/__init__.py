from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    # username="zw"
   return render_template('user.html', name='zw')

@app.route('/index')
def showIndex():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return '<h1>hello, %s!</h1>' %name


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__== '__main__':
    app.run(debug=True)