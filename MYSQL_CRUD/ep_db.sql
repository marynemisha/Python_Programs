create database ep;
use ep;
CREATE TABLE department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(30)
);

CREATE TABLE employee (
    eid INT PRIMARY KEY,
    name VARCHAR(30),
    dept_id INT,
    salary INT,
    experience INT
);

INSERT INTO department VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Sales');

INSERT INTO employee VALUES
(1, 'Anu', 1, 25000, 2),
(2, 'Riya', 2, 40000, 4),
(3, 'Ammu', 1, 30000, 3),
(4, 'Arun', 2, 45000, 5),
(5, 'Meera', 3, 20000, 1);

SELECT * FROM employee;

SELECT * FROM employee WHERE salary > 30000;

SELECT * FROM employee ORDER BY salary DESC;

UPDATE employee SET salary = 28000 WHERE eid = 1;

DELETE FROM employee WHERE eid = 5;

SELECT COUNT(*), SUM(salary), AVG(salary),
       MAX(salary), MIN(salary)
FROM employee;

SELECT dept_id, COUNT(*) AS total_employees
FROM employee
GROUP BY dept_id;

SELECT dept_id, AVG(salary) AS average_salary
FROM employee
GROUP BY dept_id
HAVING AVG(salary) > 30000;

-- INNER JOIN
SELECT employee.name, department.dept_name, employee.salary
FROM employee
INNER JOIN department
ON employee.dept_id = department.dept_id;

-- LEFT JOIN
SELECT employee.name, department.dept_name
FROM employee
LEFT JOIN department
ON employee.dept_id = department.dept_id;

-- RIGHT JOIN
SELECT employee.name, department.dept_name
FROM employee
RIGHT JOIN department
ON employee.dept_id = department.dept_id;

-- JOIN + WHERE
SELECT employee.name, department.dept_name, employee.salary
FROM employee
INNER JOIN department
ON employee.dept_id = department.dept_id
WHERE employee.salary > 30000;

-- JOIN + GROUP BY + HAVING
SELECT department.dept_name, AVG(employee.salary) AS average_salary
FROM employee
INNER JOIN department
ON employee.dept_id = department.dept_id
GROUP BY department.dept_name
HAVING AVG(employee.salary) > 30000;

-- JOIN + ORDER BY
SELECT employee.name, department.dept_name, employee.salary
FROM employee
INNER JOIN department
ON employee.dept_id = department.dept_id
ORDER BY employee.salary DESC;
