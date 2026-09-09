create database event_db;
use event_db;
create table event(
       id int auto_increment primary key,
       event_name varchar(100),
       event_type varchar(50),
       venue varchar(100),
       organizer varchar(100),
       phone varchar(100) unique,
       event_date date
);
show tables;
select * from event;
