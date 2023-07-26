from tkinter import *
import database
from tkinter.ttk import Treeview


class Page2:
    def __init__(self, window,login):
        self.login = login
        self.window = window
        self.window.geometry('1300x750')
        self.window.protocol("WM_DELETE_WINDOW", lambda : database.on_closing(self.window))
        self.window.resizable(False, False)
        self.window.title("Admin")
        self.window.img = PhotoImage(file=r"image\theme.png")
        self.window.banner = PhotoImage(file=r"image\banner.png")
        lb = Listbox(self.window, width=1, height=30, bg="red")
        lb.place(x=120, y=8)
        self.canvas = Canvas(self.window, width=self.window.img.width(), height=self.window.img.height())
        self.canvas.place(x=0, y=0)
        self.canvas.create_image(0, 0, image=self.window.banner, anchor="nw")
        self.theme = self.canvas.create_image(0, 0, image=self.window.img, anchor="nw")

        self.hcur = 0
        self.on_screen = []

        self.white = self.canvas.create_rectangle(63, 510, 222, 588, fill="white", outline="")
        course_btn = self.canvas.create_rectangle(406, 0, 609, 72, fill="", outline="")
        self.canvas.tag_bind(course_btn, "<Button-1>", lambda i: self.show_cinfo())

        student_info_btn = self.canvas.create_rectangle(0, 0, 203, 72, fill="", outline="")
        self.canvas.tag_bind(student_info_btn, "<Button-1>", lambda i: self.show_sinfo())
        # Add mark button:
        mark_btn = self.canvas.create_rectangle(203, 0, 406, 72, fill="", outline="")
        self.canvas.tag_bind(mark_btn, "<Button-1>", lambda i: self.add_mark())
        # Add course button:
        add_course_btn = self.canvas.create_rectangle(609, 0, 812, 72, fill="", outline="")
        self.canvas.tag_bind(add_course_btn, "<Button-1>", lambda i: self.add_course())

        edit_student_btn = self.canvas.create_rectangle(1015, 0, 1218, 72, fill="", outline="")
        self.canvas.tag_bind(edit_student_btn, "<Button-1>", lambda i: self.edit_student())

        add_student_btn = self.canvas.create_rectangle(812, 0, 1018, 72, fill="", outline="")
        self.canvas.tag_bind(add_student_btn, "<Button-1>", lambda i: self.add_student())

        logout = self.canvas.create_rectangle(1225, 18, 1260, 54, fill="", outline="")
        self.canvas.tag_bind(logout, "<Button-1>", lambda i: self.logout())

    def show_sinfo(self):
        # Check if the frame has already been created
        self.change_tab(-750)
        # Create a new frame to hold the Treeview and Scrollbar widgets
        self.frame = Frame(self.window)
        self.frame.pack(expand=1, padx=5, pady=5)
        self.canvas.delete(self.white)
        self.scroll_x = Scrollbar(self.frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.frame, orient=VERTICAL)

        # Create the Treeview widget and add columns and headings
        self.table = Treeview(self.frame, columns=("ID", "Name", "DoB", "Mail", "Phone Number"),
                              yscrollcommand=self.scroll_y.set,
                              xscrollcommand=self.scroll_x.set)

        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.config(command=self.table.xview)
        self.scroll_y.config(command=self.table.yview)

        self.table.heading("ID", text="ID")
        self.table.heading("Name", text="Student Name")
        self.table.heading("DoB", text="DoB")
        self.table.heading("Mail", text="Email address")
        self.table.heading("Phone Number", text="Phone Number")
        self.table["show"] = "headings"
        self.table.pack(fill=BOTH, expand=1)

        counter = 0
        for i in database.students:
            self.table.insert('', counter,
                              values=(i, database.students[i].get_name(), database.students[i].get_birth(),
                                      database.students[i].get_email(), database.students[i].get_phoneNumber()))
            counter += 1
        self.on_screen = [self.table, self.scroll_y, self.scroll_x, self.frame]

    def show_cinfo(self):
        self.change_tab(-2250)
        self.canvas.delete(self.white)
        self.frame = Frame(self.window)
        self.frame.pack(expand=1, padx=3, pady=5)

        self.scroll_x = Scrollbar(self.frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.frame, orient=VERTICAL)

        # Create the Treeview widget and add columns and headings
        self.table = Treeview(self.frame, columns=("ID", "Course Name", "Number of Student"),
                              yscrollcommand=self.scroll_y.set,
                              xscrollcommand=self.scroll_x.set)

        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.config(command=self.table.xview)
        self.scroll_y.config(command=self.table.yview)
        counter = 0
        for i in database.courses:
            self.table.insert('', counter,
                              values=(
                              i, database.courses[i].get_course_name(), database.courses[i].show_total_student()))
            counter += 1
        self.table["show"] = "headings"
        self.table.heading("ID", text="ID")
        self.table.column("ID", width=70)
        self.table.heading("Course Name", text="Course Name")
        self.table.heading("Number of Student", text="Number of Student")
        self.table.column("Number of Student", width=70)
        self.table.pack(fill=BOTH, expand=1)

        self.on_screen = [self.table,self.scroll_x,self.scroll_y,self.frame]

    def add_course(self):
        self.change_tab(-3000)
        self.canvas.delete(self.white)
        self.inp_coursename = Entry(self.window, width=30, font=("Time New Roman", 30), bg='#D9D9D9', relief=FLAT)
        self.inp_coursename.place(x=553, y=297, width=585, height=68)
        self.ad_Sub = self.canvas.create_rectangle(783, 418, 932, 492, fill="", outline="")
        self.canvas.tag_bind(self.ad_Sub, "<Button-1>",
                             lambda event: database.add_new_course(self.inp_coursename.get()))
        self.on_screen = [self.inp_coursename, self.ad_Sub]

    def add_mark(self):
        self.change_tab(-1500)
        self.canvas.delete(self.white)
        xcord = 90
        ycord = 100
        for i in database.courses:
            sub_Button = Button(self.window, text=i, font=("Time New Roman", 30), background='#5F8D4E',
                                command=lambda i=i: self.course_mark(database.courses[i], i))
            sub_Button.place(x=xcord, y=ycord, width=185, height=50)
            self.on_screen.append(sub_Button)
            ycord += 80
            if ycord >= 700:
                xcord += 200
                ycord = 100

    def course_mark(self, course, cid):
        student_list = course.show_student_info()
        self.change_tab(-1500)
        xcord = 90
        ycord = 100
        for i in student_list:
            sub_Button = Button(self.window, text=i, font=("Time New Roman", 30), background='#5F8D4E',
                                command=lambda i=i: self.mark(student_list[i], i, course, cid))
            sub_Button.place(x=xcord, y=ycord, width=185, height=50)
            self.on_screen.append(sub_Button)
            ycord += 80
            if ycord >= 500:
                xcord += 200
                ycord = 100
        self.sub_Button = Button(self.window, text="Back", font=("Time New Roman", 20), background='#5F8D4E',
                                 command=self.add_mark)
        self.sub_Button.place(x=1120, y=665, width=145, height=50)
        self.on_screen.append(self.sub_Button)

    def mark(self, sm, sid, course, cid):
        name = Label(self.window, text=f'{sid}:', font=("Time New Roman", 30), background='#5F8D4E')
        name.place(x=90, y=550)
        grade = Label(self.window, text='Att:        /20 Mid:        /20 Fin:        /20', font=("Time New Roman", 30),
                      background='#ffffff')
        grade.place(x=300, y=550)
        att = Entry(self.window, width=3, font=("Time New Roman", 30), bg='#D9D9D9')
        att.place(x=376, y=550)
        att.insert(0, sm[0])
        mid = Entry(self.window, width=3, font=("Time New Roman", 30), bg='#D9D9D9')
        mid.place(x=600, y=550)
        mid.insert(0, sm[1])
        fin = Entry(self.window, width=3, font=("Time New Roman", 30), bg='#D9D9D9')
        fin.place(x=824, y=550)
        fin.insert(0, sm[2])
        self.confirm = Button(self.window, text="Confirm", font=("Time New Roman", 20), background='#5F8D4E',
                              command=lambda: course.set_mark(sid, att.get(), mid.get(), fin.get()))
        self.confirm.place(x=920, y=665, width=145, height=50)
        delete = Button(self.window, text="Delete Student", font=("Time New Roman", 20), background='Red',
                        command=lambda: database.remove(sid, cid))
        delete.place(x=220, y=665, width=195, height=50)

        self.on_screen += [att, mid, fin, grade, name, self.confirm, delete]

    def find_student(self, sid):
        self.change_tab(-4500)
        student = 0
        for i in database.students:
            if i == sid: student = database.students[i]
        if student == 0:
            self.error = Label(self.window, text='Student ID does not exist', font="12")
            self.error.place(x=74, y=515)
            self.window.after(2000, lambda: self.error.destroy())
            self.edit_student()
            return 0

        self.canvas.delete(self.white)
        self.inp_studentid = Entry(self.window, width=30, font=("Time New Roman", 30), bg='#D9D9D9', relief=FLAT)
        self.inp_studentid.place(x=74, y=315, width=222, height=62)

        self.sid = Label(self.window, width=20, font=("Time New Roman", 30), text=sid, background='#D9D9D9')
        self.sid.place(x=74, y=140, width=185, height=50)

        self.inp_studentname = Entry(self.window, width=30, font=("Time New Roman", 30), bg='#D9D9D9', relief=FLAT)
        self.inp_studentname.place(x=765, y=119, width=485, height=70)
        self.inp_studentname.insert(0, student.get_name())

        self.inp_email = Entry(self.window, width=30, font=("Time New Roman", 30), bg='#D9D9D9', relief=FLAT)
        self.inp_email.place(x=765, y=235, width=485, height=70)
        self.inp_email.insert(0, student.get_email())

        self.inp_phonenumber = Entry(self.window, width=30, font=("Time New Roman", 30), bg='#D9D9D9', relief=FLAT)
        self.inp_phonenumber.place(x=765, y=355, width=485, height=70)
        self.inp_phonenumber.insert(0, student.get_phoneNumber())

        self.inp_day = Entry(self.window, width=3, font=("Time New Roman", 30), bg='#D9D9D9', relief=FLAT)
        self.inp_day.place(x=765, y=493, width=94, height=70)
        self.inp_day.insert(0, student.get_birth()[:2])
        self.inp_month = Entry(self.window, width=3, font=("Time New Roman", 30), bg='#D9D9D9', relief=FLAT)
        self.inp_month.place(x=950, y=493, width=94, height=70)
        self.inp_month.insert(0, student.get_birth()[3:5])
        self.inp_year = Entry(self.window, width=5, font=("Time New Roman", 30), bg='#D9D9D9', relief=FLAT)
        self.inp_year.place(x=1133, y=493, width=130, height=70)
        self.inp_year.insert(0, student.get_birth()[6:])

        self.inp_student_course = Entry(self.window, width=30, font=("Time New Roman", 30), bg='#D9D9D9', relief=FLAT)
        self.inp_student_course.place(x=765, y=618, width=485, height=70)
        self.inp_student_course.insert(0, str(student.get_courses()).strip("[]").replace('\'', ''))
        self.ad_Sub = self.canvas.create_rectangle(63, 520, 222, 588, fill="", outline="")
        self.canvas.delete(self.white)
        self.canvas.tag_bind(self.ad_Sub, "<Button-1>",
                             lambda event: database.edit_info(sid, self.inp_studentname.get(),
                                                              self.inp_email.get(), self.inp_phonenumber.get(),
                                                              f'{self.inp_day.get()}/{self.inp_month.get()}/{self.inp_year.get()}',
                                                              self.inp_student_course.get().split(", ")))
        self.conf = self.canvas.create_rectangle(63, 400, 222, 468, fill="", outline="")
        self.canvas.tag_bind(self.conf, "<Button-1>",
                             lambda event: self.find_student(self.inp_studentid.get()))
        self.on_screen = [self.inp_day, self.inp_email, self.inp_phonenumber, self.inp_year, self.inp_month,
                          self.inp_student_course, self.inp_studentname, self.inp_studentid, self.sid]

    def edit_student(self):
        self.change_tab(-4500)
        self.white = self.canvas.create_rectangle(63, 510, 222, 588, fill="white", outline="")
        self.inp_studentid = Entry(self.window, width=30, font=("Time New Roman", 30), bg='#D9D9D9', relief=FLAT)
        self.inp_studentid.place(x=74, y=315, width=222, height=62)

        self.ad_Sub = self.canvas.create_rectangle(63, 400, 222, 468, fill="", outline="")
        self.canvas.tag_bind(self.ad_Sub, "<Button-1>",
                             lambda event: self.find_student(self.inp_studentid.get()))

        self.on_screen = [self.inp_studentid, self.ad_Sub]

    def add_student(self):
        self.change_tab(-3750)
        self.canvas.delete(self.white)
        self.inp_studentname = Entry(self.window, width=30, font=("Time New Roman", 30), bg='#D9D9D9', relief=FLAT)
        self.inp_studentname.place(x=518, y=172, width=552, height=62)

        self.inp_email = Entry(self.window, width=30, font=("Time New Roman", 30), bg='#D9D9D9', relief=FLAT)
        self.inp_email.place(x=518, y=269, width=552, height=62)

        self.inp_phonenumber = Entry(self.window, width=30, font=("Time New Roman", 30), bg='#D9D9D9', relief=FLAT)
        self.inp_phonenumber.place(x=518, y=369, width=552, height=62)

        self.inp_day = Entry(self.window, width=3, font=("Time New Roman", 30), bg='#D9D9D9', relief=FLAT)
        self.inp_day.place(x=518, y=473, width=123, height=62)
        self.inp_month = Entry(self.window, width=3, font=("Time New Roman", 30), bg='#D9D9D9', relief=FLAT)
        self.inp_month.place(x=718, y=473, width=113, height=62)
        self.inp_year = Entry(self.window, width=5, font=("Time New Roman", 30), bg='#D9D9D9', relief=FLAT)
        self.inp_year.place(x=922, y=473, width=155, height=62)

        self.inp_student_course = Entry(self.window, width=30, font=("Time New Roman", 30), bg='#D9D9D9', relief=FLAT)
        self.inp_student_course.place(x=518, y=578, width=552, height=62)

        self.ad_Sub = self.canvas.create_rectangle(1123, 362, 1280, 433, fill="", outline="")
        self.canvas.tag_bind(self.ad_Sub, "<Button-1>",
                             lambda event: database.add_new_student(self.inp_studentname.get(),
                                                                    self.inp_email.get(),
                                                                    self.inp_phonenumber.get(),
                                                                    f'{self.inp_day.get()}/{self.inp_month.get()}/{self.inp_year.get()}',
                                                                    self.inp_student_course.get().split(",")))

        self.on_screen = [self.inp_day, self.inp_year, self.inp_month, self.inp_student_course, self.ad_Sub,
                          self.inp_email, self.inp_phonenumber, self.inp_studentname]

    def change_tab(self, new_position):
        for i in self.on_screen:
            try:
                i.destroy()
            except:
                self.canvas.delete(i)
        self.canvas.move(self.theme, 0, new_position - self.hcur)
        self.hcur = new_position

    def logout(self):
        self.login.deiconify()
        self.window.destroy()


# a = Tk()
# Page2(a)
# a.mainloop()
