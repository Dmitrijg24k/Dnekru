-- use test_for_labs;
-- create table inserted(
-- 	id int auto_increment primary key,
--     id_inserted int,
--     fio_inserted varchar(300)
-- )
create table updated(
	id int auto_increment primary key,
    id_updated int,
    fio_updated varchar(300)
);
-- DELIMITER ;
-- DELIMITER //
-- create TRIGGER  insert_trig  after insert on officiants
-- for each row
-- insert into inserted(id_inserted, fio_inserted) values (New.id, New.fio) //
-- select min(start_date_work) from officiants;
-- insert into officiants (fio, start_date_work) value ('Иванков В.Г.', '2019-12-31');



-- DELIMITER //
-- create TRIGGER  update_trig  after update on officiants
-- for each row insert into updated (id_updated, fio_updated) select id, fio from inserted;

-- DELIMITER //
-- create TRIGGER  delete_trig  after delete on officiants
-- for each row insert into updated (id_updated, fio_updated) select id, fio from inserted;

-- DELIMITER //
-- create TRIGGER  delete_officiant on officiants instead iff delete
-- for each row update officiants set isDelete = 1 where id = (select id from deleted)