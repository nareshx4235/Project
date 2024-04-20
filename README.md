Face Authenatication Based Attendance System
It will be a two step mechanism. First, prior to face recognition we have to do face detection. Once, face detection has been performed successfully then only face recognition will be performed by using Principal Component Analysis (PCA).

How to run the system
In order to run the system, you'll require to install Python.

windows : VS  code 

After completing above step, you'll need to download MYSQL  to setup the database required for the system to mark and store the attendance.



Compiling and Running the Project
After completing all the above mentioned steps, Open VS code and setup the connection port of MYSQL 

Run Face Authentication Based Attendance System.py

The flow of interactions within the facial authenticationbased attendance system, detailing how students check in and check out and how teachers
log in and register.

For Admin (Teacher):
i. UI_System initializes and displays the user interface.
ii. Admin clicks on the "Login" button.
iii. UI_System sends a request to Login for authentication.
iv. Login verifies credentials and grants access.
v. If not registered, admin clicks on "Register" button.
vi. UI_System sends a request to Register for registration.
vii. Register collects admin's information and registers them.
viii. Once logged in, admin interacts with Face_Recognition_System to manage
attendance.

For Student:
i. UI_System initializes and displays the user interface.
ii. Student clicks on "Take Attendance" button.
iii. UI_System sends a request to Face_Recognition_System to start facial recognition.
iv. Face_Recognition_System captures student's face and checks against registered
faces.
v. If recognized, Face_Recognition_System marks student as checked-in/checkedout.
vi. Face_Recognition_System updates attendance record in database.
vii. System notifies student about check-in/check-out status.
