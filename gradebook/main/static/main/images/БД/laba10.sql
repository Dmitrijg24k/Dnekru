USE ELSCDnevnik;
SET @HFloor = (SELECT MAX(Floor) FROM Classes);
select @HFloor;
drop procedure if exists procedure1;
-- SELECT @HFloor;
DELIMITER //
create procedure procedure1() 
begin
	DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    SELECT 'SQLException invoked';
    set @c := 30;
    while @c>0 do 
        set @c:=@c-1; 
        insert into Classes (ClassAdmin, Cabinets, Floor) VALUES('Сидорова Т.А.', 300 + @c, 3);
        SELECT * from Classes;
    end while;
end;//
CALL procedure1();


-- insert into Classes (ClassAdmin, Cabinets, Floor) VALUES('Сидорова Т.А.', CAST(concat('2', CONVERT(10,char)) as INT),  2);

-- select CAST(concat('2', CONVERT(10,char));
-- select 200 + 30
-- SELECT Id, IF(Floor > 2, "Только для старшеклассников.", "Для младших классов") FROM Classes;
-- SELECT @i := 0;
-- UPDATE `ClassAdmins` SET `FullName`=CONCAT('Проект ', @i := @i+1) ORDER BY `id`;


-- create procedure load_user_test_data()
-- begin
-- declare v_max int default 1000;
-- declare v_counter int default 0;
--   truncate table users;
--   start transaction;
--   while v_counter < v_max do
--     # random query
--     insert into users (username) values (CONCAT("user", floor(0 + (rand() * 65535))));
--     set v_counter = v_counter + 1;
--   end while;
--   commit;
-- end

-- SET @number = 30;
-- WHILE @number > 0
--     BEGIN
-- 		insert into Classes (ClassAdmin, Cabinets, Floor) ('Иванова К.Ф.', @number, 1);
--         SET @number = @number - 1
--     END;
-- BEGIN TRY
--     INSERT INTO Students (FullName, Numbers, Class, ReceiptDate) values('Пирагов К.Ф.', 79081, "1", '2015-01-01'); -- Этаж записан как строка
-- END TRY
-- BEGIN CATCH
--     SELECT "ERROR FLOOR"
-- END CATCH
-- BEGIN TRY
--     INSERT INTO Students (FullName, Numbers, Class, ReceiptDate) values('Пирагов К.Ф.', "1", '2015-01-01'); -- Numbers не должен быть пустым
-- END TRY
-- BEGIN CATCH
--     SELECT "ERROR Numbers"
-- END CATCH
--  

