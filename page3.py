from tkinter import *
from database import students, courses
import tkinter.messagebox as messagebox
from PIL import ImageTk, Image
from tkinter.ttk import Treeview
from tkinter import Text, Tk
import database

class Page3:
    def __init__(self, root,login,student_id):
        self.login = login
        self.root = root
        self.sid = student_id
        self.root.title('Student Page')

        # adjust size
        self.root.geometry("1300x750")
        # tells the root to not let the widgets inside it determine its size.
        self.root.pack_propagate(False)
        self.root.resizable(0, 0)  # makes the root window fixed in size.
        self.root.protocol("WM_DELETE_WINDOW", lambda : database.on_closing(self.root))
        img = PhotoImage(file=r"image\student_page.png")
        self.root.img = img
        # create a canvas on top of the label to make it clickable
        self.canvas = Canvas(self.root, width=self.root.img.width(), height=self.root.img.height())
        self.canvas.pack()
        self.canvas.place(x=0, y=0)

        self.canvas.create_image(0, 0, image=self.root.img, anchor="nw")

        label_id = Label(self.root, text=self.sid, font="12", fg="white", bg="#285430", relief=RAISED, borderwidth=3, width=30, height = 2)
        label_id.place(x=86,y=190,width=100)
        # Your info button:
        self.info_btn = self.canvas.create_rectangle(42, 299, 221, 357, fill="", outline="")
        self.canvas.tag_bind(self.info_btn, "<Button-1>", lambda i: self.show_info())

        self.course_btn = self.canvas.create_rectangle(42, 400, 222, 462, fill="", outline="")
        self.canvas.tag_bind(self.course_btn, "<Button-1>", lambda id: self.show_course())

        self.back_btn = self.canvas.create_rectangle(42, 648, 221, 712, fill="", outline="")
        self.canvas.tag_bind(self.back_btn, "<Button-1>", lambda event: self.back())

        self.on_screen=[]

    def show_info(self):
        self.change_tab()
        stu = students[self.sid]
        student_Name = Label(self.root, text='Student Name:', font="12", fg="white", bg="#285430", relief=RAISED, borderwidth=3, width=30, height = 2)
        student_Name.place(x=450, y=130)

        inp_StuName =Label(self.root, text=stu.get_name(),  font="10",relief=RAISED, borderwidth=3, width=33, height = 2)
        inp_StuName.place(x=850, y=130)

        student_Id = Label(self.root, text='Student ID:', font="12", bg="#285430",fg="white", relief=RAISED, borderwidth=3, width = 30, height =2)
        student_Id.place(x=450, y=200)

        inp_StuID = Label(self.root, text=self.sid, width=33, height=2, font="10", relief=RAISED, borderwidth=3)
        inp_StuID.place(x=850, y=200)

        student_DoB = Label(self.root, text='Date of Birth:', font="12", bg="#285430",fg="white", relief=RAISED, borderwidth=3, width = 30, height =2)
        student_DoB.place(x=450, y=270)

        inp_StuDoB = Label(self.root, text=stu.get_birth(), width=33, height=2, font="10", relief=RAISED, borderwidth=3)
        inp_StuDoB.place(x=850, y=270)
        #
        student_Email = Label(self.root, text='Student Email:', font="12", bg="#285430",fg="white", relief=RAISED, borderwidth=3, width = 30, height =2)
        student_Email.place(x=450, y=340)

        inp_StuEmail = Label(self.root, text=stu.get_email(), width=33, height=2, font="10", relief=RAISED, borderwidth=3)
        inp_StuEmail.place(x=850, y=340)
        #
        phone_number = Label(self.root, text='Phone number:', font="12", bg="#285430",fg="white", relief=RAISED, borderwidth=3, width = 30, height =2)
        phone_number.place(x=450, y=410)

        inp_phoneNumber = Label(self.root, text=stu.get_phoneNumber(), width=33, height=2, font="10", relief=RAISED, borderwidth=3)
        inp_phoneNumber.place(x=850, y=410)

        self.on_screen = [student_Name,student_Id,student_Email,student_DoB,phone_number,inp_phoneNumber,inp_StuID,inp_StuDoB,inp_StuName,inp_StuEmail]


    def show_course(self):
        self.change_tab()
        self.frame = Frame(self.root)
        self.frame.pack(side= RIGHT, expand=1, padx=3, pady=5,fill= X)
        self.frame.place(relx=0.205, rely=0.5, anchor= W)
        self.scroll_x = Scrollbar(self.frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.frame, orient=VERTICAL)

        # Create the Treeview widget and add columns and headings
        self.table = Treeview(self.frame, columns=("Course Name", "Attendance", "Midterm", "Final", "Total"),
                              yscrollcommand=self.scroll_y.set,
                              xscrollcommand=self.scroll_x.set)

        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.config(command=self.table.xview)
        self.scroll_y.config(command=self.table.yview)
        counter = 0
        for i in students[self.sid].get_courses():
            self.table.insert('', counter,
                              values=(
                                  i, courses[i].get_attendance(self.sid), courses[i].get_midTerm(self.sid), courses[i].get_final(self.sid), courses[i].get_total(self.sid)))
            counter += 1

        self.table["show"] = "headings"
        self.table.heading("Course Name", text="Course Name")
        self.table.heading("Attendance", text="Attendance")
        self.table.heading("Midterm", text="Midterm")
        self.table.heading("Final", text="Final")
        self.table.heading("Total", text="Total")

        self.table.pack(fill=BOTH, expand=1)

        self.on_screen = [self.table, self.scroll_x, self.scroll_y, self.frame]

    # Log Out button:
    def back(self):
        self.login.deiconify()
        self.root.destroy()

    def change_tab(self):
        for i in self.on_screen:
            i.destroy()


