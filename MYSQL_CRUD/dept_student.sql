use june_b1;
create table departments(dept_id int primary key,department_name varchar(100) not null,hod_name varchar(100),mobile_number bigint unique);
create table students (student_id int primary key,department_id int,student_name varchar(100),place varchar(100) not null,college varchar(100),
contact_number bigint unique,foreign key (department_id) references department(dept_id));
insert into departments values
(1, 'python', 'Anil', 9876543210),
(2, 'mern ', 'Binu', 9876543211),
(3, '.net', 'Arun', 9876543212),
(4, 'data science', 'Deepa', 9876543213),
(5, 'data analytics', 'Amal', 9876543214);
show tables;
select * from departments;
insert into students values
(101, 1, 'akhil', 'kochi', 'stc college', 9812345671),
(102, 2, 'anu', 'thrissur', 'kmea college', 9823456782),
(103, 1, 'arun', 'kochi', 'stcpcz college', 9834567893),
(104, 3, 'meera', 'kottayam', 'sh college', 9845678904),
(105, 4, 'amal', 'ernakulam', 'kmm college', 9856789015);
select * from students;
select department_name from departments;
select student_name,place from students;
select * from  students where college="kmm college";
select * from departments where hod_name like 'A%';
select distinct college from students;
select * from students where place="Kochi";
select department_id,student_name from students;
select * from departments where mobile_number like '%7';
select * from departments where mobile_number like '%3';
select s.student_name,d.department_name from students s inner join 
departments d on d.dept_id = s.department_id;
select department_id,count(*) as Number_of_students from students 
group by department_id;
select department_name, hod_name from departments;
select * from students where department_id!=2;
select department_name from departments where department_name
like '%science%';
select * from students where contact_number like '98%';
select count(*) as Total_number_of_departments from departments;
select student_name, college, place from students
order by student_name desc;
select avg(department_id) from students;
select college,count(*) as Number_of_students from students
group by college; 