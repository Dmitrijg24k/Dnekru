USE ELSCDnevnik;
-- create view InfoAboutStudents as select Students.FullName as 'ФИО', Students.ReceiptDate as 'дата поступления', Classes.ClassAdmin as 'Классный руководитель', Classes.Cabinets as 'Кабинеты', Classes.Floor as 'Этаж' FROM Students JOIN Classes ON Students.Class = Classes.Id;
-- select * from InfoAboutStudents;

-- alter view InfoAboutStudents as select Students.FullName as 'ФИО', Students.Numbers as 'Номер', Students.ReceiptDate as 'дата поступления', Classes.ClassAdmin as 'Классный руководитель', Classes.Cabinets as 'Кабинеты', Classes.Floor as 'Этаж' FROM Students JOIN Classes ON Students.Class = Classes.Id;
-- select * from InfoAboutStudents;

-- drop view InfoAboutStudents;

-- create  view InfoAboutStudents as select FullName, ReceiptDate from Students;
-- select * from InfoAboutStudents;


-- insert into InfoAboutStudents(FullName, ReceiptDate) values ('Твердов А.К.', '2005-11-19');
-- update InfoAboutStudents set ReceiptDate = '2006-11-19' where FullName = 'Твердов А.К.';
-- delete from InfoAboutStudents where ReceiptDate = '2006-11-19'
-- select * from show_officiants;

-- drop table InfoAbouClasses;
-- create temporary table InfoAbouClasses(
-- 	Id int primary key auto_increment,
--     ClassAdmin varchar(300) not null check (ClassAdmin != ''),
--     Cabinets int check (Cabinets > 0),
--     Floor int default 1
-- );
-- insert into InfoAbouClasses (select * from Classes where Floor = 2);
-- select * from InfoAbouClasses;

select * from Students as ManyPeople;
