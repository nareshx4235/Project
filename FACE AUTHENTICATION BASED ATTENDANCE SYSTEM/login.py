from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

import mysql.connector
# --------------------------
from train import Train
from student import Student
from train import Train
from face_recognition1 import Face_Recognition
from attendance import AttendanceApp
from register import Register

import os


class Login:
    def __init__(self,root):
        self.root=root
        self.root.resizable(0, 0)
        self.root.title("Login")
        #self.root.state('zoomed')
        self.root.geometry("1320x768")
        self.root.wm_iconbitmap("desktop.ico")

        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()
        self.show_pwd = BooleanVar()

        self.bg=ImageTk.PhotoImage(file="college_images\loginBg1.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame1= Frame(self.root,bg="#002B53")
        frame1.place(x=560,y=170,width=340,height=450)

        

        get_str = Label(frame1,text="Login",font=("times new roman",20,"bold"),fg="white",bg="#002B53")
        get_str.place(x=140,y=100)

        #label1 
        email =lb1= Label(frame1,text="Email:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        email.place(x=30,y=160)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtuser.place(x=33,y=190,width=270)


        #label2 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        pwd.place(x=30,y=230)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,show="*",font=("times new roman",15,"bold"))
        self.txtpwd.place(x=33,y=260,width=270)
        
        self.chk_show_pwd = ttk.Checkbutton(frame1, text="Show Password", variable=self.show_pwd, command=self.toggle_password)
        self.chk_show_pwd.place(x=185, y=290)


        # Creating Button Login
        loginbtn=Button(frame1,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#002B53",bg="white",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=33,y=320,width=270,height=35)


        # Creating Button Registration
        loginbtn=Button(frame1,command=self.reg,text="Register",font=("times new roman",13,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=60,y=390,width=80,height=22)


        # Creating Button Forget
        loginbtn=Button(frame1,command=self.forget_pwd,text="Forget",font=("times new roman",13,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=180,y=390,width=80,height=22)


     #  THis function is for open register window
    def reg(self):
       self.new_window=Toplevel(self.root)
       self.app=Register(self.new_window)

    def toggle_password(self):
        if self.show_pwd.get():
            self.txtpwd.config(show="")
        else:
            self.txtpwd.config(show="*")
    def login(self):
        if self.txtuser.get() == "" or self.txtpwd.get() == "":
            messagebox.showerror("Error", "All Fields Required!")
        elif self.txtuser.get() == "admin" and self.txtpwd.get() == "admin":
            messagebox.showinfo("Successfully", "Welcome to Attendance Management System Using Facial Recognition")
            self.open_main_window()
        else:
            conn = mysql.connector.connect(username="root", password="Mysql@ybh1", host="localhost",
                                        database="face_recognizer")
            mycursor = conn.cursor()
            mycursor.execute("select * from regteach where email=%s and pwd=%s", (
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row = mycursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Username and Password!")
            else:
                self.open_main_window()
            conn.commit()
            conn.close()
    def open_main_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition_System(self.new_window)        
#=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(username='root', password='Mysql@ybh1',host='localhost',database='face_recognizer',port=3306)
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s and ssq=%s and sa=%s")
            value=(self.txtuser.get(),self.var_ssq.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update regteach set pwd=%s where email=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                



# =====================Forget window=========================================
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(username='root', password='Mysql@ybh1',host='localhost',database='face_recognizer',port=3306)
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                ssq.place(x=70,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=70,y=150)

                #entry2 
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=70,y=180,width=270)

                #label2 
                new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_pwd.place(x=70,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=70,y=300,width=270,height=35)


            

# =====================main program Face dection system====================
class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("Face Recognition System")
        
        # Define gradient colors for background
        background_color1 = (74, 144, 226)  # Blue
        background_color2 = (255, 255, 255)  # White

        # Create gradient image for background
        gradient_image = self.create_gradient(1366, 768, background_color1, background_color2)
        background_label = ttk.Label(root, image=gradient_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Define button background color (same as window background)
        button_bg_color = '#5b90f5'

        buttons_text = ['Profile', 'Face Detector', 'Attendance', 'Train Data', 'Photos', 'Log Out']
        buttons_icons = ['👤', '😊', '📅', '💾', '🖼', '↩']

        button_width = 15  # Increased button width
        button_height = 7  # Increased button height
        button_padx = 20
        button_pady = 20

        # Calculate total width and height of buttons
        total_width = button_width * 3 + button_padx * 2
        total_height = button_height * 2 + button_pady * 1

        # Calculate starting position to center the buttons
        start_x = (1366 - total_width) / 2
        start_y = (768 - total_height) / 2

        functions = [self.student_details, self.face_data, self.attendance, self.train_data,
                    self.open_img, self.Close]

        for i in range(2):
            for j in range(3):
                index = i * 3 + j
                button = Button(root,
                                text=f'{buttons_icons[index]}\n{buttons_text[index]}',
                                font=('Arial', 16  ),  # Decreased font size
                                padx=105,  # Decreased horizontal padding
                                pady=60,  # Decreased vertical padding
                                width=button_width,
                                height=button_height,
                                highlightthickness=3,  # Removed border
                                bd=8,  # Removed border width
                                fg='white',  # Set foreground (text) color of buttons to white
                                bg=button_bg_color,  # Set background color of buttons
                                command=functions[index]  # Associate function with button
                                )
                button.grid(row=i, column=j, padx=button_padx, pady=button_pady)   

    def create_gradient(self, width, height, color1, color2):
        gradient = Image.new('RGB', (width, height))
        for y in range(height):
            r = int(color1[0] + (color2[0] - color1[0]) * y / height)
            g = int(color1[1] + (color2[1] - color1[1]) * y / height)
            b = int(color1[2] + (color2[2] - color1[2]) * y / height)
            for x in range(width):
                gradient.putpixel((x, y), (r, g, b))
        return ImageTk.PhotoImage(gradient)

    def open_new_window(self):
        new_window = Toplevel(self.root)
        new_window.title("New Window")
        new_window.geometry("1366x768")
        label = ttk.Label(new_window, text="New Window Content")
        label.pack()

    def open_img(self):
        os.startfile("photos")   
    
    def student_details(self):
        new_window = Toplevel(self.root)
        app = Student(new_window)
        
    def train_data(self):
        new_window = Toplevel(self.root)
        app = Train(new_window) 
        
    def face_data(self):
        new_window = Toplevel(self.root)
        app = Face_Recognition(new_window)
        
    def attendance(self):
        new_window = Toplevel(self.root)
        app = AttendanceApp(new_window)

    def Close(self):
        self.root.destroy()
        
      
        
        
        
        
        
        
        
        
            
if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()
