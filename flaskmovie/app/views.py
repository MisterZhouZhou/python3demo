from flask import render_template
from . import app

@app.errorhandler(404)
def page_not_found(error):
    # 404
    return render_template('home/404.html'), 404