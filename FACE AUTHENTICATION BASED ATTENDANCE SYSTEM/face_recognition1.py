from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import cv2
from datetime import datetime
from tkinter import messagebox
import numpy as np
import pandas as pd
import csv



class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.checked_in_students = set()
        self.window_open = True
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.root.wm_iconbitmap("desktop.ico")
        

        # Open database connection
        self.conn = mysql.connector.connect(host="localhost", username="root", password="Mysql@ybh1", database="face_recognizer")
        self.my_cursor = self.conn.cursor()
        
        self.video_cap = cv2.VideoCapture(0)  # Initialize video capture

        title_lbl = Label(self.root, text="Take your attendance here !!! ", font=("verdana", 28, "bold"), bg="yellow", fg="navy")
        title_lbl.place(x=0, y=0, width=1366, height=45)
        # first image
       

        # button
        Button_btn2 = Button(root,text="Check-in", command=self.face_recog, font=("arial", 18, "bold"), bg="green", fg="white", bd=0, relief=FLAT)
        Button_btn2.place(x=500, y=300, width=300, height=100, bordermode="outside", anchor="center")

        Button_btn3 = Button(root,text="Check-out", command=self.face_check_out, font=("arial", 18, "bold"), bg="red", fg="white", bd=0, relief=FLAT)
        Button_btn3.place(x=850, y=300, width=300, height=100, bordermode="outside", anchor="center")

    

   

    def face_recog(self):
     faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
     clf = cv2.face.LBPHFaceRecognizer_create()
     clf.read("Classifier.xml")

     video_cap = cv2.VideoCapture(0)

     while self.window_open:
        ret, img = video_cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Flag to track if a recognized face is found
        face_found = False

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, predict = clf.predict(gray[y:y + h, x:x + w])
            confidence = int((100 * (1 - predict / 300)))

            if confidence > 77:
                face_found = True  # Set the flag to indicate a recognized face is found

                self.my_cursor.execute("Select `Student Name` from student where `Student ID`=" + str(id))
                n = self.my_cursor.fetchone()
                n = "+".join(n)

                self.my_cursor.execute("Select `Roll No.` from student where `Student ID`=" + str(id))
                r = self.my_cursor.fetchone()
                r = "+".join(r)

                self.my_cursor.execute("Select Dep from student where `Student ID`=" + str(id))
                d = self.my_cursor.fetchone()
                d = "+".join(d)

                self.my_cursor.execute("Select `Student ID` from student where `Student ID`=" + str(id))
                i = self.my_cursor.fetchone()
                i = "+".join(i)

                # Use face_recognition library to detect landmarks
                

                cv2.putText(img, f"Student ID: {i}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Roll No.: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                if self.mark_attendance(i, r, n, d):
                    print("Attendance marked for:", n)
                else:
                    print("Failed to mark attendance for:", n)

        if not face_found:
            # Display "Unknown Face" only if no recognized faces are found
            cv2.putText(img, f"Unknown Face", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

        cv2.imshow("Face Recognition", img)
        key = cv2.waitKey(1)
        if key == 13 or key == 27:  # Enter key or Escape key
            break

     video_cap.release()
     cv2.destroyAllWindows()



     

    def face_check_out(self):
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("Classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while self.window_open:
            ret, img = video_cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
             id, predict = clf.predict(gray[y:y + h, x:x + w])
             confidence = int((100 * (1 - predict / 300)))

             if confidence > 77:
                self.my_cursor.execute("SELECT * FROM student WHERE `Student ID` = %s", (id,))
                result = self.my_cursor.fetchone()

                if result:
                    student_id = result[4]
                    roll_no = result[6]
                    student_name = result[5]
                    department = result[0]

                    now = datetime.now()
                    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

                    # Update checkout time regardless of existing entry
                    self.my_cursor.execute("UPDATE attendance SET `Checkout Time` = %s WHERE `Student ID` = %s", (dt_string, student_id))
                    self.conn.commit()

                    cv2.putText(img, f"Student ID: {student_id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll No.: {roll_no}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {student_name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {department}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

            cv2.imshow("Face Recognition", img)
            key = cv2.waitKey(1)
            if key == 13 or key == 27:  # Enter key or Escape key
             break

        video_cap.release()
        cv2.destroyAllWindows()



    def mark_attendance(self, i, r, n, d):
     now = datetime.now()
     dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

     try:
        self.my_cursor.execute("SELECT * FROM attendance WHERE `Student ID` = %s AND Date = %s", (i, now.strftime("%Y-%m-%d")))
        result = self.my_cursor.fetchone()

        if not result:
            self.my_cursor.execute("INSERT INTO attendance (Dep, `Student Name`, `Student ID`, `Roll No.`, Date, `Checkin Time`,`Checkout Time`, Status) VALUES (%s,%s, %s, %s, %s, %s, %s, %s)", (d, n, i, r, now.strftime("%Y-%m-%d"), dt_string, "", "Present"))
            self.conn.commit()
            self.checked_in_students.add(i)
            messagebox.showinfo("Success", "Attendance marked successfully.")
        else:
            messagebox.showerror("Error", "Attendance already marked for today.")
     except mysql.connector.Error as err:
      messagebox.showerror("Error", f"Error marking attendance: {err}")

    # Reinitialize the camera capture
     self.video_cap = cv2.VideoCapture(0)
    # Reset the window_open flag
     self.window_open = True




    def on_closing(self):
        self.window_open = False
        self.root.destroy()

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
