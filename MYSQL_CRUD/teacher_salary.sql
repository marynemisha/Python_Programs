show databases;
use june_b1;
show tables;
drop table teacher;
show tables;
create table teacher(T_Id int primary key,Teacher_Name varchar(100) not null,Department varchar(100),
Mobile_Number Bigint unique,Email_id varchar(100),Place varchar(100));
create table salary(Salary_id int primary key,Teacher_Id int,Salary Bigint,Permanent varchar(100) not null);
INSERT INTO teacher (T_Id,Teacher_Name,Department,Mobile_Number,Email_id,Place)VALUES
(1,"Anitha","Computer Science",9876543210,"anitha@gmail.com","Kochi"),
(2,"Suresh","Python",9876543211,"suresh@gmail.com","Aluva"),
(3,"Meena","Data science",9876543212,"meena@yahoo.com","Thrissur"),
(4,"Rajesh","Mern",9876543213,"rajesh@gmail.com","Kottayam"),
(5,"Priya","English",9876543214,"priya@edu.com","Kochi"),
(6,"Arun","Computer Science",9876543215,"arun@gmail.com","Idukki"),
(7,"Divya","Data science",9876543216,"divya@gmail.com","Kollam"),
(8,"Vishnu","Mern",9876543217,"vishnu@yahoo.com","Alappuzha"),
(9,"Sneha","Mathematics",9876543218,"sneha@gmail.com","Palakkad"),
(10,"Manu","python",9876543219,"manu@gmail.com","Kannur");
INSERT INTO salary (Salary_id,Teacher_Id,Salary,Permanent)VALUES
(101,1,35000,"Permanent"),
(102,2,40000,"Temporary"),
(103,3,38000,"Permanent"),
(104,4,45000,"Permanent"),
(105,5,36000,"Temporary"),
(106,6,42000,"Permanent"),
(107,7,39000,"Temporary"),
(108,8,41000,"Permanent"),
(109,9,37000,"Temporary"),
(110,10,44000,"Permanent");
SELECT * FROM teacher WHERE Email_id LIKE '%gmail%';
SELECT * FROM teacher WHERE Department IN ('Python','MERN');
SELECT Teacher_Name FROM teacher WHERE Teacher_Name LIKE 'A%';
SELECT COUNT(*) as Number_of_teachers FROM salary WHERE Salary > 30000;
SELECT Teacher_Name FROM teacher ORDER BY Teacher_Name DESC;
SELECT Teacher_Name, Mobile_Number FROM teacher WHERE Place = 'Kochi';
SELECT Teacher_Name, Department FROM teacher WHERE Email_id LIKE '%gmail.com';
SELECT * FROM teacher WHERE Place IN ('Kochi','Ernakulam');
SELECT teacher.teacher_name,teacher.department,salary.salary from teacher INNER JOIN salary  ON teacher.T_Id = salary.Teacher_Id WHERE salary.Salary BETWEEN 20000 AND 50000;
SELECT t.Teacher_Name FROM teacher t INNER JOIN salary s ON t.T_Id = s.Teacher_Id WHERE s.Permanent = 'Permanent';
SELECT t.Teacher_Name, s.Salary FROM teacher t INNER JOIN salary s ON t.T_Id = s.Teacher_Id WHERE s.Salary = (
    SELECT MAX(s2.Salary) FROM salary s2 INNER JOIN teacher t2 ON t2.T_Id = s2.Teacher_Id WHERE t2.Department = t.Department);
SELECT t.Department, MAX(s.Salary) AS Highest_Salary
FROM teacher t
INNER JOIN salary s
ON t.T_Id = s.Teacher_Id
GROUP BY t.Department;
SELECT t.Teacher_Name, t.Department, s.Salary
FROM teacher t
INNER JOIN salary s
ON t.T_Id = s.Teacher_Id
WHERE s.Salary IN (
    SELECT MAX(s.Salary)
    FROM teacher t
    INNER JOIN salary s
    ON t.T_Id = s.Teacher_Id
    GROUP BY t.Department
);
SELECT COUNT(*) FROM teacher WHERE Department = 'Python';
SELECT AVG(Salary) as average_salary FROM salary;
SELECT t.Teacher_Name, t.Department, s.Salary
FROM teacher t
INNER JOIN salary s
ON t.T_Id = s.Teacher_Id
WHERE (teacher.department,max(salary.salary) IN (select teacher.Department,max(salary.salary)FROM teacher inner join salary on teacher.T_Id=salary.Teacher_Id group by teacher.Department));
SELECT Teacher_Name, Email_id
FROM teacher
WHERE Department LIKE 'P%';
select * from teacher order by Department asc, Teacher_Name asc;
SELECT t.Teacher_Name FROM teacher t INNER JOIN salary s ON t.T_Id = s.Teacher_Id WHERE s.Permanent = 'Temporary';
SELECT Place, COUNT(*) AS Teacher_Count
FROM teacher
GROUP BY Place
ORDER BY Teacher_Count DESC
LIMIT 1;
SELECT Salary
    FROM salary
    GROUP BY Salary
    HAVING COUNT(*) > 1;
SELECT t.*, s.Salary
FROM teacher t
INNER JOIN salary s
ON t.T_Id = s.Teacher_Id
WHERE s.Salary IN (
    SELECT Salary
    FROM salary
    GROUP BY Salary
    HAVING COUNT(salary) > 1
);
SELECT Salary, COUNT(*)
FROM salary
GROUP BY Salary;
  SELECT t.Teacher_Name, s.salary 
FROM teacher t 
JOIN salary s ON t.T_ID = s.Teacher_ID 
WHERE s.salary IN ( 
SELECT salary 
FROM salary 
GROUP BY salary 
HAVING COUNT(salary) > 1 
);
  SELECT T.Teacher_Name, T.Department, S.Salary 
FROM Teacher T 
INNER JOIN Salary S ON T.T_ID = S.Teacher_ID 
WHERE S.Salary > (SELECT AVG(Salary) FROM Salary);