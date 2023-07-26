from tkinter import *
from PIL import Image, ImageFont, ImageTk
import page3, database, login_teacher

database.load_backup()
class login:
    def __init__(self, root):
        self.root = root
        self.root.title('Student')

        # adjust size
        self.root.geometry("900x600")
        # tells the root to not let the widgets inside it determine its size.
        self.root.pack_propagate(False)
        self.root.resizable(0, 0)  # makes the root window fixed in size.

        img = PhotoImage(file=r"image\student_log.png")
        self.root.img = img
        # create a canvas on top of the label to make it clickable
        self.canvas = Canvas(self.root, width=self.root.img.width(), height=self.root.img.height())
        self.canvas.pack()
        self.canvas.place(x=0, y=0)

        self.canvas.create_image(0, 0, image=self.root.img, anchor="nw")

        # student id
        self.student_id = Entry(self.root, bg='#D9D9D9', font=("Time New Roman", 25), relief=FLAT)
        self.student_id.place(x=421, y=279, width=352, height=68)

        # button submit
        self.ad_Sub = self.canvas.create_rectangle(551, 394, 676, 449, fill="", outline="")
        self.canvas.tag_bind(self.ad_Sub, "<Button-1>", lambda event: self.go_page3(self.student_id.get()))

        # button log as teacher
        self.ad_log = self.canvas.create_rectangle(513, 472, 714, 513, fill="", outline="")
        self.canvas.tag_bind(self.ad_log, "<Button-1>", lambda event: self.open_teacher_login())

        # login as teacher

    def open_teacher_login(self):
        win = Toplevel()
        login_teacher.login(win, self.root)
        self.root.withdraw()

    def go_page3(self, sid):
        if sid not in database.students:
            error = Label(self.root, fg='red', bg='#ffffff', font=("Time New Roman", 10), text='Wrong student ID')
            error.place(x=438, y=362, width=352, height=20)
            self.root.after(2000, lambda: error.destroy())
        else:
            win = Toplevel()
            page3.Page3(win, self.root, self.student_id.get())
            self.root.withdraw()

root = Tk()
login(root)
root.protocol("WM_DELETE_WINDOW", lambda : database.on_closing(root))
root.mainloop()
