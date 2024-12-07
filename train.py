from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Tk,Entry
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1400x710+0+0')
        self.root.title('Face Attendance')
        
        title_lbl = Label(self.root, text="TRAIN DATASET", font=("Roboto Condensed", 35, "bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top_train = Image.open(r"D:\project\face_3rd\project_images\students.jpg")
        img_top_train = img_top_train.resize((1500, 380), Image.Resampling.LANCZOS)
        self.photoimg_top_train = ImageTk.PhotoImage(img_top_train)
        
        left_lbl = Label(self.root, image = self.photoimg_top_train)
        left_lbl.place(x=0,y=45,width=1500,height=350)
        
        #button in the middle
        b1_1 = Button(self.root, text="Train Data",command=self.train_classifier, cursor="hand2",font=("Roboto Condensed", 30, "bold"),bg="green",fg="white")
        b1_1.place(x=0,y=390,width=1530,height=40)
        
        img_bottom_train = Image.open(r"D:\project\face_3rd\project_images\chinese.jpg")
        img_bottom_train = img_bottom_train.resize((1500, 410), Image.Resampling.LANCZOS)
        self.photoimg_bottom_train = ImageTk.PhotoImage(img_bottom_train)
        
        left_lbl = Label(self.root, image = self.photoimg_bottom_train)
        left_lbl.place(x=0,y=430,width=1500,height=380)
        
        
    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        
        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            
            cv2.imshow("Training...",imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)
        
        #train the classifier LBPH
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("Classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed!!!")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()