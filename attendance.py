from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
import numpy as np
from time import strftime
from datetime import datetime

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("{width}x{height}+0+0".format(width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight()))
        self.root.title("Face Recognition System")

        full_screen_width = self.root.winfo_screenwidth()
        desired_width = full_screen_width // 3
        lower_img_height=self.root.winfo_screenheight()-298

        #===============variables==========
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        

        main_image1 = Image.open(r"images\stdDtl1.jpg")
        main_image1 = main_image1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(main_image1)

        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=0, y=0, width=800, height=200)

        main_image = Image.open(r"images\stdDtl3.jpg")
        main_image = main_image.resize((800, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(main_image)

        second_label = Label(self.root, image=self.photoimg)
        second_label.place(x=800, y=0, width=800, height=200)

        # background image
        bg_img = Image.open(r"images\bgimage.jpg")
        bg_img = bg_img.resize((1550, 720), Image.LANCZOS)
        self.photoimgbg = ImageTk.PhotoImage(bg_img)
        bg_label = Label(self.root, image=self.photoimgbg)
        bg_label.place(x=0, y=130, width=1550, height=720)

         # title label
        titl_lbl = Label(
            bg_label,
            text="ATTENDANCE MANAGEMENT SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="red",
        )
        titl_lbl.place(x=0, y=0, width=1530, height=45)

         # frame on bg image
        main_frame = Frame(bg_label, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=600)

        # left label frame onto the main_frame
        left_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student Attendance Details",
            font=("times new roman", 12, "bold"),
        )
        left_frame.place(x=10, y=10, width=700, height=620)

        left_image = Image.open(r"images\left_label.jpg")
        left_image = left_image.resize((680, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(left_image)

        left_label = Label(left_frame, image=self.photoimg_left)
        left_label.place(x=10, y=0, width=680, height=130)

        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=10, y=135, width=680, height=370)

        #labels and entry
        # attendance id
        id_lable = Label(
            left_inside_frame,
            text="AttendanceID :",
            font=("comicsansms 11 bold"),
            bg="white",
        )
        id_lable.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        id_entry_label = ttk.Entry(
            left_inside_frame,
            width=20,
            textvariable=self.var_atten_id,
            font=("times new roman", 10, "bold"),
        )
        id_entry_label.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        #roll
        rollLabel=Label(left_inside_frame, text="Roll:", bg="white", font="comicsansms 11 bold")
        rollLabel.grid(row=0, column=2, padx=4, pady=8)

        atten_roll=ttk.Entry(left_inside_frame, width=22, textvariable=self.var_atten_roll, font="comicsansms 11 bold")
        atten_roll.grid(row=0, column=3, padx=4, pady=8)

         #name
        nameLabel=Label(left_inside_frame, text="Name:", bg="white", font="comicsansms 11 bold")
        nameLabel.grid(row=1, column=0)

        atten_name=ttk.Entry(left_inside_frame, width=22, textvariable=self.var_atten_name, font="comicsansms 11 bold")
        atten_name.grid(row=1, column=1, pady=8)

        #department
        depLabel=Label(left_inside_frame, text="Department:", bg="white", font="comicsansms 11 bold")
        depLabel.grid(row=1, column=2)

        atten_dep=ttk.Entry(left_inside_frame, width=22, textvariable=self.var_atten_dep, font="comicsansms 11 bold")
        atten_dep.grid(row=1, column=3, pady=8)

        #time
        timeLabel=Label(left_inside_frame, text="Time:", bg="white", font="comicsansms 11 bold")
        timeLabel.grid(row=2, column=0)

        atten_time=ttk.Entry(left_inside_frame, width=22, textvariable=self.var_atten_time, font="comicsansms 11 bold")
        atten_time.grid(row=2, column=1, pady=8)

        #date
        dateLabel=Label(left_inside_frame, text="Date:", bg="white", font="comicsansms 11 bold")
        dateLabel.grid(row=2, column=2)

        atten_date=ttk.Entry(left_inside_frame, width=22, textvariable=self.var_atten_date, font="comicsansms 11 bold")
        atten_date.grid(row=2, column=3, pady=8)

        #attendance
        attendanceLabel=Label(left_inside_frame, text="Attendance Status:", bg="white", font="comicsansms 11 bold")
        attendanceLabel.grid(row=3, column=0)

        self.atten_status=ttk.Combobox(left_inside_frame, width=20, textvariable=self.var_atten_attendance, font="comicsansms 11 bold", state="readonly")
        self.atten_status["values"]=("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # button frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=680, height=35)

        save_btn = Button(btn_frame,text="Import CSV",command=self.importCsv,width=16, font=("times new roman", 13, "bold"),bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame,text="Export CSV",command=self.exportCsv,width=16,font=("times new roman", 13, "bold"),bg="blue",fg="white" )
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame,text="Update",width=16,font=("times new roman", 13, "bold"),bg="blue",fg="white" )
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame,text="Reset",width=16, command=self.reset_data,font=("times new roman", 13, "bold"),bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)


        # right label frame
        right_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Attendance Details",
            font=("times new roman", 12, "bold"),
        )
        right_frame.place(x=750, y=10, width=720, height=620)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=455)

        #==============scroll bar table================
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)
        self.fetchData(mydata)
        
    #====================fetch dataa====================
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)
    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data", "No Data Found to Export", parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write=csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your Data is Exported to "+os.path.basename(fln)+" Successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        row = content["values"]
        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_dep.set(row[3])
        self.var_atten_time.set(row[4])
        self.var_atten_date.set(row[5])
        self.var_atten_attendance.set(row[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")




        

        

    











if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()