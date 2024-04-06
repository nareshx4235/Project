import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Python311\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Python311\tcl\tk8.6"

executables = [cx_Freeze.Executable("Face Authentication Based Attendance System.py", base=base, icon="desktop.ico")]


cx_Freeze.setup(
    name = "Face Authentication Based Attendance System",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["desktop.ico",'tcl86t.dll','tk86t.dll', 'college_images','data','database','attendance_report']}},
    version = "2.1",
    description = "Face Authentication Based Attendance System | Developed By Naresh Adhikari",
    executables = executables
    )