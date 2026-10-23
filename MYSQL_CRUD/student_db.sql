create database st;
use st;
CREATE TABLE student (
    sid INT PRIMARY KEY,
    name VARCHAR(30),
    department_id INT,
    mark INT,
    city VARCHAR(30)
);

CREATE TABLE department (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(30)
);

INSERT INTO department VALUES
(1, 'BCA'),
(2, 'BBA'),
(3, 'BCom');

INSERT INTO student VALUES
(1, 'Anu', 1, 85, 'Kochi'),
(2, 'Ammu', 1, 70, 'Aluva'),
(3, 'Riya', 2, 90, 'Kochi'),
(4, 'Meera', 1, 60, 'Aluva'),
(5, 'Arun', 2, 75, 'Kochi');

-- SELECT
SELECT * FROM student;

-- WHERE
SELECT * FROM student WHERE mark > 80;

-- ORDER BY
SELECT * FROM student ORDER BY mark DESC;

-- UPDATE
UPDATE student SET mark = 88 WHERE sid = 1;

-- DELETE
DELETE FROM student WHERE sid = 5;

-- Aggregate functions
SELECT COUNT(*) FROM student;
SELECT SUM(mark), AVG(mark), MAX(mark), MIN(mark)
FROM student;

-- GROUP BY
SELECT department_id, COUNT(*) AS total
FROM student
GROUP BY department_id;

-- HAVING
SELECT department_id, AVG(mark) AS average_mark
FROM student
GROUP BY department_id
HAVING AVG(mark) > 75;

-- INNER JOIN
SELECT student.name, department.department_name
FROM student
INNER JOIN department
ON student.department_id = department.department_id;

-- LEFT JOIN
SELECT student.name, department.department_name
FROM student
LEFT JOIN department
ON student.department_id = department.department_id;

-- RIGHT JOIN
SELECT student.name, department.department_name
FROM student
RIGHT JOIN department
ON student.department_id = department.department_id;

-- JOIN + WHERE
SELECT student.name, department.department_name, student.mark
FROM student
INNER JOIN department
ON student.department_id = department.department_id
WHERE student.mark > 80;

-- JOIN + GROUP BY + HAVING
SELECT department.department_name, AVG(student.mark) AS average_mark
FROM student
INNER JOIN department
ON student.department_id = department.department_id
GROUP BY department.department_name
HAVING AVG(student.mark) > 75;

-- JOIN + ORDER BY
SELECT student.name, department.department_name, student.mark
FROM student
INNER JOIN department
ON student.department_id = department.department_id
ORDER BY student.mark DESC;