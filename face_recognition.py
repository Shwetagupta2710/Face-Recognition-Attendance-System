from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("{width}x{height}+0+0".format(width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight()))
        self.root.title("Face Recognition System")

        full_screen_width = self.root.winfo_screenwidth()
        desired_width = full_screen_width // 3
        lower_img_height=self.root.winfo_screenheight()-298

        title_lbl = Label(self.root, text="FACE RECOGNITION",
                          font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=full_screen_width, height=38)
        
        #1st image
        img_top = Image.open("images/face.jpeg")
        img_top = img_top.resize((800, 800), Image.LANCZOS)
        self.photoimage_top = ImageTk.PhotoImage(img_top)

        top_lbl = Label(self.root, image=self.photoimage_top)
        top_lbl.place(x=0, y=55, width=800, height=800)

        #2nd image
        img_bottom = Image.open("images/face1.jpeg")
        img_bottom = img_bottom.resize((950, 800), Image.LANCZOS)
        self.photoimage_bottom = ImageTk.PhotoImage(img_bottom)

        bottom_lbl = Label(self.root, image=self.photoimage_bottom)
        bottom_lbl.place(x=750, y=55, width=950, height=800)

        but1 = Button(bottom_lbl, text="FACE RECOGNITION", cursor="hand2", command=self.face_recog, font=("times new roman", 14, "bold"), bg="darkgreen",
                      fg="white")
        but1.place(x=365, y=620, width=220, height=40)

    #=====face recognition======
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            
            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])

                confidence = int((100*(1-predict/300)))
                conn = mysql.connector.connect(
                        host="localhost", user="root", password="Shweta@2710", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_iD="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Dep from student where Student_iD="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("select RollNum from student where Student_iD="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                if confidence>77:
                    cv2.putText(img, f"Roll:{r}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Name:{n}", (x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Department:{d}", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                else:
                    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 3)
                    cv2.putText(img, "Unknown Face", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)

                coord=[x,y,w,y]
            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()