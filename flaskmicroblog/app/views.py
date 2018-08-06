from flask import render_template, redirect, flash, url_for
from app import app
from app.forms import LoginForm
from app.models import User

# @app.route('/')
# @app.route('/index')
# def index():
#     return "Hello World!"
#
# '''
#   返回html
# '''
# @app.route('/template')
# def template():
#     user = {'nickname': 'Miguel'}
#     return '''
#         <html>
#             <head>
#                 <title>Home Page</title>
#             </head>
#             <body>
#                 <h1>Hello, ''' + user['nickname'] +'''</h1>
#             </body>
#         </html>
#     '''
#
#
# @app.route('/template2')
# def template2():
#     user = {'nickname': 'Miguel'}
#     return render_template('index3.html',
#                            title='Home',
#                            user=user)
#
# # 列表模版
# @app.route('/template3')
# def template3():
#     user = {'nickname': 'Miguel'}  # fake user
#     posts = [  # fake array of posts
#         {
#             'author': {'nickname': 'John'},
#             'body': 'Beautiful day in Portland!'
#         },
#         {
#             'author': {'nickname': 'Susan'},
#             'body': 'The Avengers movie was so cool!'
#         }
#     ]
#     return render_template("index2.html",
#                            title='Home',
#                            user=user,
#                            posts=posts)


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])


@app.route('/user/<nickname>')
def user(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user == None:
        flash('User ' + nickname + ' not found.')
        return redirect(url_for('index'))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html',
                           user=user,
                           posts=posts)
