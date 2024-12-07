from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1400x710+0+0')
        self.root.title('Face Attendance')
        
        
        #header
        img = Image.open(r"D:\project\face_3rd\project_images\Header.jpg")
        img = img.resize((470, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image = self.photoimg)
        f_lbl.place(x=0,y=0,width=470,height=130)
        
        #second image
        img1 = Image.open(r"D:\project\face_3rd\project_images\students.jpg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image = self.photoimg1)
        f_lbl.place(x=460,y=0,width=500,height=130)
        
        
        #third image
        img2 = Image.open(r"D:\project\face_3rd\project_images\college.jpg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root, image = self.photoimg2)
        f_lbl.place(x=960,y=0,width=500,height=130)
        
        
        #bg image
        bg_img = Image.open(r"D:\project\face_3rd\project_images\bg_image.jpg")
        bg_img = bg_img.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photobg_img = ImageTk.PhotoImage(bg_img)
        
        f_bg_img = Label(self.root, image = self.photobg_img)
        f_bg_img.place(x=0,y=130,width=1530,height=710)
        
        #title
        title_lbl = Label(f_bg_img, text="ATTENDANCE BY FACE RECOGNITION SYSTEM", font=("Roboto Condensed", 35, "bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        #button->student
        button_img1 = Image.open(r"D:\project\face_3rd\project_images\students_button.jpg")
        button_img1 = button_img1.resize((220, 220), Image.Resampling.LANCZOS)
        self.photobutton_img1 = ImageTk.PhotoImage(button_img1)
        
        b1 = Button(f_bg_img, image=self.photobutton_img1,command=self.student_details, cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1 = Button(f_bg_img, text="Student Details",command=self.student_details, cursor="hand2",font=("Roboto Condensed", 15, "bold"),bg="blue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)
        
        
        #button->detect face
        button_img2 = Image.open(r"D:\project\face_3rd\project_images\face_detect.jpg")
        button_img2 = button_img2.resize((220, 220), Image.Resampling.LANCZOS)
        self.photobutton_img2 = ImageTk.PhotoImage(button_img2)
        
        b2 = Button(f_bg_img, image=self.photobutton_img2, cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220)
        
        b2_1 = Button(f_bg_img, text="Face Detection", cursor="hand2",command=self.face_data,font=("Roboto Condensed", 15, "bold"),bg="blue",fg="white")
        b2_1.place(x=500,y=300,width=220,height=40)
        
        
        #button-> Attendance
        button_img3 = Image.open(r"D:\project\face_3rd\project_images\attendance_registry.jpg")
        button_img3 = button_img3.resize((220, 220), Image.Resampling.LANCZOS)
        self.photobutton_img3 = ImageTk.PhotoImage(button_img3)
        
        b3 = Button(f_bg_img, image=self.photobutton_img3, cursor="hand2",command=self.attendance_data)
        b3.place(x=800,y=100,width=220,height=220)
        
        b3_1 = Button(f_bg_img, text="Attendance", cursor="hand2",command=self.attendance_data,font=("Roboto Condensed", 15, "bold"),bg="blue",fg="white")
        b3_1.place(x=800,y=300,width=220,height=40)
        
        
        #button-> helpdesk
        button_img4 = Image.open(r"D:\project\face_3rd\project_images\helpdesk.jpg")
        button_img4 = button_img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photobutton_img4 = ImageTk.PhotoImage(button_img4)
        
        b4 = Button(f_bg_img, image=self.photobutton_img4, cursor="hand2")
        b4.place(x=1100,y=100,width=220,height=220)
        
        b4_1 = Button(f_bg_img, text="Help Desk", cursor="hand2",font=("Roboto Condensed", 15, "bold"),bg="blue",fg="white")
        b4_1.place(x=1100,y=300,width=220,height=40)
        
        
        #button-> Train model
        button_img5 = Image.open(r"D:\project\face_3rd\project_images\trainmodel.jpg")
        button_img5 = button_img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photobutton_img5 = ImageTk.PhotoImage(button_img5)
        
        b5 = Button(f_bg_img, image=self.photobutton_img5, cursor="hand2",command=self.train_data)
        b5.place(x=200,y=340,width=220,height=220)
        
        b5_1 = Button(f_bg_img, text="Train Data", cursor="hand2",command=self.train_data,font=("Roboto Condensed", 15, "bold"),bg="blue",fg="white")
        b5_1.place(x=200,y=540,width=220,height=40)
        
        
        #button-> Take photo
        button_img6 = Image.open(r"D:\project\face_3rd\project_images\capture.jpg")
        button_img6 = button_img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photobutton_img6 = ImageTk.PhotoImage(button_img6)
        
        b6 = Button(f_bg_img, image=self.photobutton_img6, cursor="hand2",command=self.open_img)
        b6.place(x=500,y=340,width=220,height=220)
        
        b6_1 = Button(f_bg_img, text="Show Photos", cursor="hand2",command=self.open_img,font=("Roboto Condensed", 15, "bold"),bg="blue",fg="white")
        b6_1.place(x=500,y=540,width=220,height=40)
        
        
        #button-> developer
        button_img7 = Image.open(r"D:\project\face_3rd\project_images\coder.jpg")
        button_img7 = button_img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photobutton_img7 = ImageTk.PhotoImage(button_img7)
        
        b7 = Button(f_bg_img, image=self.photobutton_img7, cursor="hand2")
        b7.place(x=800,y=340,width=220,height=220)
        
        b7_1 = Button(f_bg_img, text="Developer", cursor="hand2",font=("Roboto Condensed", 15, "bold"),bg="blue",fg="white")
        b7_1.place(x=800,y=540,width=220,height=40)
        
        
        #button-> Exit
        button_img8 = Image.open(r"D:\project\face_3rd\project_images\exit.jpg")
        button_img8 = button_img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photobutton_img8 = ImageTk.PhotoImage(button_img8)
        
        b8 = Button(f_bg_img, image=self.photobutton_img8, cursor="hand2")
        b8.place(x=1100,y=340,width=220,height=220)
        
        b8_1 = Button(f_bg_img, text="EXIT", cursor="hand2",font=("Roboto Condensed", 15, "bold"),bg="blue",fg="white")
        b8_1.place(x=1100,y=540,width=220,height=40)
        
        
    def open_img(self):
        os.startfile("data")
    
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
        
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
        
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()