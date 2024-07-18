from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Management System")

        img=Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\black.jpg")
        img=img.resize((1366,128),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1366,height=138)

        title_lbl = Label(f_lbl, text = "STUDENT MANAGEMENT SYSTEM", font=("times new roman", 30, "bold"),bg="white",fg="purple")
        title_lbl.place(x=25,y=25,width = 1300,height = 90)

        #Background image.
        img2 = Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\bLack.jpg")
        img2 = img2.resize((1366,640),Image.Resampling.LANCZOS) 
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root,image = self.photoimg2)
        bg_img.place(x=0,y=128,width = 1366, height = 640)







if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()