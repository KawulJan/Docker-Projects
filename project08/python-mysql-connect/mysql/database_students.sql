CREATE DATABASE student;
USE student;

CREATE TABLE students(
    StudentID INT not NULL AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    SurName VARCHAR(100) NOT NULL,
    PRIMARY KEY (StudentID)
);

INSERT INTO students(FirstName, SurName)
VALUES("AhmatJan", "Keyum"), ("UyghurJan", "Abuduryim");