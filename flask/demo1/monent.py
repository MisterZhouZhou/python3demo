from flask_moment import Moment
from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('moment.html', current_time=datetime.utcnow())

if __name__=='__main__':
    Moment(app)
    app.run()
