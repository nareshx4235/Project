from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition1 import Face_Recognition
from attendance import AttendanceApp

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("desktop.ico")
        
        
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
        os.startfile("data")   
    
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
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
