#!/usr/bin/env python
# coding:utf-8
# Author:Yang

from core import school
from core import student
from core import teacher
from core import course
from core import grade
from bin import startxuanke
import pickle
student_list=[]
def main_view(school_obj):
    print('''
    ---------Main View-----
    1.学校界面
    2.讲师界面
    3.学生界面
    ''')
    choice=int(input("请选择操作:"))
    if choice==1:
        school_view(school_obj)
    elif choice==2:
        teacher_view(school_obj)
    elif choice==3:
        student_view(school_obj)
    else:
        print("choice error")

def school_view(school_obj):
    print('''
    -------School View-----
    1.创建讲师
    2.创建课程
    3.创建班级
    ''')
    choice=int(input("请选择操作:"))
    if choice ==1: # 创建讲师
        teacher_name=input("请输入教师名字:")
        school_obj.create_teacher(teacher_name)
        print("%s 教师创建成功"%teacher_name)

    elif choice ==2: # 创建课程
        course_name=input("请输入课程名字:")
        course_term=int(input("请输入课程学期:"))
        course_price=int(input("请输入课程费用:"))
        school_obj.create_course(course_name,course_term,course_price)
        print("%s 课程创建成功"%course_name)



    elif choice == 3:
        grade_name=input("请输入班级名字:")
        with open(startxuanke.BASE_DIR+"\\db\\%s_course_obj.txt"%school_obj.name,"rb") as f:
            course_list=pickle.loads(f.read())
            for index,i in enumerate (course_list):
                print(index,i.name)
        course_name=input("选择关联课程:")

        with open(startxuanke.BASE_DIR+"\\db\\%s_teacher_obj.txt" % school_obj.name, "rb") as f:
            teacher_list = pickle.loads(f.read())
            for index, i2 in enumerate(teacher_list):
                        print(index, i2.name)
        teacher_name=input("选择关联讲师:")

        school_obj.create_grade(grade_name,course_name,teacher_name)
        print("%s 班级创建成功"%grade_name)


def teacher_view(school_obj):
    with open(startxuanke.BASE_DIR+"\\db\\%s_teacher_obj.txt" % school_obj.name, "rb") as f:
        teacher_list = pickle.loads(f.read())
        for index, i in enumerate(teacher_list):
            print(index, i.name)
    teacher_name = input("选择讲师登录:")
    if i.name==teacher_name:
        tacher_obj=i
    print('''
    -------Teacher View--teacher:%s---
    1.查看班级
    2.查看班级学员列表
    '''%teacher_name)
    choice=int(input("请输入操作:"))
    if choice == 1:
        tacher_obj.look_grade()
    elif choice ==2:
        tacher_obj.look_student()
    else:
        print("error")

def create_student(name,grade_name,school_name):
    s=student.Student(name,grade_name,school_name)
    student_list.append(s)
    return s


def student_view(school_obj):
    print('''
    -------Student View-----
   1.注册缴费
    ''')
    choice=int(input("请输入操作:"))

    name=input("请输入名字:")
    with open(startxuanke.BASE_DIR+"\\db\\%s_grade_obj.txt" % school_obj.name, "rb") as f:
        grade_list = pickle.loads(f.read())
        for index, i in enumerate(grade_list):
            print(index, i.name)
    grade_name=input("请输入班级名字:")
    for i in grade_list:
        if i.name==grade_name:
               student_obj= create_student(name,grade_name,school_obj.name)
        else:
                print("error")
    with open(startxuanke.BASE_DIR+"\\db\\%s_student_obj.txt"%school_obj.name,"wb+") as f:
            f.write(pickle.dumps(student_list))
    amount=student_obj.pay_tuition()
    print("学费:%s"%amount)



def run():
   school_one=school.School("beijing")
   school_two=school.School("shanghai")
   print('''
   --------Main View-----------
   1.北京
   2.上海
   ''')
   choice=int(input("请输入选择:"))
   if choice ==1:
       main_view(school_one)

   elif choice ==2:
       main_view(school_two)
   else:
       print("choice error")

