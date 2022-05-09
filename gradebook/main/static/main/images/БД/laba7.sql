USE ELSCDnevnik;
-- -- drop table ClassesN;
-- -- drop table StudentsN;
-- create TABLE ClassesN (
-- 	Id int primary key auto_increment,
--     ClassAdmin varchar(300) not null check (ClassAdmin != ''),
--     Cabinets int check (Cabinets > 0),
--     Korpus varchar(300) not null check (Korpus != ''),
--     AdresKorpus varchar(300) not null check (AdresKorpus != '')
-- );
-- create TABLE StudentsN (
-- 	Id int primary key auto_increment,
--     FullName varchar(300) not null check (FullName != '') unique,
--     Class int References Classes (Id),
--     ReceiptDate datetime default '2010-01-01'
-- );
-- insert into StudentsN (FullName, Class, ReceiptDate) values('Иванов Константин Федорович.', 1, '2003-01-01');
-- insert into StudentsN (FullName, Class, ReceiptDate) values('Петров Андрей Иванович.', 1, '2003-04-01');
-- insert into StudentsN (FullName, Class, ReceiptDate) values('Сидоров Никита Петровив.', 1, '2003-02-01');
-- insert into StudentsN (FullName, Class, ReceiptDate) values('Федор Николай Сидорович.', 2, '2004-05-01');

SELECT * FROM Students WHERE Class in (SELECT Id FROM Classes where Floor = 3);
-- SELECT * FROM Students
SELECT FullName, Class,ReceiptDate, (SELECT ClassAdmin FROM Classes where Classes.Id = Students.Class) AS ClassAdmins FROM Students;
-- (SELECT ClassAdmin FROM Classes where ClassAdmin = 'Зубкова А.О.') - доделать пункт 2
-- insert into Classes (ClassAdmin, Cabinets, Floor) values('Петренокао К.Ф.', 302, 3);
-- delete from Classes where Id = 7;
-- SELECT * FROM Classes where (not exists(select Class from Students where Class = Classes.Id));
-- insert into Students (FullName, Numbers, Class, ReceiptDate) values('Копачи А.Т.', 79082, (SELECT Id from Classes where ClassAdmin = 'Петрова В.Е.'), '2015-01-01');
-- SELECT * FROM Students;