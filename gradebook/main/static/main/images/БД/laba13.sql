USE ELSCDnevnik;
-- create table Ins(
-- 	id int auto_increment primary key,
--     Fullname_in varchar(300), 
--     id_in int
-- );
-- create table Up(
-- 	id int auto_increment primary key,
--     Fullname_up varchar(300),
--     id_up int,
--     isDelete int default 0
-- );
-- create table Dele(
-- 	id int auto_increment primary key,
--     Fullname_del varchar(300), 
--     id_del int
-- );

-- drop trigger trigIns;
-- DELIMITER //
-- create TRIGGER  trigIns  after insert on Students
-- for each row insert into Ins (Fullname_in, id_up) values (New.Fullname, New.id); //
-- -- select * from Students
-- -- delete from Students where id = 12;
-- insert into Students (FullName, Numbers, Class, ReceiptDate) values('Тютч Ф.Е.', 81081, 2, '2008-01-01');
-- select * from Ins;

-- drop trigger trigUp;
-- SET SQL_SAFE_UPDATES=0;
-- DELIMITER //
-- create TRIGGER  trigUp  after update on Students
-- for each row insert into Up (Fullname_up, id_up) values (New.Fullname, New.id); //
-- update Students set ReceiptDate = '2002-12-01' where ReceiptDate = '2008-01-01';
-- select * from Up;
-- SET SQL_SAFE_UPDATES=1;

SET SQL_SAFE_UPDATES=0;
drop trigger del_trig;
DELIMITER //
create TRIGGER  del_trig  before delete on Students
for each row insert into Dele (Fullname_del, id_del) values (old.Fullname, old.id); //
select * from Dele;
delete from Students where ReceiptDate = '2002-12-01';
select * from Dele;
SET SQL_SAFE_UPDATES=1;
-- DELIMITER //
-- create TRIGGER  InsTrigUp on Students instead of delete
-- for each row update Up set isDelete = 1 //
-- delete from Students where ReceiptDate = '2002-12-01'
-- select * from Up;