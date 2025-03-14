
from tkinter import *
from tkinter import ttk
from traceback import format_exc
from turtle import color
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("{width}x{height}+0+0".format(width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight()))
        self.root.title("Face Recognition System")

        full_screen_width = self.root.winfo_screenwidth()
        desired_width = full_screen_width // 3
        lower_img_height=self.root.winfo_screenheight()-298

        title_lbl = Label(self.root, text="DEVELOPER",
                          font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=full_screen_width, height=45)

        back_btn = Button(title_lbl, text="Back", command=self.close_window,width=21,
            font=("times new roman", 10, "bold"),
            bg="blue",
            fg="white",)
        back_btn.place(x=30,y=5)
        
        img_top = Image.open("images/dev.webp")
        img_top = img_top.resize((1530, 730), Image.LANCZOS)
        self.photoimage_top = ImageTk.PhotoImage(img_top)

        top_lbl = Label(self.root, image=self.photoimage_top)
        top_lbl.place(x=0, y=55, width=1530, height=730)
        #frame
        main_frame=Frame(top_lbl, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=500, height=600)

        img_top4 = Image.open("images/shweta.jpg")
        img_top4 = img_top4.resize((200, 200), Image.LANCZOS)
        self.photoimage_top4 = ImageTk.PhotoImage(img_top4)

        top_lbl = Label(main_frame, image=self.photoimage_top4)
        top_lbl.place(x=300, y=0, width=200, height=200)

         # developer info
        dev_lable = Label(main_frame,text="hello my name, Shweta",font=("times new roman", 20, "bold"),bg="white")
        dev_lable.place(x=0, y=5)

        dev_lable = Label(main_frame,text="I am a Software developer",font=("times new roman", 20, "bold"),bg="white")
        dev_lable.place(x=0, y=40)

        img_top2 = Image.open("images/student.jpg")
        img_top2 = img_top2.resize((500, 390), Image.LANCZOS)
        self.photoimage_top2 = ImageTk.PhotoImage(img_top2)

        top_lbl = Label(main_frame, image=self.photoimage_top2)
        top_lbl.place(x=0, y=210, width=500, height=390)





    def close_window(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()