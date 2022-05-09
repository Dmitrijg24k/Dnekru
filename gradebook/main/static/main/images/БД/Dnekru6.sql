-- drop database Dnekru;
-- create database Dnekru;
use Dnekru;

-- create table daysWeek (
-- 	Id int primary key auto_increment,
--     nameDay varchar(15)
-- );
-- drop table numbersLesson;
-- create table numbersLesson (
-- 	Id int primary key auto_increment,
--     time_start time,
--     time_end time
-- );
-- drop table register;
-- drop table schedule;

-- create table schedule (
-- 	Id int primary key auto_increment,
--     dayWeek int not null, 
--     numberLesson int not null,
--     school_subject int not null,
-- 	FOREIGN KEY (dayWeek) references daysWeek(Id) on delete cascade,
-- 	FOREIGN KEY (numberLesson) references numbersLesson(Id) on delete cascade,
--     FOREIGN KEY (school_subject) references appointedTeachers(subject_id) on delete cascade,
--     dateLesson date
-- ); 
-- drop table roles;
-- create table roles (
-- 	Id int primary key auto_increment,
--     nameRole varchar(32)
-- );
-- create Table register (
-- 	Id int primary key auto_increment,
--     schoolboyId int not null,
--     school_subject int not null,
--     shedulelesson int not null,
--     FOREIGN KEY (schoolboyId) references schoolboys(Id) ON DELETE CASCADE,
--     FOREIGN KEY (school_subject) references appointedTeachers(subject_id) ON DELETE CASCADE,
--     FOREIGN KEY (shedulelesson) references schedule(Id) on delete cascade,
--     rating int,
--     visit bool default True
-- );
-- drop table teachers;
-- create Table teachers (
-- 	Id int primary key auto_increment,
--     teachers_role int not null,
-- 	teachers_login varchar(64) not null check (teachers_login != '') unique,
--     teachers_password varchar(64) not null check (teachers_password != '') unique , 
--     FOREIGN KEY (teachers_role) references roles(Id) on delete cascade,
--     FirstName varchar(32) not null check (FirstName != '') unique,
--     LastName varchar(32) not null check (LastName != '') unique,
--     Patronymic varchar(32) not null check (Patronymic != '') unique,
--     experience int
-- );
-- -- -- хэш тдельно или тут?
-- create Table subjects (
-- 	Id int primary key auto_increment,
--     NameSubject varchar(32) not null check (NameSubject != '')
-- );
-- drop table appointedTeachers;
-- drop table schoolboys;
-- drop table classes;
-- create Table classes (
-- 	Id int primary key auto_increment,
-- 	numberClass int not null check (numberClass != ''),
--     titleClass char not null check (titleClass != ''),
--     UNIQUE(numberClass, titleClass)
--     -- CONSTRAINT fullClasses FOREIGN KEY  (numberClass, titleClass)
-- );
-- create Table appointedTeachers (
-- 	appointed_id int PRIMARY KEY auto_increment,
-- 	teacher_id INT NOT NULL,
--     subject_id INT NOT NULL,
--     class int not null, -- class_number
--     UNIQUE(teacher_id, subject_id, class),
--     -- CONSTRAINT appointed_id PRIMARY KEY  (teacer_id, subject_id, class), -- appointed_id
--     FOREIGN KEY (teacher_id) REFERENCES teachers (Id) ON DELETE CASCADE,
-- 	FOREIGN KEY (subject_id) REFERENCES subjects (Id) ON DELETE CASCADE,
--     FOREIGN KEY (class) REFERENCES classes (Id) ON DELETE CASCADE
-- );
-- create Table schoolboys(
-- 	Id int primary key auto_increment,
--     schoolboys_role int not null,
--     class int not null,
--     schoolboyss_login varchar(64) not null check (schoolboyss_login != '') unique,
--     schoolboys_password varchar(64) not null check (schoolboys_password != '') unique , 
--     FOREIGN KEY (schoolboys_role) references roles(Id) on delete cascade,
--     FirstName varchar(64) not null check (FirstName != '') unique,
--     LastName varchar(64) not null check (LastName != '') unique,
--     Patronymic varchar(64) not null check (Patronymic != '') unique,
--     FOREIGN KEY (class) references classes(Id) on delete cascade
-- );