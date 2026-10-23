create database school;
use school;
CREATE TABLE class (
    class_id INT PRIMARY KEY,
    class_name VARCHAR(20)
);

CREATE TABLE school (
    student_id INT PRIMARY KEY,
    name VARCHAR(30),
    class_id INT,
    mark INT,
    fees INT
);

INSERT INTO class VALUES
(1, 'Class 9'),
(2, 'Class 10'),
(3, 'Class 11');

INSERT INTO school VALUES
(1, 'Anu', 2, 85, 10000),
(2, 'Ammu', 2, 70, 10000),
(3, 'Riya', 1, 90, 9000),
(4, 'Meera', 2, 60, 10000),
(5, 'Arun', 1, 75, 9000);

SELECT * FROM school;

SELECT * FROM school WHERE mark >= 80;

SELECT * FROM school ORDER BY mark DESC;

UPDATE school SET mark = 88 WHERE student_id = 1;

DELETE FROM school WHERE student_id = 5;

SELECT COUNT(*), SUM(fees), AVG(mark),
       MAX(mark), MIN(mark)
FROM school;

SELECT class_id, COUNT(*) AS total_students
FROM school
GROUP BY class_id;

SELECT class_id, AVG(mark) AS average_mark
FROM school
GROUP BY class_id
HAVING AVG(mark) > 75;

-- INNER JOIN
SELECT school.name, class.class_name, school.mark
FROM school
INNER JOIN class
ON school.class_id = class.class_id;

-- LEFT JOIN
SELECT school.name, class.class_name
FROM school
LEFT JOIN class
ON school.class_id = class.class_id;

-- RIGHT JOIN
SELECT school.name, class.class_name
FROM school
RIGHT JOIN class
ON school.class_id = class.class_id;

-- JOIN + WHERE
SELECT school.name, class.class_name, school.mark
FROM school
INNER JOIN class
ON school.class_id = class.class_id
WHERE school.mark > 80;

-- JOIN + GROUP BY + HAVING
SELECT class.class_name, AVG(school.mark) AS average_mark
FROM school
INNER JOIN class
ON school.class_id = class.class_id
GROUP BY class.class_name
HAVING AVG(school.mark) > 75;

-- JOIN + ORDER BY
SELECT school.name, class.class_name, school.mark
FROM school
INNER JOIN class
ON school.class_id = class.class_id
ORDER BY school.mark DESC;