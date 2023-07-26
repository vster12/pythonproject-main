class Course:
    def __init__(self, course_name):
        self.__course_students = {}
        self.__course_name = course_name

    def infos(self):
        return str(self.__course_students).replace('\'','"').replace(' ','') + ' ' + self.__course_name

    def set_students(self,diction):
        self.__course_students = diction

    def get_course_name(self):
        return self.__course_name

    def set_mark(self,student_id,att,mid,fin):
        self.__course_students[student_id] = [att,mid,fin]

    def get_attendance(self, student_id):
        return self.__course_students[student_id][0]

    def get_midTerm(self, student_id):
        return self.__course_students[student_id][1]

    def get_final(self, student_id):
        return self.__course_students[student_id][2]

    def add_student(self, student_id):
        self.__course_students[student_id] = [0] * 3

    def show_student_info(self):
        return self.__course_students

    def show_total_student(self):
        return len(self.__course_students)

    def remove_student(self,student_id):
        self.__course_students.pop(student_id)

    def get_total(self,student_id):
        return round(int(self.get_attendance(student_id))*0.1+int(self.get_midTerm(student_id))*0.4+int(self.get_final(student_id))*0.5,2)