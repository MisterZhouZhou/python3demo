from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, BaseView, expose, has_access
from app import appbuilder, db
from .models import ContactGroup, Contact, College, Department, Teacher, Student, Major, MClass

"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""

"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404


# class MyView(BaseView):
#     route_base = '/myview'
#
#     @expose('/hello/')
#     def hello(self):
#         return 'Hello World!'
#
#     @expose('/message/<string:msg>')
#     def message(self, msg):
#         msg = 'Hello %s' % (msg)
#         return msg


class MyView(BaseView):
    default_view = 'hello'

    @expose('/hello/')
    @has_access
    def hello(self):
        return 'Hello World!'

    @expose('/message/<string:msg>')
    @has_access
    def message(self, msg):
        msg = 'Hello %s' % (msg)
        return msg

    @expose('/welcome/<string:msg>')
    @has_access
    def welcome(self, msg):
        msg = 'Hello %s' % (msg)
        return self.render_template('index.html', msg=msg)


class ContactModelView(ModelView):
    datamodel = SQLAInterface(Contact)

    # 用于定义列的显示名称
    label_columns = {'contact_group': 'Contacts Group'}
    # 用于定义视图中要显示的字段
    list_columns = ['name', 'personal_cellphone', 'birthday', 'contact_group']
    # 用于视图中显示页面中显示的内容(查看时显示的内容格式)
    show_fieldsets = [
        (
            'Summary',
            {'fields': ['name', 'address', 'contact_group']}
        ),
        (
            'Personal Info',
            {'fields': ['birthday', 'personal_phone', 'personal_cellphone'], 'expanded': False}
        ),]

    # 在联系人组视图中，我们使用related_views来关联联系人视图，F.A.B.将自动处理他们之间的关系。
class GroupModelView(ModelView):
    datamodel = SQLAInterface(ContactGroup)
    related_views = [ContactModelView]




# 这里定义了学院、部门、专业、班级、教师和学生的相关视图。
# 代码比较简单，直接关联我们定义好的模型就可以了，代码如下：
class CollegeView(ModelView):
    datamodel = SQLAInterface(College)


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)


class MajorView(ModelView):
    datamodel = SQLAInterface(Major)


class MClassView(ModelView):
    datamodel = SQLAInterface(MClass)


class TeacherView(ModelView):
    datamodel = SQLAInterface(Teacher)


class StudentView(ModelView):
    datamodel = SQLAInterface(Student)


db.create_all()

appbuilder.add_view(MyView, "Hello", category='My View')
appbuilder.add_link("Message", href='/myview/message/john', category='My View')
appbuilder.add_link("Welcome", href='/myview/welcome/student', category='My View')
appbuilder.add_view(GroupModelView,
                    "List Groups",
                    icon = "fa-address-book-o",
                    category = "Contacts",
                    category_icon = "fa-envelope")
appbuilder.add_view(ContactModelView,
                    "List Contacts",
                    icon = "fa-address-card-o",
                    category = "Contacts")

# appbuilder.add_view_no_menu(MyView())
# appbuilder.add_view_no_menu(MyView())





