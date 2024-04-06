from tkinter import *
from login import Login
from face_recognition1 import Face_Recognition

class UI_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("UI SYSTEM")
        self.root.wm_iconbitmap("desktop.ico")

        # Create gradient background
        self.create_gradient_background()

        # Define button background color
        button_bg_color = 'black'

        # Take Attendance Button
        b1 = Button(root, text="Take Attendance", command=self.take_attendance, font=("Arial", 16), padx=20, pady=10, width=30, height=3, highlightthickness=1, bd=2, fg='white', bg=button_bg_color, relief=GROOVE, borderwidth=0, cursor="hand2")
        b1.place(relx=0.35, rely=0.4, anchor=CENTER)

# Login Button with a horizontal gap of 20 pixels
        b2 = Button(root, text="Login", command=self.login, font=("Arial", 16), padx=20, pady=10, width=30, height=3, highlightthickness=1, bd=2, fg='white', bg=button_bg_color, relief=GROOVE, borderwidth=0, cursor="hand2")
        b2.place(relx=0.7, rely=0.4, anchor=CENTER)

    def create_gradient_background(self):
        canvas = Canvas(self.root, width=1366, height=768)
        canvas.pack()

        # Draw gradient rectangle for background
        for y in range(768):
            # Interpolate between two RGB colors based on y-coordinate
            shade = int((y / 768) * 255)
            color = '#%02x%02x%02x' % (0, 191, 255 - shade)
            canvas.create_line(0, y, 1366, y, fill=color)

    def take_attendance(self):
        self.new_window=Toplevel(root)
        self.app=Face_Recognition(self.new_window)
        

    def login(self):
        self.new_window= Toplevel(root)
        self.app=Login(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = UI_System(root)
    root.mainloop()
