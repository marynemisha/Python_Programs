create database healthdb;
use healthdb;
create table Patient(id int primary key auto_increment,
                     name varchar(100),age int,gender varchar(10),
                     disease varchar(100),phone varchar(15));
insert into Patient(name,age,gender,disease,phone)
values('Anjali', 25, 'Female', 'Fever', '9876543210'),
('Rahul', 40, 'Male', 'Diabetes', '9876543211'),
('Meera', 32, 'Female', 'Asthma', '9876543212'),
('Arun', 50, 'Male', 'Blood Pressure', '9876543213'),
('Sneha', 28, 'Female', 'Migraine', '9876543214');
show tables;
select * from Patient;
                     
                     
                     
                     
                     