-- use test_for_labs;


-- create procedure select_all_officiants() select fio from officiants;
-- drop procedure new_officiant;

-- create procedure new_officiant (new_fio varchar(300),  new_start_date_work varchar(300)) insert into officiants (fio, start_date_work) values (new_fio, new_start_date_work);
-- drop procedure new_officiant;

-- call new_officiant('Котов В.Л.', '2020-01-01');
-- call select_all_officiants;

-- DELIMITER $$
-- create function `id_officiant_from_fio` (param varchar(300)) returns int 
-- DETERMINISTIC  
-- BEGIN  
-- set @name_ = (select id from officiants where fio =  param);
-- return (@name_);
-- end  $$
-- DELIMITER ;
  
-- drop function id_officiant_from_fio;

-- select id_officiant_from_fio('Васильев Е.В.');
-- DELIMITER //
-- create procedure select_officiant_id (ofId int)
-- 	begin
-- 		select * from officiants where id = ofId;
--     end
--     //
-- delimiter ;
-- call select_officiant_id(1); 