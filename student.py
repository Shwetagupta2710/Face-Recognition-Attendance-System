from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Management System")

         #==========Variables==========
        self.serchTxt_var=StringVar()
        self.search_var=StringVar()
        self.var_dep=StringVar()
        self.var_course=StringVar() #for later uses
        self.var_year=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_semester=StringVar()

        img=Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\black.jpg")
        img=img.resize((1366,128),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1366,height=138)

        title_lbl = Label(f_lbl, text = "STUDENT MANAGEMENT SYSTEM", font=("times new roman", 30, "bold"),bg="purple",fg="white")
        title_lbl.place(x=25,y=25,width = 1300,height = 90)

        #Background image.
        img2 = Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\bLack.jpg")
        img2 = img2.resize((1366,640),Image.Resampling.LANCZOS) 
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root,image = self.photoimg2)
        bg_img.place(x=0,y=128,width = 1366, height = 640)

        #main frame
        main_frame = Frame(bg_img)
        main_frame.place(x=25,y=0,width=1300,height = 560)

        #left frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,text="Student Details",cursor="hand2",font=("times new roman", 12, "bold"),bg="white",fg="red")
        left_frame.place(x=10,y=10,width=630,height = 540)
        img_left = Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\student2.jpg")
        img_left = img_left.resize((100,60),Image.Resampling.LANCZOS) 
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(left_frame,image =self.photoimg_left,cursor="hand2")
        f_lbl.place(x=270,y = 10,width=60, height = 60)

        #current course
        current_course_frame = LabelFrame(left_frame, relief=RIDGE,text="Current Course Information",font=("times new roman", 12, "bold"),fg="red")
        current_course_frame.place(x=5,y=75,width=615,height = 105)

        #department
        dep_label = Label(current_course_frame, text="Department:",font=("times new roman", 12, "bold"), fg="red")
        dep_label.grid(row=0,column=0, padx=10, sticky = W)
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman", 12, "bold"),width=17,state = "readonly")
        dep_combo["values"]=("Select Department","Computer Science","Information Science ","Electronics","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2, pady=10, sticky = W)

        #year
        year_label = Label(current_course_frame, text="Year:",font=("times new roman", 12, "bold"), fg="red")
        year_label.grid(row=0,column=2,padx=10, sticky = W)
        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman", 12, "bold"),width=17,state = "readonly")
        year_combo["values"]=("Select Year","First Year","Second Year","Third Year","Fourth Year")
        year_combo.current(0)
        year_combo.grid(row=0,column=3,padx=2, pady=10, sticky = W)

        #semester
        semester_label = Label(current_course_frame, text="Semester:",font=("times new roman", 12, "bold"), fg="red")
        semester_label.grid(row=1,column=0,padx=10, sticky = W)
        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman", 12, "bold"),width=17,state = "readonly")
        semester_combo["values"]=("Select Semester","First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=1,padx=2, pady=10, sticky = W)

        #Class Information
        class_Student_frame = LabelFrame(left_frame, relief=RIDGE,text="Class Information",font=("times new roman", 12, "bold"),fg="red")
        class_Student_frame.place(x=5,y=185,width=615,height = 315)

        #Student ID
        studentId_label = Label(class_Student_frame, text="Student ID:",font=("times new roman", 12, "bold"), fg="red")
        studentId_label.grid(row=0,column=0,padx=10, sticky = W)

        studentID_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=15,font=("times new roman", 12, "bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5, sticky =W)

        #Student Name
        studentName_label = Label(class_Student_frame, text="Student Name:",font=("times new roman", 12, "bold"), fg="red")
        studentName_label.grid(row=0,column=2,padx=10, sticky = W)

        studentName_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=15,font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5, sticky =W)

        #Class Division
        class_div_label = Label(class_Student_frame, text="Class and Section:",font=("times new roman", 12, "bold"), fg="red")
        class_div_label.grid(row=1,column=0,padx=10, sticky = W)

        class_div_entry = ttk.Entry(class_Student_frame,textvariable=self.var_div,width=15,font=("times new roman", 12, "bold"))
        class_div_entry.grid(row=1,column=1,padx=10, pady=5, sticky =W)

        #Roll_No
        roll_no_label = Label(class_Student_frame, text="Roll No:",font=("times new roman", 12, "bold"), fg="red")
        roll_no_label.grid(row=1,column=2,padx=10, sticky = W)

        roll_no_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=15,font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1,column=3,padx=10, pady=5, sticky =W)

        #Gender
        gender_label = Label(class_Student_frame, text="Gender:",font=("times new roman", 12, "bold"), fg="red")
        gender_label.grid(row=2,column=0,padx=10, sticky = W)
        gender_combo = ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman", 12, "bold"),width=13,state = "readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10, pady=5, sticky = W)

        #Date of birth
        dob_label = Label(class_Student_frame, text="Date of Birth:",font=("times new roman", 12, "bold"), fg="red")
        dob_label.grid(row=2,column=2,padx=10, sticky = W)

        dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=15,font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2,column=3,padx=10, pady=5, sticky =W)

        #Email
        email_label = Label(class_Student_frame, text="Email:",font=("times new roman", 12, "bold"), fg="red")
        email_label.grid(row=3,column=0,padx=10, sticky = W)

        email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email,width=15,font=("times new roman", 12, "bold"))
        email_entry.grid(row=3,column=1,padx=10, pady=5, sticky =W)

        #Phone No
        phone_label = Label(class_Student_frame, text="Phone No:",font=("times new roman", 12, "bold"), fg="red")
        phone_label.grid(row=3,column=2,padx=10, sticky = W)

        phone_entry = ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=15,font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3,column=3,padx=10, pady=5, sticky =W)

        #Address
        address_label = Label(class_Student_frame, text="Address:",font=("times new roman", 12, "bold"), fg="red")
        address_label.grid(row=4,column=0,padx=10, sticky = W)

        address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address,width=15,font=("times new roman", 12, "bold"))
        address_entry.grid(row=4,column=1,padx=10, pady=5, sticky =W)

        #Teacher name
        teacher_label = Label(class_Student_frame, text="Teacher:",font=("times new roman", 12, "bold"), fg="red")
        teacher_label.grid(row=4,column=2,padx=10, sticky = W)

        teacher_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=15,font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4,column=3,padx=10, pady=5, sticky =W)

        #radio buttons
        self.var_radio1=StringVar()
        radionbtn1= ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text ="Take a photo sample", value="Yes")
        radionbtn1.grid(row=5,column=0)
        radionbtn2= ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text ="No photo sample", value="No")
        radionbtn2.grid(row=5,column=1)

        
        #bbuttons_frame
        btn_frame = Frame(class_Student_frame,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=200,width=600,height = 85)

        #save button
        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman", 12, "bold"), fg="white",bg="red")
        save_btn.grid(row=0,column=0,padx=2,pady=5,sticky = W)

        #update button
        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman", 12, "bold"), fg="white",bg="red")
        update_btn.grid(row=0,column=1,padx=2,pady=2,sticky = W)

        #delete button
        delete_btn = Button(btn_frame,text="Delete",command=self.delete_Data,width=15,font=("times new roman", 12, "bold"), fg="white",bg="red")
        delete_btn.grid(row=0,column=2,padx=2,pady=2,sticky = W)

        #reset button
        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman", 12, "bold"), fg="white",bg="red")
        reset_btn.grid(row=0,column=3,padx=2,pady=2,sticky = W)

        btn_frame1 = Frame(class_Student_frame,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=240,width=600,height = 35)

        #take photo button
        take_photo_btn = Button(btn_frame1,command=self.generate_dataset, text="Take Photo Sample",width=30,font=("times new roman", 12, "bold"), fg="white",bg="red")
        take_photo_btn.grid(row=0,column=0,padx=10,pady=2,sticky = W)

        #update photo button
        update_btn = Button(btn_frame1,text="Update Photo",command=self.generate_dataset,width=30,font=("times new roman", 12, "bold"), fg="white",bg="red")
        update_btn.grid(row=0,column=1,padx=2,pady=2,sticky = W)




         #right frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,text="Student Details",cursor="hand2",font=("times new roman", 12, "bold"),bg="white",fg="red")
        right_frame.place(x=660,y=10,width=630,height = 540)

        img_right = Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\student1.png")
        img_right= img_right.resize((250,60),Image.Resampling.LANCZOS) 
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(right_frame,image =self.photoimg_right,cursor="hand2")
        f_lbl.place(x=5,y = 10,width=615, height = 60)







if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()