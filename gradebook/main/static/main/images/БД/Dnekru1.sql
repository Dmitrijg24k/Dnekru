-- create database Dnekru
use Dnekru;
-- create table roles (
-- 	id int primary key auto_increment,
--     nameRole varchar(32)
-- );
-- drop table register;
-- create Table register (
-- 	Id int primary key auto_increment,
--     teacher int references appointedTeachers(teacer_id) ON DELETE CASCADE,
--     schoolboyId int references schoolboys(Id) ON DELETE CASCADE,
-- --     class_number int references schoolboys(class_number) ON DELETE CASCADE,
-- --     class_title int references schoolboys(class_title) ON DELETE CASCADE,
--     school_subject int references appointedTeachers(subject_id) ON DELETE CASCADE,
--     rating int,
--     visit bool default True,
--     lesson_date datetime unique
-- );
-- create Table teachers (
-- 	Id int primary key auto_increment,
-- 	teachers_login varchar(64) not null check (teachers_login != '') unique,
--     teachers_password varchar(64) not null check (teachers_password != '') unique , 
--     teachers_role int,
--     FirstName varchar(32) not null check (FirstName != '') unique,
--     LastName varchar(32) not null check (LastName != '') unique,
--     Patronymic varchar(32) not null check (Patronymic != '') unique,
--     experience int
-- );
-- -- хэш тдельно или тут?
-- create Table subjects (
-- 	Id int primary key auto_increment,
--     NameSubject varchar(32) not null check (NameSubject != '')
-- );
-- create Table classes (
-- 	numberClass int not null check (numberClass != '') unique,
--     titleClass char not null check (titleClass != '') unique,
--     CONSTRAINT Id PRIMARY KEY  (numberClass, titleClass)
-- );
-- create Table appointedTeachers (
-- 	teacer_id INT NOT NULL,
--     subject_id INT NOT NULL,
--     class_number int not null,
--     class_title char not null,
--     CONSTRAINT class_id FOREIGN KEY (class_number, class_title) references classes (numberClass,titleClass) ON DELETE CASCADE,
--     CONSTRAINT appointed_id PRIMARY KEY  (teacer_id, subject_id, class_number, class_title), -- appointed_id
--     INDEX teacer_id (teacer_id),
--     INDEX subject_id (subject_id),
--     INDEX class_number (class_number),
--     INDEX class_title (class_title),
--     FOREIGN KEY (teacer_id) REFERENCES teachers (Id) ON DELETE CASCADE,
-- 	FOREIGN KEY (subject_id) REFERENCES subjects (Id) ON DELETE CASCADE,
--     FOREIGN KEY (class_number) REFERENCES classes (numberClass) ON DELETE CASCADE,
--     FOREIGN KEY (class_title) REFERENCES classes (titleClass) ON DELETE CASCADE
-- );
drop table schoolboys;
create Table schoolboys(
	Id int primary key auto_increment,
    schoolboyss_login varchar(64) not null check (schoolboyss_login != '') unique,
    schoolboys_password varchar(64) not null check (schoolboys_password != '') unique , 
    schoolboys_role int references roles(Id),
    FirstName varchar(64) not null check (FirstName != '') unique,
    LastName varchar(64) not null check (LastName != '') unique,
    Patronymic varchar(64) not null check (Patronymic != '') unique,
    class_number int references classes(numberClass) on delete cascade,
    class_title char references classes(titleClass) on delete cascade
);