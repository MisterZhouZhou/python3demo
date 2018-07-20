from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import Mail
# from datetime import datetime
# from nameForm import NameForm
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # 附加路由和自定义的错误页面
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app




# @app.route('/')
# def index():
#     # username="zw"
#    return render_template('user.html', name='zw')
#
# # index
# @app.route('/index')
# def showIndex():
#     return render_template('index.html', current_time=datetime.utcnow())
#
# # 表单
# @app.route('/form', methods=['GET','POST'])
# def showForm():
#     form = NameForm()
#     if form.validate_on_submit():
#         old_name = session.get('name')
#         if old_name is not None and old_name != form.name.data:
#             flash('Looks like you have changed your name!')
#         session['name'] = form.name.data
#         return redirect(url_for('showForm'))
#     return render_template('form.html', form=form, name=session.get('name'))
#
#
# @app.route('/user/<name>')
# def user(name):
#     return '<h1>hello, %s!</h1>' %name
#
#
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404


# if __name__== '__main__':
#     app.run(debug=True)