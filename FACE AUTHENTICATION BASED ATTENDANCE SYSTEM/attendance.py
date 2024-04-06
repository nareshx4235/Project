from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime
import csv

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Management System")
        self.root.geometry("600x400")
        self.root.wm_iconbitmap("desktop.ico")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.id_label = Label(self.root, text="Enter Student ID:")
        self.id_label.pack(pady=10)

        self.id_entry = Entry(self.root)
        self.id_entry.pack(pady=5)

        self.name_label = Label(self.root, text="Enter Student Name:")
        self.name_label.pack(pady=10)

        self.name_entry = Entry(self.root)
        self.name_entry.pack(pady=5)

        self.month_label = Label(self.root, text="Select Month:")
        self.month_label.pack(pady=10)

        self.month_combobox = ttk.Combobox(self.root, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
        self.month_combobox.pack(pady=5)

        self.show_report_button = Button(self.root, text="Show Report", command=self.show_report)
        self.show_report_button.pack(pady=10)

        self.fetch_all_button = Button(self.root, text="Fetch All Records", command=self.fetch_all_records)
        self.fetch_all_button.pack(pady=10)

        self.conn = mysql.connector.connect(host="localhost", username="root", password="Mysql@ybh1", database="face_recognizer")
        self.cursor = self.conn.cursor()

    def show_report(self):
        student_id = self.id_entry.get()
        student_name = self.name_entry.get()
        month = self.month_combobox.get()
        if not student_id or not student_name or not month:
            messagebox.showerror("Error", "Please enter Student ID, Student Name, and select a month.")
            return

        try:
            query = f"SELECT * FROM attendance WHERE `Student ID` = '{student_id}' AND `Student Name` = '{student_name}' AND MONTH(Date) = '{datetime.strptime(month, '%B').month}'"
            self.cursor.execute(query)
            records = self.cursor.fetchall()

            present_days = len(records)
            total_checkin_time = sum([record[5].seconds // 3600 for record in records])  # Convert timedelta to hours
            total_checkout_time = sum([record[6].seconds // 3600 for record in records])  # Convert timedelta to hours

            avg_checkin_time = total_checkin_time / present_days if present_days > 0 else 0
            avg_checkout_time = total_checkout_time / present_days if present_days > 0 else 0

            report_window = Toplevel(self.root)
            report_window.title("Attendance Report")
            report_text = f"Student ID: {student_id}\nStudent Name: {student_name}\nMonth: {month}\nTotal Present Days: {present_days}\nAverage Check-in Time: {avg_checkin_time}\nAverage Checkout Time: {avg_checkout_time}"
            report_label = Label(report_window, text=report_text)
            report_label.pack(padx=20, pady=20)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def fetch_all_records(self):
        try:
            self.cursor.execute("SELECT * FROM attendance")
            records = self.cursor.fetchall()
            with open("attendance_report/attendance_data.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Dep", "Student Name", "Student ID", "Roll No.", "Date", "Checkin Time", "Checkout Time", "Status"])
                writer.writerows(records)
            messagebox.showinfo("Success", "Attendance data exported to attendance_data.csv")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def __del__(self):
        self.conn.close()


if __name__ == "__main__":
    root = Tk()
    app = AttendanceApp(root)
    root.mainloop()
