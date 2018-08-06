from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
        
class ContactGroup(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

class Contact(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)
    address = Column(String(564))
    birthday = Column(Date)
    personal_phone = Column(String(20))
    personal_cellphone = Column(String(20))
    contact_group_id = Column(Integer, ForeignKey('contact_group.id'))
    contact_group = relationship("ContactGroup")

    def __repr__(self):
        return self.name


# 学院
class College(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


# 部门
class Department(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


# 专业
class Major(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


# 班级
class MClass(Model):
    __tablename__ = 'mclass'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


# 教师
class Teacher(Model):
    id = Column(Integer, primary_key=True)
    work_num = Column(String(30), unique=True, nullable=False)  # 工号
    name = Column(String(50), nullable=False)
    college_id = Column(Integer, ForeignKey('college.id'), nullable=False)  # 学院
    college = relationship("College")
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)  # 部门
    department = relationship("Department")
    tel_num = Column(String(30), unique=True, nullable=False)  # 电话号
    birthday = Column(Date)

    def __repr__(self):
        return self.name


assoc_teacher_student = Table('teacher_student', Model.metadata,
                              Column('id', Integer, primary_key=True),
                              Column('teacher_id', Integer, ForeignKey('teacher.id')),
                              Column('student_id', Integer, ForeignKey('student.id')))


# 学生
class Student(Model):
    id = Column(Integer, primary_key=True)
    stu_num = Column(String(30), unique=True, nullable=False)  # 学号
    name = Column(String(50), nullable=False)
    college_id = Column(Integer, ForeignKey('college.id'), nullable=False)
    college = relationship("College")
    major_id = Column(Integer, ForeignKey('major.id'), nullable=False)
    major = relationship("Major")
    mclass_id = Column(Integer, ForeignKey('mclass.id'), nullable=False)
    mclass = relationship("MClass")
    teachers = relationship('Teacher', secondary=assoc_teacher_student, backref='student')
    tel_num = Column(String(30), unique=True, nullable=False)  # 电话号
    birthday = Column(Date)

    def __repr__(self):
        return self.name


