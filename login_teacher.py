from tkinter import *
from PIL import Image, ImageFont,ImageTk
import tkinter.messagebox as messagebox
import page2, database
from hashlib import sha256

class login:
    def __init__(self,root,login):
        self.login = login
        self.root = root
        self.root.title('Admin')
        self.root.protocol("WM_DELETE_WINDOW", lambda : database.on_closing(self.root))
        self.root.update()
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())
        x_cordinate = int((self.root.winfo_screenwidth() / 4 - self.root.winfo_width() / 2))
        y_cordinate = int((self.root.winfo_screenheight() / 4 - self.root.winfo_height() / 2))
        self.root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
# adjust size
        self.root.geometry("900x600")
# tells the root to not let the widgets inside it determine its size.
        self.root.pack_propagate(False)
        self.root.resizable(0, 0)  # makes the root window fixed in size.

        img = PhotoImage(file=r"image\teacher_log.png")
        self.root.img = img
# create a canvas on top of the label to make it clickable
        self.canvas = Canvas(self.root, width=self.root.img.width(), height=self.root.img.height())
        self.canvas.pack()
        self.canvas.place(x=0, y=0)

        self.canvas.create_image(0, 0, image=self.root.img, anchor="nw")

#Label
        self.admin = Entry(self.root, text = "", bg ='#D9D9D9',font = ("Time New Roman", 25),relief= FLAT)
        self.admin.place(x = 87, y = 197, width = 352, height = 38)

#password
        self.password = Entry(self.root, text = "", bg ='#D9D9D9',font = ("Time New Roman", 25),relief= FLAT,show='*')
        self.password.place(x = 80, y = 338, width = 352, height = 38)

        self.hide_import = Image.open(r"image\hide.png")
        self.inp_Pswd = Entry(root, width = 30, font="10", show='*')
        self.resize_hide = self.hide_import.resize((30, 30), Image.ANTIALIAS)

        self.img_hide = ImageTk.PhotoImage(self.resize_hide)
        self.photo_hide = Button(root, text="", font=("Time New Roman", 10), image=self.img_hide,
                                 command=self.show_password, border = 0, bg = '#D9D9D9')
        self.photo_hide.place(x=440, y=341)

#button submit
        self.ad_Sub = self.canvas.create_rectangle(190,415,315,540,fill ="", outline = "")
        self.canvas.tag_bind(self.ad_Sub, "<Button-1>", lambda log: self.submit())

#button log as stu
        self.ad_log = self.canvas.create_rectangle(152, 493, 353, 534, fill="", outline="")
        self.canvas.tag_bind(self.ad_log, "<Button-1>", lambda logst: self.open_student_login())

#pass *
    def show_password(self):
        if self.password.cget('show') == '':
            self.password.config(show='*')
        else:
            self.password.config(show='')

#submit
    def go_page2(self):
        win = Toplevel()
        print(page2.__file__)
        self.admin.delete(0,END)
        self.password.delete(0,END)
        page2.Page2(win, self.root)
        self.root.withdraw()

    def submit(self):
        self.username = self.admin.get()
        self.passw = self.password.get()
        f = open("admin_credentials.txt", "r")
        admin_cred = f.readlines()
        verified = False
        for cred in admin_cred:
            [usr, pwd] = cred.strip().split()
            if self.username.strip() == usr and sha256(self.passw.strip().encode('utf-8')).hexdigest() == pwd:
                verified = True
        if verified:
            self.go_page2()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

#log as stu
    def open_student_login(self):
        self.login.deiconify()
        self.root.destroy()

