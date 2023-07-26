import Courses, Students
import json

courses = {}
students = {}


def add_new_course(name):
    name=name.capitalize()
    c = Courses.Course(name)
    count = 0
    for i in courses:
        if i[:3] == name[:3]: count+=1
    cid = name[:3] + "." + str(count+1).zfill(3)
    courses.update({cid:c})
    return cid

def add_new_student(name, email, phoneNumber, birth,s_courses):
    s = Students.Student(name, email, phoneNumber, birth)
    s.set_courses(s_courses)
    sid = 'BI12-' + str((len(students)+1)).zfill(3)
    for course in courses:
        if course in s_courses:
            courses[course].add_student(sid)
    students.update({sid:s})

def edit_info(id,name, email, phoneNumber, birth,s_courses):
    for i in students[id].get_courses():
        if i not in s_courses:
            courses[i].remove_student(id)
    for i in s_courses:
        if i not in students[id].get_courses():
            courses[i].add_student(id)
    students[id].edit_student(name,email,phoneNumber,birth,s_courses)

def remove(sid,cid):
    students[sid].remove_course(cid)
    courses[cid].remove_student(sid)

def on_closing(window):
    f1 = open('student_backup.txt','r')
    f2 = open('course_backup.txt','r')
    student_backup = f1.readlines()
    course_backup = f2.readlines()
    f1 = open('student_backup.txt', 'a')
    f2 = open('course_backup.txt', 'a')
    for i in students:
        stud = students[i].infos() + '\n'
        if stud not in student_backup:
            f1.write(stud)
    for i in courses:
        cour = courses[i].infos() + '\n'
        if cour not in course_backup:
            f2.write(cour)
    f1.close()
    f2.close()
    window.destroy()

def load_backup():
    f1 = open('student_backup.txt', 'r')
    f2 = open('course_backup.txt', 'r')
    course_backup = f2.readlines()
    student_backup = f1.readlines()
    for i in student_backup:
        info = i.strip('\n').split(' ',4)
        add_new_student(info[4],info[0],info[1],info[2],[c for c in info[3].split(',')])
    for i in course_backup:
        info = i.strip('\n').split(' ',2)
        load_course(info[1],json.loads(info[0]))
    f1.close()
    f2.close()

def load_course(name,stu):
    cid = add_new_course(name)
    courses[cid].set_students(stu)
