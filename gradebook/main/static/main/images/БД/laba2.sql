USE ELSCDnevnik;
-- drop table Classes;
-- drop table Students;
create TABLE Classes (
	Id int primary key auto_increment,
    ClassAdmin varchar(300) not null check (ClassAdmin != ''),
    Cabinets int check (Cabinets > 0),
    Floor int default 1
);
create TABLE Students (
	Id int primary key auto_increment,
    FullName varchar(300) not null check (FullName != '') unique,
    Numbers int not null  check (Numbers != ''),
    Class int References Classes (Id),
    ReceiptDate datetime default '2010-01-01'
);