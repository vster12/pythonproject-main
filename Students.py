class Student:
    def __init__(self, name, email, phoneNumber, birth):
        self.__name = name
        self.__email = email
        self.__phoneNumber = phoneNumber
        self.__birth = birth
        self.__courses = []

    def infos(self):
        return self.__email + ' ' + self.__phoneNumber + ' ' + self.__birth + ' ' + str(self.__courses).strip("[]").replace(' ','').replace('\'','') + ' ' + self.__name

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phoneNumber(self):
        return self.__phoneNumber

    def get_birth(self):
        return self.__birth

    def standardizing(self):
        if self.__birth[1] == '/':
            self.__birth = '0' + self.__birth
        if self.__birth[4] == '/':
            self.__birth = self.__birth[0: 3] + '0' + self.__birth[3:]
        tmp = self.__name.split()
        res = ' '.join(tmp)
        res = res.title()
        self.__name = res

    def set_courses(self, course_ids):
        for course in course_ids:
            self.__courses.append(course)

    def remove_course(self,cid):
        self.__courses.pop(self.__courses.index(cid))

    def get_courses(self):
        return self.__courses

    def edit_student(self, name, email, phoneNumber, birth, courses):
        self.__name = name
        self.__email = email
        self.__phoneNumber = phoneNumber
        self.__birth = birth
        self.__courses = courses