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
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1400x710+0+0')
        self.root.title('Face Attendance')
        
        
        #==========================variables============================
        self.var_atten_id = StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        
        img = Image.open(r"D:\project\face_3rd\project_images\college.jpg")
        img = img.resize((750, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image = self.photoimg)
        f_lbl.place(x=0,y=0,width=750,height=150)
        
        #second image
        img1 = Image.open(r"D:\project\face_3rd\project_images\students.jpg")
        img1 = img1.resize((800, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image = self.photoimg1)
        f_lbl.place(x=750,y=0,width=800,height=150)
        
        #bg_img
        bg_img = Image.open(r"D:\project\face_3rd\project_images\bg_image.jpg")
        bg_img = bg_img.resize((1430, 710), Image.Resampling.LANCZOS)
        self.photobg_img = ImageTk.PhotoImage(bg_img)
        
        f_bg_img = Label(self.root, image = self.photobg_img)
        f_bg_img.place(x=0,y=150,width=1430,height=710)
        
        title_lbl = Label(f_bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("Roboto Condensed", 35, "bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1430,height=50)
        
        #MAIN_FRAME
        main_frame = Frame(f_bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=55,width=1400,height=600)
        #left label frame
        Left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font = ("Roboto Condensed", 12, "bold"),bg="white",fg="black")
        Left_frame.place(x=10,y=10,width=660,height=580)
        
        #left image
        left_frame_img = Image.open(r"D:\project\face_3rd\project_images\students.jpg")
        left_frame_img = left_frame_img.resize((650, 130), Image.Resampling.LANCZOS)
        self.photoleft_frame_img = ImageTk.PhotoImage(left_frame_img)
        left_lbl = Label(Left_frame, image = self.photoleft_frame_img)
        left_lbl.place(x=5,y=0,width=650,height=130)
        
        Left_Inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        Left_Inside_frame.place(x=0,y=133,width=650,height=300)
        
        #labels and entry
        
        #sAttendance ID label
        AttendanceID_label = Label(Left_Inside_frame,text="AttendanceID:",font = ("Roboto Condensed", 13, "bold"),bg="white")
        AttendanceID_label.grid(row=0, column=0, padx=10, sticky=W)
        
        AttendanceID_entry = ttk.Entry(Left_Inside_frame,textvariable=self.var_atten_id,width=15,font = ("Roboto Condensed", 13, "bold"))
        AttendanceID_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        
        #student Name label
        StudentName_label = Label(Left_Inside_frame,text="Roll:",font = ("Roboto Condensed", 13, "bold"),bg="white")
        StudentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        
        StudentName_entry = ttk.Entry(Left_Inside_frame,textvariable=self.var_atten_dep,width=15,font = ("Roboto Condensed", 13, "bold"))
        StudentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #Name
        Name_label = Label(Left_Inside_frame,text="Name:",font = ("Roboto Condensed", 13, "bold"),bg="white")
        Name_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        
        Name_entry = ttk.Entry(Left_Inside_frame,textvariable=self.var_atten_name,width=15,font = ("Roboto Condensed", 13, "bold"))
        Name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #Department
        Department_label = Label(Left_Inside_frame,text="Department:",font = ("Roboto Condensed", 13, "bold"),bg="white")
        Department_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        
        Department_entry = ttk.Entry(Left_Inside_frame,textvariable=self.var_atten_roll,width=15,font = ("Roboto Condensed", 13, "bold"))
        Department_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #Time
        Time_label = Label(Left_Inside_frame,text="Time:",font = ("Roboto Condensed", 13, "bold"),bg="white")
        Time_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        
        Time_entry = ttk.Entry(Left_Inside_frame,textvariable=self.var_atten_date,width=15,font = ("Roboto Condensed", 13, "bold"))
        Time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #Date
        Date_label = Label(Left_Inside_frame,text="Date:",font = ("Roboto Condensed", 13, "bold"),bg="white")
        Date_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        
        Date_entry = ttk.Entry(Left_Inside_frame,textvariable=self.var_atten_time,width=15,font = ("Roboto Condensed", 13, "bold"))
        Date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #attendance
        attendanceLabel = Label(Left_Inside_frame,text="Attendance Status",bg="white",font="comicsans 11 bold")
        attendanceLabel.grid(row=3,column=0)
        
        self.atten_status = ttk.Combobox(Left_Inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsans 11 bold",state="readonly")
        self.atten_status["values"] = ("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
        #button_frame
        btn_frame = Frame(Left_Inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=620,height=30)
        
        
        #save data
        save_btn = Button(btn_frame,text="Import CSV",command=self.importCSV,font = ("Roboto Condensed", 13, "bold"),bg="green",fg="white",width=15)
        save_btn.grid(row=0,column=0)
        
        # update
        Update_btn = Button(btn_frame,text="Export CSV",command=self.exportCSV,font = ("Roboto Condensed", 13, "bold"),bg="green",fg="white",width=15)
        Update_btn.grid(row=0,column=1)
        
        # delete
        Delete_btn = Button(btn_frame,text="Update",font = ("Roboto Condensed", 13, "bold"),bg="green",fg="white",width=15)
        Delete_btn.grid(row=0,column=2)
        
        # reset
        Reset_btn = Button(btn_frame,command=self.reset_data,text="Reset",font = ("Roboto Condensed", 13, "bold"),bg="green",fg="white",width=15)
        Reset_btn.grid(row=0,column=3)
        
        
        
        #right label frame
        Right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font = ("Roboto Condensed", 12, "bold"),bg="white",fg="black")
        Right_frame.place(x=675,y=10,width=660,height=580)
        
        #button_frame
        Table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        Table_frame.place(x=5,y=2,width=650,height=445)
        
        #scrollbar and all
        scroll_x = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable = ttk.Treeview(Table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
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
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
        
    #=======================================fetch data=================================
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
            
    def importCSV(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")],
            parent=self.root
        )
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
    
    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No DATA found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Open CSV",
                filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")],
                parent=self.root
            )
            with open(fln,mode="w",newline="\n") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(1)
                messagebox.showinfo("Data Exported","Your data is exported to "+os.path.basename(fln)+" successsfully",parent=self.root)
                
        except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                
    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
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