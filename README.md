
# Face Recognition Attendance System

This project is a Face Recognition-based Attendance System that uses OpenCV, Tkinter, and an SQL database to manage student records and attendance. The system provides functionalities for adding, updating, deleting student details, training the face recognition model, and marking attendance through face recognition.

## Features
- **Student Details Management**: Add, update, or delete student details which are saved directly to the SQL database.
- **Face Training**: Capture images of students and train the face recognition model.
- **Attendance Marking**: Once the student's face is recognized, their attendance is marked and stored in a CSV file.
- **GUI**: Developed using Tkinter for a user-friendly interface.
  
## Technologies Used
- **Python 3.11** (Latest stable version of Python)
- **OpenCV** (for face detection and recognition)
- **Tkinter** (for creating the GUI)
- **SQL Database** (to store student details)
- **CSV** (to store attendance)

## Prerequisites
Before running the application, ensure that you have the following installed:
- Python 3.11 (latest stable version of Python)
- SQL database (for example, MySQL or SQLite)

### 1. Clone the repository:
```bash
git clone https://github.com/your-repo/face-recognition-attendance-system.git
cd face-recognition-attendance-system
```

### 2. Install the required Python libraries:
Use the `requirements.txt` file to install all the necessary dependencies. You can install them using pip:

```bash
pip install -r requirements.txt
```

Alternatively, you can manually install the following libraries:
- `opencv-python` for OpenCV
- `opencv-contrib-python` for additional OpenCV features (like `LBPH` face recognition)
- `tkinter` for the GUI
- `mysql-connector` or `sqlite3` for the SQL database connection

### 3. Database Setup:
- Set up a local SQL database (e.g., MySQL or SQLite).
- Create a database to store student details.
- Update the database connection settings in the `database.py` file with your database credentials.

Example of database setup for MySQL:
```sql
CREATE DATABASE attendance_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    roll_no VARCHAR(50),
    photo_path VARCHAR(255)
);
```

### 4. Running the Application:
1. **Start the app**: 
   Open the terminal and run the `main.py` file to launch the Tkinter-based GUI.
   ```bash
   python main.py
   ```

2. **Add Student Details**: 
   Use the "Student Details" page in the app to add, update, or delete student information. 
   
3. **Take Photos**: 
   Use the "Capture Photos" page to take pictures of students. These photos will be used to train the face recognition model.

4. **Train the Model**: 
   After capturing student images, use the "Train" button to train the face recognition model with the captured images.

5. **Mark Attendance**: 
   Use the "Recognize" page to recognize students based on the trained model. The attendance will be recorded in a CSV file (`attendance.csv`).

## File Structure
```
/face-recognition-attendance-system
│
├── Photos             # All the photos to be used
├── main.py                  # Main application logic (Tkinter GUI)
├── train.py                 # Script for training the face recognition model
├── recognize.py             # Script for recognizing faces and marking attendance
├── attendance.csv           # CSV file to store attendance records
├── student_data.db          # SQL database for student details
└── requirements.txt         # List of dependencies to install
```

## Usage
- **Student Details Management**: Allows users to add, update, or delete student details from the system.
- **Face Training**: Allows users to take images of students and train the recognition model.
- **Attendance**: After the student is recognized, their attendance is marked in `attendance.csv`.

### Example Attendance CSV:
```csv
Name, Roll No, Date, Time
John Doe, 1234, 2024-12-08, 09:00
Jane Smith, 5678, 2024-12-08, 09:05
```

## Troubleshooting
- **Error: "No module named Tkinter"**: Ensure that Tkinter is installed. If using Python 3.x, Tkinter should be installed by default.
- **Error: "Could not connect to database"**: Verify that your database credentials are correct and that the database is running.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments
- OpenCV for face detection and recognition.
- Tkinter for building the GUI.
- SQL for storing student details.
```

