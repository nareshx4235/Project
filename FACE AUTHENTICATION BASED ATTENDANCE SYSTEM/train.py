from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import numpy as np
import cv2

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("desktop.ico")
        
        # Set background color
        root.configure(bg="#4c618d")
     
        # Create a custom style for the button
        style = ttk.Style()
        style.configure("my.TButton", font=("rockwell", 25, "bold"), foreground="black", background="#F2F2F2", padding=10)

        update_btn1 = ttk.Button(self.root, text="Train your Data Here", command=self.train_classifier, style="my.TButton")
        update_btn1.place(x=500, y=345, width=400, height=90)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]   
        
        faces = []
        ids = []
        
        for image in path:
            img = Image.open(image).convert("L")  # Grayscale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            
        ids = np.array(ids)
        
        # Train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("Classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed") 
        
if __name__ == "__main__":
    root = Tk()
    obj = Train(root) 
    root.mainloop()
