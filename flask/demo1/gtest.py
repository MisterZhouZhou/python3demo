from flask import g
from flask import Flask

app = Flask(__name__)

@app.route('/test')
def test():
    return g.string

@app.before_first_request
def bf_first_request():
    g.string = 'before_first_request'


@app.before_request
def bf_request():
    g.string = 'before_request'


@app.after_request
def af_request(param):
    return param


if __name__ == '__main__':
    app.run(debug=True)