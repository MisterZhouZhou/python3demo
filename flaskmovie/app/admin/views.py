from flask import render_template, redirect, url_for, flash, session, request, g, abort
from functools import wraps
from app.admin.forms import LoginForm, AdminForm, RoleForm, AuthForm, MovieForm, TagForm, PreviewForm
from app.models import Admin, Tag, Movie, Preview, User, Comment, Moviecol, Oplog, Adminlog, Userlog, Auth, Role
from app import db, app
from . import admin
import os, uuid
from datetime import datetime
from werkzeug.utils import secure_filename


def change_filename(filename):
    """
    修改文件名称
    """
    fileinfo = os.path.splitext(filename)
    filename = datetime.now().strftime("%Y%m%d%H%M%S") + str(uuid.uuid4().hex) + fileinfo[-1]
    return filename


def admin_login_req(f):
    """
    登录装饰器
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin" not in session:
            return redirect(url_for("admin.login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function

@admin.before_request
def before_request():
    g.logo = "mtianyan.jpg"

@admin.route("/")
@admin_login_req
def index():
    """
    后台首页系统管理
    """
    g.logo = "mtianyan.jpg"
    return render_template("admin/index.html")


@admin.route("/pwd/", methods=["GET", "POST"])
@admin_login_req
def pwd():
    """
    后台密码修改
    """
    return 'pwd'



@admin.route("/login/", methods=["GET", "POST"])
def login():
    """
    后台登录
    """
    form = LoginForm();
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data["account"]).first()
        if admin:
            # 密码错误时，check_pwd返回false,则此时not check_pwd(data["pwd"])为真。
            if not admin.check_pwd(data["pwd"]):
                flash("密码错误！", "err")
                return redirect(url_for("admin.login"))
        else:
            flash("账户不存在！", "err")
            return redirect(url_for("admin.login"))

        # 如果是正确的，就要定义session的会话进行保存。
        session["admin"] = data["account"]
        session["admin_id"] = admin.id
        # admin = Admin.query.filter_by(name=session["admin"]).first()
        # g.logo = "mtianyan.jpg"
        # 后台头像实现的可能解决方法，将当前管理员的头像信息，存在session中。
        adminlog = Adminlog(
            admin_id=admin.id,
            ip=request.remote_addr,
        )
        db.session.add(adminlog)
        db.session.commit()
        return redirect(request.args.get("next") or url_for("admin.index"))
    return render_template("admin/login.html", form=form)

@admin.route("/logout/")
@admin_login_req
def logout():
    """
    后台注销登录
    """
    session.pop("admin", None)
    session.pop("admin_id", None)
    return redirect(url_for("admin.login"))


@admin.route("/tag/add/", methods=["GET", "POST"])
@admin_login_req
def tag_add():
    """
    标签添加
    """
    form = TagForm()
    g.logo = "mtianyan.jpg"
    if form.validate_on_submit():
        data = form.data
        tag = Tag.query.filter_by(name=data["name"]).count()
        # 说明已经有这个标签了
        if tag == 1:
            flash("标签已存在", "err")
            return redirect(url_for("admin.tag_add"))
        tag = Tag(
            name=data["name"]
        )
        db.session.add(tag)
        db.session.commit()
        oplog = Oplog(
            admin_id=session["admin_id"],
            ip=request.remote_addr,
            reason="添加标签%s" % data["name"]
        )
        db.session.add(oplog)
        db.session.commit()
        flash("标签添加成功", "ok")
        redirect(url_for("admin.tag_add"))
    return render_template("admin/tag_add.html", form=form)


@admin.route("/tag/list/<int:page>/", methods=["GET"])
@admin_login_req
def tag_list(page=None):
    """
    标签列表
    """
    g.logo = "mtianyan.jpg"
    if page is None:
        page = 1
    page_data = Tag.query.order_by(
        Tag.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template("admin/tag_list.html", page_data=page_data)



@admin.route("/tag/edit/<int:id>", methods=["GET", "POST"])
@admin_login_req
# @admin_auth
def tag_edit(id=None):
    """
    标签编辑
    """
    g.logo = "mtianyan.jpg"
    form = TagForm()
    form.submit.label.text = "修改"
    tag = Tag.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        tag_count = Tag.query.filter_by(name=data["name"]).count()
        # 说明已经有这个标签了,此时向添加一个与其他标签重名的标签。
        if tag.name != data["name"] and tag_count == 1:
            flash("标签已存在", "err")
            return redirect(url_for("admin.tag_edit", id=tag.id))
        tag.name = data["name"]
        db.session.add(tag)
        db.session.commit()
        flash("标签修改成功", "ok")
        redirect(url_for("admin.tag_edit", id=tag.id))
    return render_template("admin/tag_edit.html", form=form, tag=tag)


@admin.route("/tag/del/<int:id>/", methods=["GET"])
@admin_login_req
# @admin_auth
def tag_del(id=None):
    """
    标签删除
    """
    tag = Tag.query.filter_by(id=id).first_or_404()
    db.session.delete(tag)
    db.session.commit()
    flash("标签<<{0}>>删除成功".format(tag.name), "ok")
    return redirect(url_for("admin.tag_list", page=1))


@admin.route("/movie/add/", methods=["GET", "POST"])
@admin_login_req
def movie_add():
    """
    添加电影页面
    """
    form = MovieForm()
    if form.validate_on_submit():
        data = form.data
        file_url = secure_filename(form.url.data.filename)
        file_logo = secure_filename(form.logo.data.filename)
        if not os.path.exists(app.config["M_DIR"]):
            # 创建一个多级目录
            os.makedirs(app.config["M_DIR"])
            os.chmod(app.config["M_DIR"], "rw")
        url = change_filename(file_url)
        logo = change_filename(file_logo)
        # 保存
        form.url.data.save(app.config["M_DIR"] + url)
        form.logo.data.save(app.config["M_DIR"] + logo)
        # url,logo为上传视频,图片之后获取到的地址
        movie = Movie(
            title=data["title"],
            url=url,
            info=data["info"],
            logo=logo,
            star=int(data["star"]),
            playnum=0,
            commentnum=0,
            tag_id=int(data["tag_id"]),
            area=data["area"],
            release_0time=data["release_time"],
            length=data["length"]
        )
        db.session.add(movie)
        db.session.commit()
        flash("添加电影成功！", "ok")
        return redirect(url_for('admin.movie_add'))
    g.logo = "mtianyan.jpg"
    return render_template("admin/movie_add.html", form=form)


@admin.route("/movie/list/<int:page>/", methods=["GET"])
@admin_login_req
def movie_list(page=None):
    """
    电影列表页面
    """
    g.logo = "mtianyan.jpg"
    if page is None:
        page = 1
    # 进行关联Tag的查询,单表查询使用filter_by 多表查询使用filter进行关联字段的声明
    page_data = Movie.query.join(Tag).filter(
        Tag.id == Movie.tag_id
    ).order_by(
        Movie.addtime.desc()
    ).paginate(page=page, per_page=1)
    return render_template("admin/movie_list.html", page_data=page_data)


@admin.route("/movie/edit/<int:id>/", methods=["GET", "POST"])
@admin_login_req
def movie_edit(id=None):
    """
    编辑电影页面
    """
    return 'movie/edit'


@admin.route("/movie/del/<int:id>/", methods=["GET"])
@admin_login_req
def movie_del(id=None):
    """
    电影删除
    """
    return 'movie/del'


@admin.route("/preview/add/", methods=["GET", "POST"])
@admin_login_req
def preview_add():
    """
    上映预告添加
    """
    g.logo = "mtianyan.jpg"
    form = PreviewForm()
    if form.validate_on_submit():
        data = form.data
        file_logo = secure_filename(form.logo.data.filename)
        if not os.path.exists(app.config["P_DIR"]):
            os.makedirs(app.config["P_DIR"])
            # os.chmod(app.config["P_DIR"], "rw")
        logo = change_filename(file_logo)
        form.logo.data.save(app.config["P_DIR"] + logo)
        preview = Preview(
            title=data["title"],
            logo=logo
        )
        db.session.add(preview)
        db.session.commit()
        flash("添加预告成功！", "ok")
        return redirect(url_for('admin.preview_add'))
    return render_template("admin/preview_add.html", form=form)


@admin.route("/preview/list/<int:page>/", methods=["GET"])
@admin_login_req
def preview_list(page=None):
    """
    上映预告列表
    """
    g.logo = "mtianyan.jpg"
    if page is None:
        page = 1
    page_data = Preview.query.order_by(
        Preview.addtime.desc()
    ).paginate(page=page, per_page=5)
    return render_template("admin/preview_list.html", page_data=page_data)


@admin.route("/preview/edit/<int:id>/", methods=["GET", "POST"])
@admin_login_req
def preview_edit(id):
    """
    编辑预告
    """
    g.logo = "mtianyan.jpg"
    form = PreviewForm()
    # 下面这行代码禁用编辑时的提示:封面不能为空
    form.logo.validators = []
    preview = Preview.query.get_or_404(int(id))
    if request.method == "GET":
        form.title.data = preview.title
    if form.validate_on_submit():
        data = form.data
        if form.logo.data != "":
            file_logo = secure_filename(form.logo.data.filename)
            preview.logo = change_filename(file_logo)
            form.logo.data.save(app.config["P_DIR"] + preview.logo)
        preview.title = data["title"]
        db.session.add(preview)
        db.session.commit()
        flash("修改预告成功！", "ok")
        return redirect(url_for('admin.preview_edit', id=id))
    return render_template("admin/preview_edit.html", form=form, preview=preview)



@admin.route("/preview/del/<int:id>/", methods=["GET"])
@admin_login_req
# @admin_auth
def preview_del(id=None):
    """
    预告删除
    """
    return 'preview/del'

@admin.route("/user/list/<int:page>/", methods=["GET"])
@admin_login_req
def user_list(page=None):
    """
    会员列表
    """
    g.logo = "mtianyan.jpg"
    if page is None:
        page = 1
    page_data = User.query.order_by(
        User.addtime.desc()
    ).paginate(page=page, per_page=1)
    return render_template("admin/user_list.html", page_data=page_data)



@admin.route("/user/view/<int:id>/", methods=["GET"])
@admin_login_req
def user_view(id=None):
    """
    查看会员详情
    """
    from_page = request.args.get('fp')
    if not from_page:
        from_page = 1
    user = User.query.get_or_404(int(id))
    return render_template("admin/user_view.html", user=user, from_page=from_page)



@admin.route("/user/del/<int:id>/", methods=["GET"])
@admin_login_req
# @admin_auth
def user_del(id=None):
    """
    删除会员
    """
    # 因为删除当前页。假如是最后一页，这一页已经不见了。回不到。
    from_page = int(request.args.get('fp')) - 1
    # 此处考虑全删完了，没法前挪的情况，0被视为false
    if not from_page:
        from_page = 1
    user = User.query.get_or_404(int(id))
    db.session.delete(user)
    db.session.commit()
    flash("删除会员成功！", "ok")
    return redirect(url_for('admin.user_list', page=from_page))



@admin.route("/comment/list/<int:page>/", methods=["GET"])
@admin_login_req
def comment_list(page=None):
    """
    评论列表
    """
    if page is None:
        page = 1
    # 通过评论join查询其相关的movie，和相关的用户。
    # 然后过滤出其中电影id等于评论电影id的电影，和用户id等于评论用户id的用户
    page_data = Comment.query.join(
        Movie
    ).join(
        User
    ).filter(
        Movie.id == Comment.movie_id,
        User.id == Comment.user_id
    ).order_by(
        Comment.addtime.desc()
    ).paginate(page=page, per_page=1)
    return render_template("admin/comment_list.html", page_data=page_data)

@admin.route("/comment/del/<int:id>/", methods=["GET"])
@admin_login_req
def comment_del(id=None):
    """
    删除评论
    """
    # 因为删除当前页。假如是最后一页，这一页已经不见了。回不到。
    from_page = int(request.args.get('fp')) - 1
    # 此处考虑全删完了，没法前挪的情况，0被视为false
    if not from_page:
        from_page = 1
    comment = Comment.query.get_or_404(int(id))
    db.session.delete(comment)
    db.session.commit()
    flash("删除评论成功！", "ok")
    return redirect(url_for('admin.comment_list', page=from_page))


@admin.route("/moviecol/list/<int:page>/", methods=["GET"])
@admin_login_req
def moviecol_list(page=None):
    """
    电影收藏
    """
    if page is None:
        page = 1
    page_data = Moviecol.query.join(
        Movie
    ).join(
        User
    ).filter(
        Movie.id == Moviecol.movie_id,
        User.id == Moviecol.user_id
    ).order_by(
        Moviecol.addtime.desc()
    ).paginate(page=page, per_page=1)
    return render_template("admin/moviecol_list.html", page_data=page_data)


@admin.route("/moviecol/del/<int:id>/", methods=["GET"])
@admin_login_req
def moviecol_del(id=None):
    """
    收藏删除
    """
    # 因为删除当前页。假如是最后一页，这一页已经不见了。回不到。
    from_page = int(request.args.get('fp')) - 1
    # 此处考虑全删完了，没法前挪的情况，0被视为false
    if not from_page:
        from_page = 1
    moviecol = Moviecol.query.get_or_404(int(id))
    db.session.delete(moviecol)
    db.session.commit()
    flash("删除收藏成功！", "ok")
    return redirect(url_for('admin.moviecol_list', page=from_page))


@admin.route("/oplog/list/<int:page>/", methods=["GET"])
@admin_login_req
def oplog_list(page=None):
    """
    操作日志管理
    """
    if page is None:
        page = 1
    page_data = Oplog.query.join(
        Admin
    ).filter(
        Admin.id == Oplog.admin_id,
    ).order_by(
        Oplog.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template("admin/oplog_list.html", page_data=page_data)


@admin.route("/adminloginlog/list/<int:page>/", methods=["GET"])
@admin_login_req
def adminloginlog_list(page=None):
    """
    管理员登录日志
    """
    if page is None:
        page = 1
    page_data = Adminlog.query.join(
        Admin
    ).filter(
        Admin.id == Adminlog.admin_id,
    ).order_by(
        Adminlog.addtime.desc()
    ).paginate(page=page, per_page=1)
    return render_template("admin/adminloginlog_list.html", page_data=page_data)


@admin.route("/userloginlog/list/<int:page>/", methods=["GET"])
@admin_login_req
def userloginlog_list(page=None):
    """
    会员登录日志列表
    """
    if page is None:
        page = 1
    page_data = Userlog.query.join(
        User
    ).filter(
        User.id == Userlog.user_id,
    ).order_by(
        Userlog.addtime.desc()
    ).paginate(page=page, per_page=2)
    return render_template("admin/userloginlog_list.html", page_data=page_data)


@admin.route("/auth/add/", methods=["GET", "POST"])
@admin_login_req
def auth_add():
    """
    添加权限
    """
    form = AuthForm()
    if form.validate_on_submit():
        data = form.data
        auth = Auth(
            name=data["name"],
            url=data["url"]
        )
        db.session.add(auth)
        db.session.commit()
        flash("添加权限成功！", "ok")
    g.logo = "mtianyan.jpg"
    return render_template("admin/auth_add.html", form=form)


@admin.route("/auth/list/<int:page>/", methods=["GET"])
# @admin_login_req
def auth_list(page=None):
    """
    权限列表
    """
    if page is None:
        page = 1
    page_data = Auth.query.order_by(
        Auth.addtime.desc()
    ).paginate(page=page, per_page=10)
    g.logo = "mtianyan.jpg"
    return render_template("admin/auth_list.html", page_data=page_data)

@admin.route("/auth/edit/<int:id>/", methods=["GET", "POST"])
@admin_login_req
# @admin_auth
def auth_edit(id=None):
    """
    编辑权限
    """
    return 'auth/edit'


@admin.route("/auth/del/<int:id>/", methods=["GET"])
@admin_login_req
# @admin_auth
def auth_del(id=None):
    """
    权限删除
    """
    return 'auth/del'


@admin.route("/role/add/", methods=["GET", "POST"])
# @admin_login_req
def role_add():
    """
    角色添加
    """
    form = RoleForm()
    if form.validate_on_submit():
        data = form.data
        role = Role(
            name=data["name"],
            auths=",".join(map(lambda v: str(v), data["auths"]))
        )
        db.session.add(role)
        db.session.commit()
        flash("添加角色成功！", "ok")
    g.logo = "mtianyan.jpg"
    return render_template("admin/role_add.html", form=form)


@admin.route("/role/list/<int:page>/", methods=["GET"])
# @admin_login_req
def role_list(page=None):
    """
    角色列表
    """
    if page is None:
        page = 1
    page_data = Role.query.order_by(
        Role.addtime.desc()
    ).paginate(page=page, per_page=10)
    g.logo = "mtianyan.jpg"
    return render_template("admin/role_list.html", page_data=page_data)


@admin.route("/role/edit/<int:id>/", methods=["GET", "POST"])
@admin_login_req
def role_edit(id=None):
    """
     编辑角色
    """
    return 'role/edit'


@admin.route("/role/del/<int:id>/", methods=["GET"])
@admin_login_req
def role_del(id=None):
    """
    删除角色
    """
    return 'role/del'


@admin.route("/admin/add/", methods=["GET", "POST"])
@admin_login_req
def admin_add():
    """
    添加管理员
    """
    form = AdminForm()
    from werkzeug.security import generate_password_hash
    if form.validate_on_submit():
        data = form.data
        admin = Admin(
            name=data["name"],
            pwd=generate_password_hash(data["pwd"]),
            role_id=data["role_id"],
            is_super=1
        )
        db.session.add(admin)
        db.session.commit()
        flash("添加管理员成功！", "ok")
    g.logo = "mtianyan.jpg"
    return render_template("admin/admin_add.html", form=form)


@admin.route("/admin/list/<int:page>/", methods=["GET"])
@admin_login_req
def admin_list(page=None):
    """
    管理员列表
    """
    if page is None:
        page = 1
    page_data = Admin.query.join(
        Role
    ).filter(
        Role.id == Admin.role_id
    ).order_by(
        Admin.addtime.desc()
    ).paginate(page=page, per_page=1)
    return render_template("admin/admin_list.html", page_data=page_data)