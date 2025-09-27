create database Laura;
set character set utf8;

create table users(
    id INT auto_increment primary key,
    nameu varchar(100),
    email varchar (100),
    passwordu varchar (20),
    datecu timestamp default current_timestamp
);