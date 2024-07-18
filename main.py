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

        title_lbl = Label(f_lbl, text = "ATTENDANCE SYSTEM BASED ON FACE RECOGNITION", font=("times new roman", 30, "bold"),bg="white",fg="purple")
        title_lbl.place(x=25,y=25,width = 1300,height = 90)

        #Background image.
        img2 = Image.open(r"C:\Users\shwet\OneDrive\Desktop\Face-Recognition-Attendance-System\Images\background.jpg")
        img2 = img2.resize((1366,640),Image.Resampling.LANCZOS) 
        self.photoimg2 = ImageTk.PhotoImage(img2)





if __name__=="__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()