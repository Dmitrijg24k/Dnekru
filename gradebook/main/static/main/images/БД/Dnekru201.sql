drop database gradebook2;
create database gradebook2;
use gradebook2;
-- select * from django_migrations
create table daysWeek (
	Id int primary key auto_increment,
    nameDay varchar(15)
);
-- drop table numbersLesson;
create table numbersLesson (
	Id int primary key auto_increment,
    time_start time,
    time_end time
);
create Table subjects (
	Id int primary key auto_increment,
    NameSubject varchar(32) not null check (NameSubject != '')
);
create Table classes (
	Id int primary key auto_increment,
	numberClass int not null check (numberClass != ''),
    titleClass char not null check (titleClass != ''),
    UNIQUE(numberClass, titleClass)
    -- CONSTRAINT fullClasses FOREIGN KEY  (numberClass, titleClass)
);
create Table appointedTeachers (
	appointed_id int PRIMARY KEY auto_increment,
    subject_id INT NOT NULL,
    teacher_user_id int,
    UNIQUE(subject_id),
    -- CONSTRAINT appointed_id PRIMARY KEY  (teacer_id, subject_id, class), -- appointed_id
	FOREIGN KEY (subject_id) REFERENCES subjects (Id) ON DELETE CASCADE
);
-- drop table register;
-- drop table schedule;
create table schedule (
	Id int primary key auto_increment,
    dayWeek int not null, 
    numberLesson int not null,
    school_class int not null,
    school_subject int not null,
	FOREIGN KEY (dayWeek) references daysWeek(Id) on delete cascade,
	FOREIGN KEY (numberLesson) references numbersLesson(Id) on delete cascade,
    FOREIGN KEY (school_class) references Classes(Id) on delete cascade,
    FOREIGN KEY (school_subject) references appointedTeachers(appointed_id) on delete cascade,
    dateLesson date
); 
create Table register (
	Id int primary key auto_increment,
    shedulelesson int not null,
    schoolboyId int,
    FOREIGN KEY (shedulelesson) references schedule(Id) on delete cascade,
    rating int,
    visit bool default True
);

insert into Classes (numberClass, titleClass) values(1, 'А');
insert into daysWeek (nameDay) values('Понедельник');
insert into subjects (NameSubject) values('Математика');