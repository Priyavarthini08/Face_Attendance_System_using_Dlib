from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3
import subprocess
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'data/Captured_faces_data/'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student')
def student():
    subprocess.run(['python', 'Capturing_faces.py'])
    subprocess.run(['python', 'Extracting_features_to_csv.py'])
    return redirect(url_for('index'))

@app.route('/teacher')
def teacher():
    return render_template('teacher.html')

@app.route('/take_attendance')
def take_attendance():
    subprocess.run(['python', 'Taking_attendance.py'])
    return redirect(url_for('attendance'))

@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    if request.method == 'POST':
        selected_date = request.form.get('selected_date')
        selected_date_obj = datetime.strptime(selected_date, '%Y-%m-%d')
        formatted_date = selected_date_obj.strftime('%Y-%m-%d')

        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name, time FROM attendance WHERE date = ?", (formatted_date,))
        attendance_data = cursor.fetchall()
        conn.close()

        if not attendance_data:
            return render_template('attendance.html', selected_date=selected_date, no_data=True)
        
        return render_template('attendance.html', selected_date=selected_date, attendance_data=attendance_data)
    
    return render_template('attendance.html')

if __name__ == '__main__':
    app.run(debug=True)