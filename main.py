from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\black.jpg")
        img=img.resize((1366,128),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1366,height=138)

        title_lbl = Label(f_lbl, text = "FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 30, "bold"),bg="white",fg="purple")
        title_lbl.place(x=25,y=25,width = 1300,height = 90)

        #Background image.
        img2 = Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\background.jpg")
        img2 = img2.resize((1366,640),Image.Resampling.LANCZOS) 
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root,image = self.photoimg2)
        bg_img.place(x=0,y=128,width = 1366, height = 640)

        #Student button
        img3 = Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\student.jpg")
        img3 = img3.resize((150,150),Image.Resampling.LANCZOS) 
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(bg_img,image =self.photoimg3,cursor="hand2",command=self.student_details)
        b1.place(x=50,y = 100,width=125 , height = 125)

        b1_1 = Button(bg_img,text="Student Details",cursor="hand2",command=self.student_details,font=("times new roman", 12, "bold"),bg="darkblue",fg="white")
        b1_1.place(x=45,y = 230,width=135 , height = 20)

        #Detect face button
        img4 = Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\facedetect.png")
        img4 = img4.resize((100,100),Image.Resampling.LANCZOS) 
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b2 = Button(bg_img,image =self.photoimg4,cursor="hand2",command=self.face_recog)
        b2.place(x=225,y = 100,width=125 , height = 125)

        b2_1 = Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_recog,font=("times new roman", 12, "bold"),bg="darkblue",fg="white")
        b2_1.place(x=220,y = 230,width=135 , height = 20)

        #Attendance button
        img5 = Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\attendance.png")
        img5 = img5.resize((100,100),Image.Resampling.LANCZOS) 
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b3 = Button(bg_img,image =self.photoimg5,cursor="hand2",command=self.attendance_data)
        b3.place(x=400,y = 100,width=125 , height = 125)

        b3_1 = Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman", 12, "bold"),bg="darkblue",fg="white")
        b3_1.place(x=395,y = 230,width=135 , height = 20)

        #Help desk button
        img6 = Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\contact.png")
        img6 = img6.resize((100,100),Image.Resampling.LANCZOS) 
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b4 = Button(bg_img,image =self.photoimg6,cursor="hand2",command=self.contact_info)
        b4.place(x=575,y = 100,width=125 , height = 125)

        b4_1 = Button(bg_img,text="Contact",cursor="hand2",command=self.contact_info,font=("times new roman", 12, "bold"),bg="white",fg="red")
        b4_1.place(x=570,y = 230,width=135 , height = 20)

        #Train face button
        img7 = Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\traindata.png")
        img7 = img7.resize((100,100),Image.Resampling.LANCZOS) 
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b5 = Button(bg_img,image =self.photoimg7,cursor="hand2",command=self.train_classifier)
        b5.place(x=750,y = 100,width=125 , height = 125)

        b5_1 = Button(bg_img,text="Train Face",cursor="hand2",command=self.train_classifier,font=("times new roman", 12, "bold"),bg="white",fg="red")
        b5_1.place(x=745,y = 230,width=135 , height = 20)

        #Photos button
        img8 = Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\photos.jpg")
        img8 = img8.resize((100,100),Image.Resampling.LANCZOS) 
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b6 = Button(bg_img,image =self.photoimg8,cursor="hand2",command=self.open_img)
        b6.place(x=925,y = 100,width=125 , height = 125)

        b6_1 = Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman", 12, "bold"),bg="white",fg="red")
        b6_1.place(x=920,y = 230,width=135 , height = 20)

        



        






if __name__=="__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()