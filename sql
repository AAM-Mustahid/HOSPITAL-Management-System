CREATE TABLE patient (
  PatientID varchar(50) NOT NULL,
  FirstName varchar(50) NOT NULL,
  LastName varchar(50) DEFAULT NULL,
  Age int(11) NOT NULL,
  Gender varchar(45) NOT NULL,
  BloodGroup varchar(45) NOT NULL,
  Address varchar(45) DEFAULT NULL,
  Mobile int(11) NOT NULL,
  Email varchar(45) NOT NULL,
  RoomNumber int(11) DEFAULT NULL
);

CREATE TABLE doctor (
  DoctorID varchar(50) NOT NULL,
  Name varchar(45) NOT NULL,
  Age varchar(45) DEFAULT NULL
);

CREATE TABLE appointment (
  patientID varchar(50) NOT NULL,
  apptID int(11) NOT NULL,
  doctorID varchar(50) NOT NULL,
  date varchar(50) NOT NULL
);

CREATE TABLE medicalhistory (
  apptID int(11) NOT NULL,
  diagnosis varchar(45) NOT NULL,
  date varchar(50) DEFAULT NULL
);

INSERT INTO patient (PatientID, FirstName, LastName, Age, Gender, BloodGroup, Address, Mobile, Email, RoomNumber) VALUES
('P01', 'Md. Abdul Rabbi', 'Rahat', 22, 'Male', 'AB+', 'YKSG2,Ashulia,Dhaka', 019########, 'lrabbi15-4583@diu.edu.bd', NULL),
('P02', 'AAM', 'Mustahid', 22, 'Male', 'AB-', 'Changaon,Ashulia,Dhaka', 017########, 'mustahid15-4251@diu.edu.bd', 421),
('P03', 'Anamika', 'Lily', 23, 'Female', 'O-', 'Zirabo,Ashulia,Dhaka', 018########, 'anamika15-4246@diu.edu.bd', NULL),
('P04', 'Walid', 'Khan', 24, 'Male', 'A+', 'Mirpur 10,Dhaka', 015########, 'walid15-4275@diu.edu.bd', 325),
('P05', 'Shohidul', 'Islam', 23, 'Male', 'B+', 'Paltan,Dhaka', 018########, 'shohidul@gmail.com', NULL);

INSERT INTO doctor (DoctorID, Name, Age) VALUES
('D01', 'Dr. Wlater White', '55'),
('D02', 'Dr. Shaun Murphy', '27'),
('D03', 'Dr. Stephen Strange', '45');


INSERT INTO appointment (patientID, apptID, doctorID, date) VALUES
('P01', 1, 'D01', '5th November 2023'),
('P02', 11, 'D01', '11th November 2023'),
('P03', 31, 'D02', '13th November 2023'),
('P04', 2, 'D03', '14th November 2023'),
('P05', 7, 'D03', '17th November 2023');

INSERT INTO medicalhistory (apptID, diagnosis, date) VALUES
(1, 'Keratoconous', '5th November 2023'),
(11, 'Back Pain', '11th November 2023'),
(31, 'Headache', '13th November 2023'),
(2, 'Retina', '14th November 2023'),
(7, 'Regular Checkup', '17th November 2023');


SELECT * FROM 'Hospital_Management_System'.'patient' WHERE PatientID = 'A01';
SELECT * FROM 'Hospital_Management_System'.'doctor' WHERE Name = 'Dr. Shaun Murphy';
SELECT * FROM 'Hospital_Management_System'.'appointment' WHERE apptID = 11;
SELECT * FROM 'Hospital_Management_System'.'medicalhistory' WHERE diagnosis = 'Keratoconus';


UPDATE 'Hospital_Management_System'.'patient' SET Age=23 WHERE PatientID = 'A02';
UPDATE 'Hospital_Management_System'.'doctor' SET Name='Dr. Strange' WHERE Name = 'Dr. Stephen Strange';
UPDATE 'Hospital_Management_System'.'appointment' SET Date='14th November 2023'  WHERE apptID = 31;
UPDATE 'Hospital_Management_System'.'medicalhistory' SET diagnosis='Fever' WHERE diagnosis = 'Retina';




DELETE FROM 'Hospital_Management_System'.'patient' WHERE PatientID = 'A05';
DELETE FROM 'Hospital_Management_System'.'doctor' WHERE Name = 'Dr. Walter White';
DELETE FROM 'Hospital_Management_System'.'appointment' WHERE apptID = 7;
DELETE FROM 'Hospital_Management_System'.'medicalhistory' WHERE diagnosis = 'Regular Checkup';
