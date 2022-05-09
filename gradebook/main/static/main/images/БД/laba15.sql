SET SQL_SAFE_UPDATES=0;
USE ELSCDnevnik;
START TRANSACTION;
set @dates := "2015-01-01";
-- set @number := "12345";
-- update students set ReceiptDate = @dates where ReceiptDate = "2004-01-01";
-- update students set Numbers = @number where ReceiptDate = @dates;
update students set Class = (SELECT id FROM Classes where Classes.num = year(@dates) - year(students.ReceiptDate));
COMMIT;
SET SQL_SAFE_UPDATES=1;
select * from students
-- select year('2010-01-01') - year('2007-01-01')

-- SET SQL_SAFE_UPDATES=0;
-- USE ELSCDnevnik;
-- START TRANSACTION;
-- set @dates := "2005-01-01";
-- -- set @number := "12345";
-- update students set ReceiptDate = @dates where ReceiptDate = "2004-01-01";
-- -- update students set Numbers = @number where ReceiptDate = @dates;
-- update students set Class = (SELECT id FROM Classes where students.Class = Classes.id-1);
-- COMMIT;
-- SET SQL_SAFE_UPDATES=1;
-- select * from students