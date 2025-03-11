from cProfile import label
from cgitb import text
from email.mime import image
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



if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()