day6作业：模拟选课系统
需求：

使用面向对象技术设计模拟选课系统，使用pickle作为序列化存储方式
学校视图
   选择学校
      1.创建班级
      2.创建讲师
      3.创建课程
讲师：
    1.查看班级
    2.查看班级学员列表
学生：
    1.注册
    2.报名缴费
    3.选择班级
|-- README.txt
|-- __init__.py
|-- bin
|   |-- startxuanke.py   运行文件
|   |-- __init__.py
|   |-- __pycache__
|   |   |-- startxuanke.cpython-37.pyc
|   |   |-- __init__.cpython-37.pyc
|-- conf
|   |-- __init__.py
|-- core
|   |-- course.py  课程类
|   |-- grade.py   班级类
|   |-- main.py   程序主入口
|   |-- school.py   学校类
|   |-- student.py  学生类
|   |-- teacher.py   老师类
|   |-- __init__.py
|   |-- __pycache__
|   |   |-- course.cpython-37.pyc
|   |   |-- grade.cpython-37.pyc
|   |   |-- main.cpython-37.pyc
|   |   |-- school.cpython-37.pyc
|   |   |-- student.cpython-37.pyc
|   |   |-- teacher.cpython-37.pyc
|   |   |-- __init__.cpython-37.pyc
|-- db  数据库文件  以下文件全部存储的是pickle数据
|   |-- beijing_course_obj.txt
|   |-- beijing_grade_obj.txt
|   |-- beijing_student_obj.txt
|   |-- beijing_teacher_obj.txt
|   |-- __init__.py
