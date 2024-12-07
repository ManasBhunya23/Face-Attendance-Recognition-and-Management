from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Tk,Entry
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
import numpy as np
from time import strftime
from datetime import datetime
from tkinter import filedialog



mydata = []
class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1400x710+0+0')
        self.root.title('Face Recognition')
        
        title_lbl = Label(self.root, text="DEVELOPER", font=("Roboto Condensed", 35, "bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        main_frame = Frame(self.root,bd=2,bg="white")
        main_frame.place(x=480,y=50,width=500,height=600)
        
        img = Image.open(r"D:\project\face_3rd\project_images\manas.jpg")
        img = img.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(main_frame, image = self.photoimg)
        f_lbl.place(x=290,y=0,width=200,height=200)
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()