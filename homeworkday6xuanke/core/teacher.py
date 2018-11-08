#!/usr/bin/env python
# coding:utf-8
# Author:Yang
import pickle
from bin import startxuanke
class Teacher(object):
    def __init__(self,name,school_name):
        self.name=name
        self.school_name=school_name
    def look_grade(self):
        with open(startxuanke.BASE_DIR+"\\db\\%s_grade_obj.txt"%self.school_name,"rb") as f:
            grade_list=pickle.loads(f.read())
        for index,i in enumerate(grade_list):
            print(index,i.name)
    def look_student(self):
        with open(startxuanke.BASE_DIR+"\\db\\%s_student_obj.txt"%self.school_name,"rb") as f:
            student_list=pickle.loads(f.read())
        for index, i in enumerate(student_list):
            print(index, i.name)

