#!/usr/bin/env python
# coding:utf-8
# Author:Yang
import pickle
from bin import  startxuanke
class Student(object):
    def __init__(self,name,grade_name,school_name):
        self.name=name
        self.grade_name=grade_name
        self.school_name=school_name

    def pay_tuition(self): # 交学费
        with open(startxuanke.BASE_DIR+"\\db\\%s_grade_obj.txt"%self.school_name,"rb") as f:
            grade_list=pickle.loads(f.read())
            for i in grade_list:
                if i.name==self.grade_name:
                   stu_course_name=i.course_name
                else:
                    print("error")
        with open(startxuanke.BASE_DIR+"\\db\\%s_course_obj.txt"%self.school_name,"rb") as f:
            course_list=pickle.loads(f.read())
            for i in course_list:
                if i.name==stu_course_name:
                    amount=i.price
        return amount

    def write_student(self):
        with open(startxuanke.BASE_DIR+"\\db\\%s_student_obj.txt","wb+") as f:
            pickle.dumps(self.student_list)



