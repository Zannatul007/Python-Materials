CREATE DATABASE IF NOT EXISTS college;
CREATE TABLE IF NOT EXISTS student (
id INT PRIMARY KEY,
name VARCHAR(50),
age INT,
grade VARCHAR(50),
marks FLOAT,
city VARCHAR(50)
);
SELECT * FROM student;

CREATE TABLE IF NOT EXISTS department (id INT PRIMARY KEY, dept_name VARCHAR(50));
CREATE TABLE IF NOT EXISTS teacher(
id INT PRIMARY KEY, 
name VARCHAR(50),
dept_id INT, 
FOREIGN KEY (dept_id) REFERENCES department(id)
ON UPDATE CASCADE
ON DELETE CASCADE
);
-- DROP TABLE customer;
-- DROP TABLE employee;
-- DROP TABLE student;

INSERT INTO student
(id,name,age,marks,grade,city)
VALUES
(1, 'Ariana Singh', 20, 88.5, 'A', 'Delhi'),
(2, 'John Carter', 22, 75.0, 'B', 'Seoul'),
(3, 'Fatima Noor', 19, 92.3, 'A+', 'Delhi'),
(4, 'Chen Wang', 21, 68.0, 'C', 'Delhi'),
(5, 'Mohammed Alim', 23, 81.7, 'B+', 'Cairo'),
(6, 'Sara Kim', 20, 95.0, 'A+', 'Seoul');
SELECT city,AVG(marks)
FROM student
GROUP BY city
ORDER BY AVG(marks) ASC;

SELECT city,count(name)
FROM student
GROUP BY city
HAVING MAX(marks)>90;

UPDATE student
SET grade = 'A'
WHERE  marks between 80 and 90;
SELECT * FROM student;

DELETE FROM student
WHERE grade = 'C';


SELECT * FROM student;

INSERT INTO department(id,dept_name) VALUES(101,'ENGLISH'),(102,'MATH');
INSERT INTO teacher (id,name,dept_id) VALUES(1,'WASECA',101),(2,'SAIMA',102);
SELECT * FROM department;
SELECT * FROM teacher;