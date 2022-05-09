use ELSCDnevnik;
select FullName as 'Фамилия Имя Отчество', Class, ReceiptDate from Students where ReceiptDate > '2008-09-01';
select * from Classes where Floor in (2,3) and ClassAdmin like 'Круглова%';
select * from Students where ReceiptDate < '2008-09-01' and ReceiptDate > '2002-09-01' and Numbers like '%891765%';
select * from Students where FullName like 'Иванов%';
select * from Students;