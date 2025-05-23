from time import strftime
from datetime import datetime
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from Student_Details import StudentDetails
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import os

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x780+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\black.jpg")
        img=img.resize((1550,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1550,height=130)

        title_lbl = Label(f_lbl, text = "FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 30, "bold"),bg="white",fg="purple")
        title_lbl.place(x=100,y=25,width = 1300,height = 90)

        #Background image.
        img2 = Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\back.jpg")
        img2 = img2.resize((1550,768),Image.Resampling.LANCZOS) 
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root,image = self.photoimg2)
        bg_img.place(x=0,y=130,width = 1550, height = 768)
        
        #time:
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl= Label(title_lbl, font=('times new roman', 14, 'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()


        #Student button
        img3 = Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\stu.jpg")
        img3 = img3.resize((220,220),Image.Resampling.LANCZOS) 
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(bg_img,image =self.photoimg3,command=self.student_details,cursor="hand2")
        b1.place(x=100,y = 100,width=220 , height = 220)

        b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman", 12, "bold"),bg="blue",fg="white")
        b1_1.place(x=100,y = 319,width=220 , height = 50)

        #Detect face button
        img4 = Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\facedetect.png")
        img4 = img4.resize((220,220),Image.Resampling.LANCZOS) 
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b2 = Button(bg_img,image =self.photoimg4,cursor="hand2", command=self.face_data)
        b2.place(x=465,y = 100,width=220 , height = 220)

        b2_1 = Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman", 12, "bold"),bg="blue",fg="white")
        b2_1.place(x=465,y = 319,width=220 , height = 50)

        #Attendance button
        img5 = Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\attend.png")
        img5 = img5.resize((220,220),Image.Resampling.LANCZOS) 
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b3 = Button(bg_img,image =self.photoimg5,cursor="hand2", command=self.attendance_data)
        b3.place(x=830,y = 100,width=220 , height = 220)

        b3_1 = Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman", 12, "bold"),bg="blue",fg="white")
        b3_1.place(x=830,y = 319,width=220 , height = 50)

        #Help desk button
        img6 = Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\contact.png")
        img6 = img6.resize((220,220),Image.Resampling.LANCZOS) 
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b4 = Button(bg_img,image =self.photoimg6,cursor="hand2", command=self.help_data)
        b4.place(x=1195,y = 100,width=220 , height = 220)

        b4_1 = Button(bg_img,text="Help",cursor="hand2", command=self.help_data,font=("times new roman", 12, "bold"),bg="blue",fg="white")
        b4_1.place(x=1195,y = 319,width=220 , height = 50)

        #Train face button
        img7 = Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\traindata.png")
        img7 = img7.resize((220,220),Image.Resampling.LANCZOS) 
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b5 = Button(bg_img,image =self.photoimg7,cursor="hand2", command=self.train_data)
        b5.place(x=100,y = 400,width=220 , height = 220)

        b5_1 = Button(bg_img,text="Train Face",cursor="hand2",command=self.train_data,font=("times new roman", 12, "bold"),bg="blue",fg="white")
        b5_1.place(x=100,y = 610,width=220 , height = 50)

        #Photos button
        img8 = Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\photos.jpg")
        img8 = img8.resize((220,220),Image.Resampling.LANCZOS) 
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b6 = Button(bg_img,image =self.photoimg8,cursor="hand2",command=self.open_img)
        b6.place(x=465,y = 400,width=220 , height = 220)

        b6_1 = Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman", 12, "bold"),bg="blue",fg="white")
        b6_1.place(x=465,y = 610,width=220 , height = 50)

        #Developer button
        img9 = Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\developer.jpg")
        img9 = img9.resize((220,220),Image.Resampling.LANCZOS) 
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b7 = Button(bg_img,image =self.photoimg9,cursor="hand2", command=self.developer_details)
        b7.place(x=830,y = 400,width=220 , height = 220)

        b7_1 = Button(bg_img,text="Developer",cursor="hand2", command=self.developer_details,font=("times new roman", 12, "bold"),bg="blue",fg="white")
        b7_1.place(x=830,y = 610,width=220 , height = 50)

        #Exit button
        img10 = Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\exit.jpg")
        img10 = img10.resize((220,220),Image.Resampling.LANCZOS) 
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b8 = Button(bg_img,image =self.photoimg10,cursor="hand2",command=self.iExit )
        b8.place(x=1195,y = 400,width=220 , height = 220)

        b8_1 = Button(bg_img,text="Exit",cursor="hand2",command=self.iExit ,font=("times new roman", 12, "bold"),bg="blue",fg="white")
        b8_1.place(x=1195,y = 610,width=220 , height = 50)


    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return 



     #===============FUNCTIONS BUTTONS=================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=StudentDetails(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)



if __name__=="__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()