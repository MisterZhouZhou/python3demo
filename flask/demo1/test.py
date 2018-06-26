from flask import Flask
from flask import render_template

class Myobj(object):
    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name

app = Flask(__name__)

@app.route('/')
def index():
    mydict = {'key1': '123', 'key': 'hello'}
    mylist = (123, 234, 345, 789)
    myintvar = 0
    myobj = Myobj('Hyman')
    return render_template('param.html', mydict=mydict, mylist=mylist, myintvar=0, myobj=myobj)

@app.route('/if')
def iftest():
    return render_template('iftest.html', user='zw')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/statictest')
def statictest():
    return render_template('statictest.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500


if __name__ == '__main__':
    app.run()