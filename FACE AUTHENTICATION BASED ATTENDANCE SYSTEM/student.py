from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import tkinter




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Registration")
        self.root.wm_iconbitmap("desktop.ico")
        
        
        #Variables
        self.var_dep=StringVar()
        self.var_batch=StringVar()
        self.var_semester=StringVar()
        self.var_section=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_dob=StringVar()


        frame=tkinter.Frame(root, width=1200, height=800)
        frame.pack()

        # Set font style to Times New Roman and bold
        font_style = ("Times New Roman", 15, "bold")



# Saving User Info
        user_info_frame =tkinter.LabelFrame(frame, text="Student Information")
        user_info_frame.grid(row= 0, column=0, padx=20, pady=10)
        
        #DEP
        dep_label = tkinter.Label(user_info_frame, text="Department",font=font_style)
        dep_combobox = ttk.Combobox(user_info_frame, textvariable=self.var_dep,values=["Select Department","CSIT", "BCA", "BIT"])
        dep_combobox.current(0)
        dep_label.grid(row=0, column=0)
        dep_combobox.grid(row=1, column=0)
        
        #batch
        batch_label = tkinter.Label(user_info_frame, text="Batch",font=font_style)
        batch_combobox = ttk.Combobox(user_info_frame, textvariable=self.var_batch,values=["Select Batch","2076", "2077", "2078"])
        batch_combobox.current(0)
        batch_label.grid(row=0, column=1)
        batch_combobox.grid(row=1, column=1)
        
        #Semester
        semester_label = tkinter.Label(user_info_frame, text="Semester",font=font_style)
        semester_combobox = ttk.Combobox(user_info_frame, textvariable=self.var_semester,values=["Select Semester","I", "II", "III", "IV", "V", "VI", "VII","VIII"])
        semester_combobox.current(0)
        semester_label.grid(row=0, column=2)
        semester_combobox.grid(row=1, column=2)
        
        #section
        section_label = tkinter.Label(user_info_frame, text="Section",font=font_style)
        section_combobox = ttk.Combobox(user_info_frame, textvariable=self.var_section,values=["Select Section","A", "B", "C", "D"])
        section_combobox.current(0)
        section_label.grid(row=0, column=3)
        section_combobox.grid(row=1, column=3)
        
        #id
        id_label = tkinter.Label(user_info_frame, text="Student ID",font=font_style)
        id_label.grid(row=2, column=0)
        id_entry = tkinter.Entry(user_info_frame,textvariable=self.var_std_id)
        id_entry.grid(row=3, column=0)
        
        
        #name
        name_label = tkinter.Label(user_info_frame, text="Name",font=font_style)
        name_label.grid(row=2, column=1)
        name_entry = tkinter.Entry(user_info_frame,textvariable=self.var_std_name)
        name_entry.grid(row=3,column=1)
        

        #roll
        roll_label = tkinter.Label(user_info_frame, text="Roll No.",font=font_style)
        roll_label.grid(row=2, column=2)
        roll_entry = tkinter.Entry(user_info_frame,textvariable=self.var_roll)
        roll_entry.grid(row=3, column=2)
        
        #GENDER
        Gender_label = tkinter.Label(user_info_frame, text="Gender",font=font_style)
        Gender_combobox = ttk.Combobox(user_info_frame,textvariable=self.var_gender, values=["Select Gender","Male", "Female"])
        Gender_combobox.current(0)
        Gender_label.grid(row=2, column=3)
        Gender_combobox.grid(row=3, column=3)
        
        #EMAIL
        email_label = tkinter.Label(user_info_frame, text="E-mail",font=font_style)
        email_label.grid(row=4, column=0)
        email_entry = tkinter.Entry(user_info_frame,textvariable=self.var_email)
        email_entry.grid(row=5,column=0)
        
        #phone number
        Phone_label = tkinter.Label(user_info_frame, text="Phone No",font=font_style)
        Phone_label.grid(row=4, column=1)
        Phone_entry = tkinter.Entry(user_info_frame,textvariable=self.var_phone)
        Phone_entry.grid(row=5, column=1)
        
        #adress
        Address_label = tkinter.Label(user_info_frame, text="Address",font=font_style)
        Address_label.grid(row=4, column=2)
        Address_entry = tkinter.Entry(user_info_frame,textvariable=self.var_address)
        Address_entry.grid(row=5, column=2)
        
        
        #DOB
        DOB_label = tkinter.Label(user_info_frame, text="DOB",font=font_style)
        DOB_label.grid(row=4, column=3)
        DOB_entry = tkinter.Entry(user_info_frame,textvariable=self.var_dob)
        DOB_entry.grid(row=5, column=3)
        

        

        

        for widget in user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)
        courses_frame = tkinter.LabelFrame(frame)
        courses_frame.grid(row=11, column=0, sticky="news", padx=20, pady=10)
        space_label = tkinter.Label(user_info_frame, text="", font=font_style)
        space_label.grid(row=7, column=4)

        # Create a new frame for radio buttons and buttons
        buttons_frame = tkinter.LabelFrame(frame, text="Actions")
        buttons_frame.grid(row=0, column=1, padx=20, pady=10, rowspan=12)

        # Radio buttons
        
        self.var_radio1 = tkinter.StringVar(value="NO")
        

        radio_button1 = tkinter.Radiobutton(buttons_frame,variable=self.var_radio1, text="Take Photo Sample", value="Yes", font=font_style,fg="blue")
        radio_button2 = tkinter.Radiobutton(buttons_frame,variable=self.var_radio1, text="No Photo Sample", value="No", font=font_style,fg="blue")

        radio_button1.pack(anchor="w", padx=10, pady=5)
        radio_button2.pack(anchor="w", padx=10, pady=5)

        # Normal buttons
        button1 = tkinter.Button(buttons_frame, text="Save",command=self.add_data, font=font_style,fg="blue")
        button2 = tkinter.Button(buttons_frame, text="Update",command=self.update_data, font=font_style,fg="blue")
        button3 = tkinter.Button(buttons_frame, text="Delete",command=self.delete_data, font=font_style,fg="red")
        button4 = tkinter.Button(buttons_frame, text="Reset", command=self.reset_data,font=font_style,fg="blue")
        button5 = tkinter.Button(buttons_frame, text="Take your photo",command=self.generate_dataset, font=font_style,fg="navy")

        button1.pack(fill="x", padx=10, pady=5)
        button2.pack(fill="x", padx=10, pady=5)
        button3.pack(fill="x", padx=10, pady=5)
        button4.pack(fill="x", padx=10, pady=5)
        button5.pack(fill="x", padx=10, pady=5)

        
            
        #**************Table frame*******************
        table_frame = Frame(root, bd = 2, bg= "white" ,relief=RIDGE)
        table_frame.place(x= 30, y= 400, width=1200,height= 300)
        
        #scroll bar in table frame
        scroll_x= ttk.Scrollbar(table_frame, orient= HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame, orient= VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame, column= ("Department", "Batch", "Semester", "Section","Student ID", "Student Name","Roll No.", "Gender", "E-mail", "Phone No.", "Address", "D.O.B", "Photo"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill= X)
        scroll_y.pack(side=RIGHT, fill= Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)



        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Batch", text="Batch")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("Section", text="Section")
        self.student_table.heading("Student ID", text="Student ID")
        self.student_table.heading("Student Name", text="Student Name")
        self.student_table.heading("Roll No.", text="Roll No.")         
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("E-mail", text="E-mail")
        self.student_table.heading("Phone No.", text="Phone No.")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("D.O.B", text="D.O.B")
        self.student_table.heading("Photo", text="PhotoSampleStatus")        
        self.student_table["show"] = "headings"
        
        
        self.student_table.column("Department", width = 100)
        self.student_table.column("Batch", width = 100)
        self.student_table.column("Semester",width = 100)
        self.student_table.column("Section", width = 100)
        self.student_table.column("Student ID", width = 100)
        self.student_table.column("Student Name", width = 100)
        self.student_table.column("Roll No.", width = 100)        
        self.student_table.column("Gender", width = 100)
        self.student_table.column("E-mail", width = 100)
        self.student_table.column("Phone No.", width = 100)
        self.student_table.column("Address", width = 100)
        self.student_table.column("D.O.B", width = 100)
        self.student_table.column("Photo", width = 50)

        self.student_table.pack(fill= BOTH, expand= 1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
        
    #function declaration
    
    def add_data(self):
          if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
              messagebox.showerror("Error","All Fields are required",parent=self.root)
          else:
              try:
                conn= mysql.connector.connect(host="localhost", username="root", password="Mysql@ybh1", database="face_recognizer")
                my_cursor= conn.cursor()
                my_cursor.execute("Insert into student values(%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.var_dep.get(),
                                                                                            self.var_batch.get(),
                                                                                            self.var_semester.get(),
                                                                                            self.var_section.get(),
                                                                                            self.var_std_id.get(),
                                                                                            self.var_std_name.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_email.get(),                                                                                           
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_radio1.get()
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                      ))
              
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully", parent=self.root)
              except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}", parent= self.root)   

    
   # ***********data fetch to table*****        
    def fetch_data(self):
      conn=mysql.connector.connect(host="localhost" ,username="root", password="Mysql@ybh1", database="face_recognizer")     
      my_cursor=conn.cursor()
      my_cursor.execute("select * from student")
      data=my_cursor.fetchall()
      
      if len(data)!=0:
        self.student_table.delete(*self.student_table.get_children())
        for i in data:
          self.student_table.insert("", END, values=i)
        conn.commit()  
      conn.close()  
    #***********get cursor*********
    def get_cursor(self, event=""):
      cursor_focus=self.student_table.focus()
      content=self.student_table.item(cursor_focus)
      data= content["values"]
      
      print("Data: ", data)
      
      if data:
        self.var_dep.set(data[0])
        self.var_batch.set(data[1])
        self.var_semester.set(data[2])
        self.var_section.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_roll.set(data[6])
        self.var_gender.set(data[7])
        self.var_email.set(data[8])
        self.var_phone.set(data[9])
        self.var_address.set(data[10])
        self.var_dob.set(data[11])
        self.var_radio1.set(data[12])
      else:
          messagebox.showerror("Error", "Selected row is empty or invalid", parent=self.root)
    #********update function button*******
    def update_data(self):
      if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
        messagebox.showerror("Error","All Fields are required",parent=self.root)
      else:
          try:
           Update= messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
           if Update>0:
             conn=mysql.connector.connect(host="localhost" ,username="root", password="Mysql@ybh1", database="face_recognizer")     
             my_cursor =conn.cursor()
             my_cursor.execute("update student set Dep=%s, Batch=%s, Semester=%s, Section=%s, `Student Name`=%s, `Roll No.`=%s, Gender=%s, `E-mail`=%s, `Phone No.`=%s, Address=%s, `D.O.B`=%s,PhotoSample=%s where `Student ID`=%s",(
               
                                                                                                                                                                                      self.var_dep.get(),
                                                                                                                                                                                      self.var_batch.get(),
                                                                                                                                                                                      self.var_semester.get(),
                                                                                                                                                                                      self.var_section.get(),                                                                                                                                                                                      
                                                                                                                                                                                      self.var_std_name.get(),
                                                                                                                                                                                      self.var_roll.get(),                                                                                                                                                                                      
                                                                                                                                                                                      self.var_gender.get(),
                                                                                                                                                                                      self.var_email.get(),
                                                                                                                                                                                      self.var_phone.get(),
                                                                                                                                                                                      self.var_address.get(),
                                                                                                                                                                                      self.var_dob.get(),
                                                                                                                                                                                      self.var_radio1.get(),
                                                                                                                                                                                      self.var_std_id.get(),                             
                                                                                                                                                                                    ))
           else:
            if not Update:
             return
           messagebox.showinfo("Success","Student details successfully updated",parent=self.root) 
           conn.commit()
           self.fetch_data()
           conn.close() 
          except Exception as es:
            messagebox.showerror("Error",f"Due To: {str(es)}", parent=self.root) 
    #*** delete function****
    def delete_data(self):
      if self.var_std_id.get()=="":
        messagebox.showerror("Error", "Student id is required",parent=self.root)
      else:
        try:
           delete= messagebox.askyesno("Student Delete Page", "Do you want to delete this student data?",parent=self.root)  
           if delete>0:
             conn=mysql.connector.connect(host="localhost" ,username="root", password="Mysql@ybh1", database="face_recognizer")     
             my_cursor=conn.cursor()
             sql="Delete from student where `Student ID`=%s"
             val=(self.var_std_id.get(),)
             my_cursor.execute(sql,val)
           else:
             if not delete:
               return
           conn.commit() 
           self.fetch_data()
           conn.close()
           messagebox.showinfo("Delete", "Successfully deleted student details") 
        except Exception as es:
            messagebox.showerror("Error",f"Due To: {str(es)}", parent=self.root)
            
    #**********reset function********
    def reset_data(self):
      self.var_dep.set("Select Department")
      self.var_batch.set("Select Batch")
      self.var_semester.set("Select Semester")
      self.var_section.set("Select Section")
      self.var_std_id.set("")
      self.var_std_name.set("")
      self.var_roll.set("")
      self.var_gender.set("Select Gender")
      self.var_email.set("")
      self.var_phone.set("")
      self.var_address.set("")
      self.var_dob.set("")
      self.var_radio1.set("")
        
        
        #Generate data set or Take Photo Samples
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
          messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
         try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Mysql@ybh1", database="face_recognizer")
            my_cursor = conn.cursor()
            
            my_cursor.execute("SELECT * FROM student")
            myResult = my_cursor.fetchall()
            student_id = 0
            for row in myResult:
                student_id += 1
            
            my_cursor.execute("UPDATE student SET Dep=%s, Batch=%s, Semester=%s, Section=%s, `Student Name`=%s, `Roll No.`=%s, Gender=%s, `E-mail`=%s, `Phone No.`=%s, Address=%s, `D.O.B`=%s, PhotoSample=%s WHERE `Student ID`=%s", (
                self.var_dep.get(),
                self.var_batch.get(),
                self.var_semester.get(),
                self.var_section.get(),
                self.var_std_name.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_dob.get(),
                self.var_radio1.get(),
                student_id + 1  # Use the new student ID
            ))
            conn.commit()
            
            # Load OpenCV
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            
            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                
                for (x, y, w, h) in faces:
                    face_cropped = img[y:y + h, x:x + w]
                    return face_cropped
                
            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, my_frame = cap.read()
                if face_cropped(my_frame) is not None:
                    img_id += 1
                    face = cv2.resize(face_cropped(my_frame), (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = "data/user." + str(self.var_std_id.get()) + "." + str(img_id) + ".jpg"

                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face)
                    
                if cv2.waitKey(1) == 13 or int(img_id) == 100:
                    break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Generating data sets completed !!!")
         except Exception as es:
            messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)    

















if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()