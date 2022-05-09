-- drop view show_officiants;
-- 1 create view show_officiants as select officiants.fio as 'ФИО', officiants.start_date_work as 'Дата начала работы' from `tables` join officiants on officiants.id = `tables`.oficciant_id with check option;
-- select * from show_officiants;
-- 2 alter view show_officiants as select officiants.fio as 'ФИО', officiants.start_date_work as 'Дата начала работы', officiants.id as 'id официанта' from `tables` join officiants on officiants.id = `tables`.oficciant_id with check option;
-- select * from show_officiants;
-- drop view show_officiants;
-- create  view show_officiants as select fio, start_date_work from officiants with check option;
-- select * from show_officiants;
-- insert into show_officiants(fio, start_date_work) values ('Мясников Д.В.', '2019-12-29');
update show_officiants set fio = 'Игнатьев Л.Р.' where fio = 'Игнатьев Л.П.';
select * from show_officiants;
-- select * from show_officiants;

# табличные переменные не поддерживаются mysql

-- 6
create temporary table current_officiants(
	id int auto_increment primary key,
	fio_ varchar(300),
    start_date_works timestamp);
insert into current_officiants (select * from officiants where (year(start_date_work) = 2019));
select * from current_officiants;

-- 7
select * from officiants as kek;