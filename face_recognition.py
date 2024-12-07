from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Tk,Entry
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1400x710+0+0')
        self.root.title('Face Attendance')
        
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("Roboto Condensed", 35, "bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_left_train = Image.open(r"D:\project\face_3rd\project_images\college.jpg")
        img_left_train = img_left_train.resize((690, 700), Image.Resampling.LANCZOS)
        self.photoimg_left_train = ImageTk.PhotoImage(img_left_train)
        
        left_lbl = Label(self.root, image = self.photoimg_left_train)
        left_lbl.place(x=0,y=45,width=690,height=700)
        
        
        img_right_train = Image.open(r"D:\project\face_3rd\project_images\face_detect.jpg")
        img_right_train = img_right_train.resize((695, 700), Image.Resampling.LANCZOS)
        self.photoimg_right_train = ImageTk.PhotoImage(img_right_train)
        
        left_lbl = Label(self.root, image = self.photoimg_right_train)
        left_lbl.place(x=690,y=45,width=695,height=700)
        
        #button in the middle
        b1_1 = Button(left_lbl, text="Face Recognition", cursor="hand2",font=("Roboto Condensed", 18, "bold"), bg="green", fg="white",command=self.face_recog)
        b1_1.place(x=365, y=620, width=220, height=40)
        
    #=============================================================================
    def mark_attendance(self, student_id, name, roll, department, img, x, y, w, h):
        try:
            file_name = "Attendance.csv"
            now = datetime.now()
            date_str = now.strftime("%d/%m/%Y")
            time_str = now.strftime("%H:%M:%S")

            # Check and avoid duplicates
            with open(file_name, "r+", newline="\n") as f:
                myDataList = f.readlines()
                attendance_list = [line.strip().split(",") for line in myDataList]

                already_marked = any(
                    entry[0] == str(student_id) and entry[1] == roll and entry[2] == name and entry[3] == department and entry[4] == date_str
                    for entry in attendance_list
                )

                if not already_marked:
                    f.writelines(f"\n{student_id},{roll},{name},{department},{date_str},{time_str},Present")
                    
                    # Display tick on webcam feed
                    cv2.putText(
                        img, "Present", (x, y + h + 25),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2
                    )
                    print(f"Attendance Marked for: {name}, Roll: {roll}")

        except Exception as e:
            print(f"Error marking attendance: {e}")

                   
        
    #face_recognition
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)

            conn = mysql.connector.connect(
                host="127.0.0.1", 
                port=3306, 
                username="root", 
                password="manas123", 
                database="face_recognizer"
            )
            my_cursor = conn.cursor()

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

                id, predict = clf.predict(gray_img[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                if confidence > 75:
                    my_cursor.execute("SELECT Student_id, Name, dep, Roll FROM Students WHERE Student_id=%s", (id,))
                    result = my_cursor.fetchone()

                    if result:
                        student_id, name, roll, department = result
                        print(f"Detected: Student_id={student_id}, Name={name}, Roll={roll}, Department={department}")

                        # Draw text on the frame
                        cv2.putText(img, f"ID: {student_id}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f"Name: {name}", (x, y - 50), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f"Roll: {roll}", (x, y - 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f"Dept: {department}", (x, y - 1), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

                        # Call mark_attendance with required parameters
                        self.mark_attendance(student_id, name, roll, department, img, x, y, w, h)
                    else:
                        cv2.putText(img, "Unknown", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)
                else:
                    cv2.putText(img, "Unknown", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

            conn.close()
            return img


        def recognize(img, clf, faceCascade):
            return draw_boundary(img, faceCascade, 1.1, 10, clf)

        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("Classifier.xml")

        video_cap = cv2.VideoCapture(0)
        cv2.namedWindow("Face Recognition", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Face Recognition", 800, 600)

        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Failed to capture frame from webcam")
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Exit on 'Enter' key
                break

        video_cap.release()
        cv2.destroyAllWindows()

                    
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()