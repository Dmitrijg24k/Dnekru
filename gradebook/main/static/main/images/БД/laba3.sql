-- USE ELSCDnevnik;
-- insert into Classes (ClassAdmin, Cabinets, Floor) values('Зубкова А.О.', 301, 3);
-- insert into Classes (ClassAdmin, Cabinets, Floor) values('Константинова А.О.', 301, default);
-- insert into Classes (ClassAdmin, Cabinets, Floor) values('Иванова К.Ф.', 201, 2), ('Петрова В.Е.', 201, 2), ('Сидорова Т.А.', 201, 3);
-- insert into Students (FullName, Numbers, Class, ReceiptDate) values('Пирагов К.Ф.', 79081, 1, '2015-01-01'), ('Смирнов В.Е.', 79041, 2, default), ('Копятин Т.А.', 79064, 3, '2011-04-05');
-- SET SQL_SAFE_UPDATES = 0;
-- update Students set Numbers = 79042 where FullName = 'Смирнов В.Е';
-- update Classes set Floor = 2 where Cabinets = 201;
-- insert into Students (FullName, Numbers, Class, ReceiptDate) values('Смирнов К.Ф.', 79081, 1, '2006-01-01');
-- SET SQL_SAFE_UPDATES = 0;
-- delete from Students where ReceiptDate < '2007-09-01'
insert into Students (FullName, Numbers, Class, ReceiptDate) values('Иванов К.Ф.', 88005, 1, '2003-01-01');