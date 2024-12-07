-- Create the database
CREATE DATABASE IF NOT EXISTS face_recognizer;

-- Use the database
USE face_recognizer;

-- Create the Students table
CREATE TABLE Students (
    Dep VARCHAR(45) NOT NULL,
    course VARCHAR(45) NOT NULL,
    Year VARCHAR(45) NOT NULL,
    Semester VARCHAR(45) NOT NULL,
    Student_id INT NOT NULL,
    Name VARCHAR(45) NOT NULL,
    Division VARCHAR(45) NOT NULL,
    Roll VARCHAR(45) NOT NULL,
    Gender VARCHAR(45) NOT NULL,
    Dob VARCHAR(45) NOT NULL,
    Email VARCHAR(45) NOT NULL,
    Phone VARCHAR(45) NOT NULL,
    Address VARCHAR(45) NOT NULL,
    Teacher VARCHAR(45) NOT NULL,
    PhotoSample VARCHAR(45) NOT NULL,
    PRIMARY KEY (Student_id)
);
-- Use the database 'face_recognizer'
USE face_recognizer;

-- Select all records from the 'Students' table
SELECT * FROM Students;
