from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Tk,Entry
from tkinter import messagebox
import mysql.connector
import cv2
import os



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1400x710+0+0')
        self.root.title('Face Attendance')
        
        
        
        
        #variables_db
        
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        
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
        bg_img = bg_img.resize((1430, 710), Image.Resampling.LANCZOS)
        self.photobg_img = ImageTk.PhotoImage(bg_img)
        
        f_bg_img = Label(self.root, image = self.photobg_img)
        f_bg_img.place(x=0,y=130,width=1530,height=710)
        
        #title
        title_lbl = Label(f_bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("Roboto Condensed", 35, "bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        
        #MAIN_FRAME
        main_frame = Frame(f_bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=50,width=1400,height=600)
        
        #____________________________________________________________________________________________________________________________________________________
        
        #left label frame
        Left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font = ("Roboto Condensed", 12, "bold"),bg="white",fg="black")
        Left_frame.place(x=10,y=10,width=660,height=580)
        
        #left frame image
        left_frame_img = Image.open(r"D:\project\face_3rd\project_images\students.jpg")
        left_frame_img = left_frame_img.resize((625, 130), Image.Resampling.LANCZOS)
        self.photoleft_frame_img = ImageTk.PhotoImage(left_frame_img)
        
        left_lbl = Label(Left_frame, image = self.photoleft_frame_img)
        left_lbl.place(x=5,y=0,width=625,height=130)
        
        #current course
        current_course_frame = LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Information",font = ("Roboto Condensed", 12, "bold"),bg="white",fg="black")
        current_course_frame.place(x=5,y=135,width=625,height=115)
        
        
        #Department
        dep_label = Label(current_course_frame,text="Department",font = ("Roboto Condensed", 12, "bold"),bg="white")
        dep_label.grid(row=0, column=0,padx=10)
        
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font = ("Roboto Condensed", 12, "bold"),state="read only")
        dep_combo["values"] = ("Select Department📖","ComputerScience","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10, sticky=W)
        
        
        #Course
        course_label = Label(current_course_frame,text="Course",font = ("Roboto Condensed", 12, "bold"),bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        
        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font = ("Roboto Condensed", 12, "bold"),state="read only")
        course_combo["values"] = ("Select Course📚", "BE", "BCA","BE","AIDS")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #Year
        Year_label = Label(current_course_frame,text="Year",font = ("Roboto Condensed", 12, "bold"),bg="white")
        Year_label.grid(row=1, column=0, padx=10, sticky=W)
        
        Year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font = ("Roboto Condensed", 12, "bold"),state="read only")
        Year_combo["values"] = ("Select Year⏲️", "2020-21", "2021-22","2022-23","2023-24")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #Semester
        Semester_label = Label(current_course_frame,text="Semester",font = ("Roboto Condensed", 12, "bold"),bg="white")
        Semester_label.grid(row=1, column=2, padx=10, sticky=W)
        
        Semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font = ("Roboto Condensed", 12, "bold"),state="read only",width=18)
        Semester_combo["values"] = ("Select Semester✔️", "1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #class student
        Class_student_frame = LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Information",font = ("Roboto Condensed", 12, "bold"),bg="white",fg="black")
        Class_student_frame.place(x=5,y=250,width=625,height=280)
        
        #student ID label
        StudentID_label = Label(Class_student_frame,text="StudentID:",font = ("Roboto Condensed", 13, "bold"),bg="white")
        StudentID_label.grid(row=0, column=0, padx=10, sticky=W)
        
        StudentID_entry = ttk.Entry(Class_student_frame,textvariable=self.var_std_id,width=15,font = ("Roboto Condensed", 13, "bold"))
        StudentID_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        #student Name label
        StudentName_label = Label(Class_student_frame,text="StudentName:",font = ("Roboto Condensed", 13, "bold"),bg="white")
        StudentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        
        StudentName_entry = ttk.Entry(Class_student_frame,textvariable=self.var_std_name,width=15,font = ("Roboto Condensed", 13, "bold"))
        StudentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #class division label
        Class_Division_label = Label(Class_student_frame,text="Class_Division:",font = ("Roboto Condensed", 13, "bold"),bg="white")
        Class_Division_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        
        # Class_Division_entry = ttk.Entry(Class_student_frame,textvariable=self.var_div,width=15,font = ("Roboto Condensed", 13, "bold"))
        # Class_Division_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        div_combo = ttk.Combobox(Class_student_frame,textvariable=self.var_div,font = ("Roboto Condensed", 12, "bold"),state="read only",width=12)
        div_combo["values"] = ("A", "B", "C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        
        #roll numner label
        EnrollmentNo_label = Label(Class_student_frame,text="EnrollmentNo:",font = ("Roboto Condensed", 13, "bold"),bg="white")
        EnrollmentNo_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        
        EnrollmentNo_entry = ttk.Entry(Class_student_frame,textvariable=self.var_roll,width=15,font = ("Roboto Condensed", 13, "bold"))
        EnrollmentNo_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #gender label
        Gender_label = Label(Class_student_frame,text="Gender:",font = ("Roboto Condensed", 13, "bold"),bg="white")
        Gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        
        # Gender_entry = ttk.Entry(Class_student_frame,textvariable=self.var_gender,width=15,font = ("Roboto Condensed", 13, "bold"))
        # Gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        Gender_combo = ttk.Combobox(Class_student_frame,textvariable=self.var_gender,font = ("Roboto Condensed", 12, "bold"),state="read only",width=12)
        Gender_combo["values"] = ("Male ♂️", "Female ♀️", "Others")
        Gender_combo.current(0)
        Gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        #DOB label
        DOB_label = Label(Class_student_frame,text="DOB:",font = ("Roboto Condensed", 13, "bold"),bg="white")
        DOB_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        
        DOB_entry = ttk.Entry(Class_student_frame,textvariable=self.var_dob,width=15,font = ("Roboto Condensed", 13, "bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #email label
        Email_label = Label(Class_student_frame,text="Email:",font = ("Roboto Condensed", 13, "bold"),bg="white")
        Email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        
        Email_entry = ttk.Entry(Class_student_frame,textvariable=self.var_email,width=15,font = ("Roboto Condensed", 13, "bold"))
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #phoneno label
        PhoneNo_label = Label(Class_student_frame,text="PhoneNo:",font = ("Roboto Condensed", 13, "bold"),bg="white")
        PhoneNo_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        
        PhoneNo_entry = ttk.Entry(Class_student_frame,textvariable=self.var_phone,width=15,font = ("Roboto Condensed", 13, "bold"))
        PhoneNo_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #address label
        Address_label = Label(Class_student_frame,text="Address:",font = ("Roboto Condensed", 13, "bold"),bg="white")
        Address_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        
        Address_entry = ttk.Entry(Class_student_frame,textvariable=self.var_address,width=15,font = ("Roboto Condensed", 13, "bold"))
        Address_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #teachname label
        teacher_label = Label(Class_student_frame,text="Teacher:",font = ("Roboto Condensed", 13, "bold"),bg="white")
        teacher_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        
        teacher_entry = ttk.Entry(Class_student_frame,textvariable=self.var_teacher,width=15,font = ("Roboto Condensed", 13, "bold"))
        teacher_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(Class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)
        #button2
        radiobtn2 = ttk.Radiobutton(Class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)
        
        #button_frame
        btn_frame = Frame(Class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=620,height=30)
        
        
        #save data
        save_btn = Button(btn_frame,text="Save",command=self.add_data,font = ("Roboto Condensed", 13, "bold"),bg="green",fg="white",width=15)
        save_btn.grid(row=0,column=0)
        
        # update
        Update_btn = Button(btn_frame,text="Update",command=self.update_data,font = ("Roboto Condensed", 13, "bold"),bg="green",fg="white",width=15)
        Update_btn.grid(row=0,column=1)
        
        # delete
        Delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,font = ("Roboto Condensed", 13, "bold"),bg="green",fg="white",width=15)
        Delete_btn.grid(row=0,column=2)
        
        # reset
        Reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,font = ("Roboto Condensed", 13, "bold"),bg="green",fg="white",width=15)
        Reset_btn.grid(row=0,column=3)
        
        
        btn_frame1 = Frame(Class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=237,width=620,height=28)
        # Take_Photo
        Take_Photo_btn = Button(btn_frame1,command=self.generate_dataset,text="Take_Photo",font = ("Roboto Condensed", 13, "bold"),bg="green",fg="white",width=30)
        Take_Photo_btn.grid(row=0,column=0)
        
        # Update_Photo
        Update_Photo_btn = Button(btn_frame1,text="Update_Photo",font = ("Roboto Condensed", 13, "bold"),bg="green",fg="white",width=30)
        Update_Photo_btn.grid(row=0,column=1)
               
        #____________________________________________________________________________________________________________________________________________________
        
        
        #right label frame
        Right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font = ("Roboto Condensed", 12, "bold"),bg="white",fg="black")
        Right_frame.place(x=675,y=10,width=660,height=580)
        
        
        #right frame image
        Right_frame_img = Image.open(r"D:\project\face_3rd\project_images\college_image.jpg")
        Right_frame_img = Right_frame_img.resize((625, 130), Image.Resampling.LANCZOS)
        self.photoRight_frame_img = ImageTk.PhotoImage(Right_frame_img)
        
        Right_lbl = Label(Right_frame, image = self.photoRight_frame_img)
        Right_lbl.place(x=5,y=0,width=625,height=130)
        
        
        #search System
        Search_frame = LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font = ("Roboto Condensed", 12, "bold"),bg="white",fg="black")
        Search_frame.place(x=5,y=135,width=625,height=70)
        
        SearchBar_label = Label(Search_frame,text="Search:",font = ("Roboto Condensed", 15, "bold"),bg="yellow")
        SearchBar_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        
        SearchBox_combo = ttk.Combobox(Search_frame,font = ("Roboto Condensed", 12, "bold"),state="read only",width=12)
        SearchBox_combo["values"] = ("Select✔️", "Roll_No","Phone_No","3rd","4th","5th","6th","7th","8th","9th","10th")
        SearchBox_combo.current(0)
        SearchBox_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        Search_entry = ttk.Entry(Search_frame,width=15,font = ("Roboto Condensed", 13, "bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        
        Search_btn = Button(Search_frame,text="Search",font = ("Roboto Condensed", 13, "bold"),bg="green",fg="white",width=10)
        Search_btn.grid(row=0,column=3,padx=2)
        
        ShowAll_btn = Button(Search_frame,text="ShowAll",font = ("Roboto Condensed", 13, "bold"),bg="green",fg="white",width=10)
        ShowAll_btn.grid(row=0,column=4,padx=2)
        
        
        #Table Frame
        Table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        Table_frame.place(x=5, y=210, width=625, height=300)
        
        scroll_x = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.student_table = ttk.Treeview(Table_frame,columns=("Department","Course","Year","Sem","ID","Name","Division","Roll","Gender","DOB","Email","Gender","Phone","Teacher","Photo"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Sem")
        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Division",text="Division")
        self.student_table.heading("Roll",text="Roll")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"] = "headings"
        
        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Division",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
    
    #function for db    
    def add_data(self):
        # Check if required fields are empty or have invalid values
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are necessary and must be filled", parent=self.root)
        else:
            try:
                # Establishing connection
                conn = mysql.connector.connect(
                    host="127.0.0.1", 
                    port=3306, 
                    username="root", 
                    password="manas123", 
                    database="face_recognizer"
                )

                # Corrected cursor initialization (missing parentheses)
                my_cursor = conn.cursor()  # Add parentheses here to call cursor() method

                # SQL query to insert data
                query = """
                    INSERT INTO Students 
                    (Dep, course, Year, Semester, Student_id, Name, Division, Roll, Gender, Dob, Email, Phone, Address, Teacher, PhotoSample)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                )

                # Execute the SQL query
                my_cursor.execute(query, values)

                # Committing the transaction
                conn.commit()
                self.fetch_data()

                # Closing the connection
                conn.close()

                # Showing success message
                messagebox.showinfo("Success", "Details added successfully", parent=self.root)
            
            except mysql.connector.Error as db_error:
                # Handling MySQL-specific exceptions
                messagebox.showerror("Database Error", f"Error occurred: {db_error}", parent=self.root)
            except Exception as e:
                # Handling any other exceptions
                messagebox.showerror("Error", f"An unexpected error occurred: {e}", parent=self.root)
                
    def fetch_data(self):
        try:
            # Establishing connection
            conn = mysql.connector.connect(
                    host="127.0.0.1", 
                    port=3306, 
                    username="root", 
                    password="manas123", 
                    database="face_recognizer"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM Students")
            data = my_cursor.fetchall()
            
            # Check if data is returned from the database
            if len(data) != 0:
                # Clear existing data in the table before adding new ones
                self.student_table.delete(*self.student_table.get_children())
                
                # Insert all rows from the database into the table widget
                for i in data:
                    self.student_table.insert("", END, values=i)
                
                conn.commit()
            
            conn.close()
        
        except mysql.connector.Error as db_error:
            # Handle database errors
            messagebox.showerror("Database Error", f"Error occurred: {db_error}", parent=self.root)
        except Exception as e:
            # Handle other general errors
            messagebox.showerror("Error", f"An unexpected error occurred: {e}", parent=self.root)
            
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        
        self.var_dep.set(data[0])
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are necessary and must be filled", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update the student details?", parent=self.root)
                if Update:
                    conn = mysql.connector.connect(
                        host="127.0.0.1", 
                        port=3306, 
                        username="root", 
                        password="manas123", 
                        database="face_recognizer"
                    )
                    my_cursor = conn.cursor()

                    # Check if Student ID exists
                    my_cursor.execute("SELECT * FROM Students WHERE Student_id=%s", (self.var_std_id.get(),))
                    result = my_cursor.fetchone()
                    
                    if not result:
                        messagebox.showerror("Error", "Student ID not found.", parent=self.root)
                        conn.close()
                        return

                    # Corrected query
                    query = """UPDATE Students 
                            SET Dep=%s, Course=%s, Year=%s, Semester=%s, Division=%s, 
                                Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, 
                                Address=%s, Teacher=%s, PhotoSample=%s 
                            WHERE Student_id=%s"""

                    values = (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    )

                    print("Attempting Update with values:", values)
                    my_cursor.execute(query, values)
                    print("Rows affected:", my_cursor.rowcount)

                    if my_cursor.rowcount == 0:
                        messagebox.showwarning("Warning", "No records updated. Check input data.", parent=self.root)
                    else:
                        conn.commit()
                        messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)

                    self.fetch_data()
                    conn.close()
                else:
                    return 
            except mysql.connector.Error as err:
                messagebox.showerror("SQL Error", f"Error: {err}", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


                
                
                
                
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete", "Do you want to delete the student data?", parent=self.root)
                if delete:
                    conn = mysql.connector.connect(
                        host="127.0.0.1", 
                        port=3306, 
                        username="root", 
                        password="manas123", 
                        database="face_recognizer"
                    )
                    my_cursor = conn.cursor()

                    # Corrected table name
                    sql = "DELETE FROM Students WHERE Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Delete", "Successfully Deleted Student Data", parent=self.root)
                else:
                    return
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error Code: {err.errno}\nMessage: {err.msg}", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    #generate dataset and make samples
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are necessary and must be filled", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                        host="127.0.0.1", 
                        port=3306, 
                        username="root", 
                        password="manas123", 
                        database="face_recognizer"
                    )
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from Students")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id+=1
                my_cursor.execute("SELECT * FROM Students WHERE Student_id=%s", (self.var_std_id.get(),))
                result = my_cursor.fetchone()
                    
                if not result:
                    messagebox.showerror("Error", "Student ID not found.", parent=self.root)
                    conn.close()
                    return

                # Corrected query
                query = """UPDATE Students 
                            SET Dep=%s, Course=%s, Year=%s, Semester=%s, Division=%s, 
                                Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, 
                                Address=%s, Teacher=%s, PhotoSample=%s 
                            WHERE Student_id=%s"""

                values = (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()==id+1
                    )
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #load xml harrcascade
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # 1.3 is the scalimg factor
                    # 5 is the Minimum neighbours
                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id +=1 
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face", face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break  
                    
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset Completed successfully.")  
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    
            
                    
            

                
                
                
                
                
                

        
            
        
        

        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()