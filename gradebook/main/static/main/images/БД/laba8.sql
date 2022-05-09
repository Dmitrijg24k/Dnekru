USE ELSCDnevnik;
SELECT Students.FullName, Students.ReceiptDate, Classes.ClassAdmin, Classes.Cabinets, Classes.Floor FROM Students, Classes WHERE Students.Class = Classes.Id;
SELECT Students.FullName, Students.ReceiptDate, Classes.ClassAdmin, Classes.Cabinets, Classes.Floor FROM Students JOIN Classes ON Students.Class = Classes.Id;
SELECT Students.FullName, Students.ReceiptDate, Classes.ClassAdmin, Classes.Cabinets, Classes.Floor FROM Students LEFT JOIN Classes ON Students.Class = Classes.Id;
SELECT Students.FullName, Students.ReceiptDate, Classes.ClassAdmin, Classes.Cabinets, Classes.Floor FROM Students RIGHT JOIN Classes ON Students.Class = Classes.Id;
-- create TABLE ClassAdmins (
-- 	Id int primary key auto_increment,
--     FullName varchar(300) not null check (FullName != '') unique,
--     Numbers int not null  check (Numbers != ''),
--     Document varchar(300) not null check (Document != '') unique
-- );
-- insert into ClassAdmins (FullName, Numbers, Document) values('Иванова К.Ф.', 880055, "1405-198024"), ('Зубкова А.О.', 890055, "1245-128024"), ('Константинова А.О.', 870055, "1455-191224"), ('Петрова В.Е.', 840355, "1856-198024"), ('Сидорова Т.А.', 874375, "1405-198354"), ('Петренко К.Ф.', 849255, "1470-198024");
-- SELECT * FROM ClassAdmins
-- insert into ClassAdmins (FullName, Numbers, Document) values('Морозова Т.А.', 880385, "1405-238024");
SELECT FullName FROM ClassAdmins
UNION
SELECT ClassAdmin FROM Classes;
-- SELECT FullName FROM ClassAdmins where FullName not in (SELECT ClassAdmin FROM Classes);
SELECT FullName FROM ClassAdmins where FullName in (SELECT ClassAdmin FROM Classes);