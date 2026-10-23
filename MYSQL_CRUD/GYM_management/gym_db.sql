create database gym_db;
use gym_db;
create table member(id int auto_increment primary key,
            name varchar(100),
		    place varchar(100),
            mobile varchar(15),
            plan enum("1 month","2 months","4 months","6 months","8 months","1 year"),
            fee int,
            joined_on date);
show tables;
select * from member;
desc member;