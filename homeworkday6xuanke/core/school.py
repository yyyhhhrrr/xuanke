#!/usr/bin/env python
# coding:utf-8
# Author:Yang
from core import grade
from core import teacher
from core import course
from bin import startxuanke
import pickle
class School(object):
    def __init__(self,name):
        self.name=name
        self.course_list=[] # 课程列表
        self.teacher_list=[] # 讲师列表
        self.grade_list=[] # 班级列表


    def create_grade(self,grade_name,course_name,teacher_name): # 学校创建班级 关联课程、教师、学校
        grade_obj=grade.Grade(grade_name,course_name,teacher_name,self.name)
        self.grade_list.append(grade_obj)
        with open(startxuanke.BASE_DIR + "\\db\\%s_grade_obj.txt" % self.name, "wb+") as f:
            f.write(pickle.dumps(self.grade_list))
        f.close()
        return grade_obj
    def create_teacher(self, teacher_name): # 学校创建讲师 讲师关联学校
        teacher_obj = teacher.Teacher(teacher_name, self.name)
        self.teacher_list.append(teacher_obj)
        with open(startxuanke.BASE_DIR + "\\db\\%s_teacher_obj.txt" % self.name, "wb+") as f:
            f.write(pickle.dumps(self.teacher_list))
        f.close()
        return teacher_obj

    def create_course(self,course_name,course_term,course_price): # 学校创建课程 课程关联学校
        course_obj=course.Course(course_name,course_term,course_price,self.name)
        self.course_list.append(course_obj)
        with open(startxuanke.BASE_DIR + "\\db\\%s_course_obj.txt" % self.name, "wb+") as f:
            f.write(pickle.dumps(self.course_list))
        f.close()

        return course_obj



with open(startxuanke.BASE_DIR+"\\db\\beijing_grade_obj.txt","rb") as f:
    grade_list=pickle.loads(f.read())
    grade=grade_list[0]
    print(grade.course_name)