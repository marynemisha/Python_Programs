create database company;
use company;
create table employees(emp_id int auto_increment primary key,name varchar(100),
age int,dept_name varchar(100),salary int);
insert into employees(name,age,dept_name,salary)values
("Anu",24,"IT",25000),
("Anjana",30,"Accountant",70000),
("Manu",42,"Sales manager",80000),
("Lavanya",21,"Marketing",30000),
("Diya",32,"HR",50000);
select * from employees;
select name,salary from employees;
select * from employees where salary>30000;
select * from employees where dept_name="IT";
update employees set salary=28000 where emp_id=1;
update employees set age=28 where emp_id=1;
delete from employees where age<25;
select * from employees where age<25;
delete from employees where emp_id=4;
select * from employees where salary>30000 and age>25;
select * from employees where salary>50000 or age<25;
select * from employees where not dept_name="IT";
select * from employees where salary between 30000 and 60000;
select * from employees order by salary asc;
select * from employees order by salary desc;
select * from employees order by age asc;
select * from employees order by name asc;
update employees set salary=80000 where emp_id=2;
update employees set age=35 where emp_id=3;
update employees set dept_name="Finance" where emp_id=5;