use ELSCDnevnik;
select MIN(ReceiptDate) from Students where FullName like 'Иванов%';
select Class, COUNT(Class) as 'Количество учащихся' from Students group by Class;
select Class, COUNT(Class) as 'Количество учащихся' from Students group by Class HAVING COUNT(Class) >= 2; 