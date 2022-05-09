USE ELSCDnevnik;
-- create procedure select_all_students() select Fullname from Students;
-- call select_all_students;
-- drop procedure select_all_students;

-- create procedure new_student (new_Fullname varchar(300),  new_Numbers int, new_Class int , new_ReceiptDate datetime) insert into Students (Fullname, Numbers, Class, ReceiptDate) values (new_Fullname,  new_Numbers, new_Class, new_ReceiptDate);
-- call new_student('Смиркин Т.Ф.', 75421, 2, '2005-01-01');
-- drop procedure new_student;
-- select * from Students;

-- DELIMITER $$
-- 	create function `id_student_about_fullname` (new_Fullname varchar(300)) returns int 
-- 	DETERMINISTIC  
-- 	BEGIN  
-- 		set @FIO_ = (select id from Students where Fullname =  new_Fullname);
-- 		return (@FIO_);
-- 	end  $$
-- DELIMITER ;

-- select id_student_about_fullname('Смиркин Т.Ф.');
-- drop function id_student_about_fullname;

-- DELIMITER ??
-- create procedure select_id_student (Id_student int)
-- 	begin
-- 		select * from Students where id = Id_student;
--     end
--     ??
-- delimiter ;
-- call select_id_student(10); 
-- drop procedure select_id_student;