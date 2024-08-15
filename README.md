# Face_Attendance_System_using_Dlib
# Overview

This project is a facial recognition attendance system developed using Flask, OpenCV, and Dlib. The system allows teachers to track student attendance through facial recognition. Students can register their faces, and teachers can take attendance by capturing real-time video streams. The attendance data is stored in an SQLite database.

# Features

 * Student Registration: Students can register their faces by providing their names. The system captures multiple images of the student's face and stores them in a directory.

 * Face Feature Extraction: The system uses the 'shape_predictor_68_face_landmarks.dat model' to extract facial features and store them in the backend.

 * Teacher Panel: Teachers can take attendance by capturing video streams. The system recognizes faces using the 'dlib_face_recognition_resnet_model_v1.dat model' and stores the attendance data (name and time) in the database.

 * Attendance Viewing: Teachers can view the attendance records, showing which students were present on a selected date and the time they were recognized.

# Prerequisites

dlib==19.17.0

numpy==1.22.0

scikit-image==0.18.3

pandas==1.3.4

opencv-python==4.5.4.58

flask

# Install the required dependencies:

pip install -r requirements.txt

# Download the required models:

https://drive.google.com/drive/folders/1Md1SnWRmzY3iZ1RPgsZf68Kj2Y2GBI7H?usp=drive_link

shape_predictor_68_face_landmarks.dat

dlib_face_recognition_resnet_model_v1.dat

Place the downloaded models in the project directory.

# Usage

1. Run the Flask Application:

   python app.py

2. Welcome Page: Navigate to http://127.0.0.1:5000 in your browser. You will see a welcome page with options to select "Student" or "Teacher."

3. Student Registration:

* Click on "Student."
* Enter the student's name and capture face photos.
* The system will create a directory for the student and store the captured images.

4. Teacher Panel:

* Click on "Teacher"
* You will see two options: "Take Attendance" and "View Attendance."
* Take Attendance:

     * Click on "Take Attendance."
     * The system will start capturing video streams and recognize faces.
     * Recognized faces will be stored in the database with the current time.
* View Attendance:

     * Click on "View Attendance."
     * Select a date to view the attendance records.


# Teacher Panel

<img width="895" alt="teacher_panel" src="https://github.com/user-attachments/assets/a1ee2545-91ab-49f1-aa06-b96e1fc3958e">

# Attendance Tracker Sheet

<img width="889" alt="attendance_tracker_sheet" src="https://github.com/user-attachments/assets/7fd74788-9399-4df2-abe0-e03fd00831bb">














