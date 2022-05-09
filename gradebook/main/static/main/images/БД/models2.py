# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Appointedteachers(models.Model):
    appointed_id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey('Teachers', models.DO_NOTHING, verbose_name=u"Учитель")
    subject = models.ForeignKey('Subjects', models.DO_NOTHING, verbose_name=u"Предмет")
    class_field = models.ForeignKey('Classes', models.DO_NOTHING, db_column='class', verbose_name=u"Класс")  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'appointedteachers'
        unique_together = (('teacher', 'subject', 'class_field'),)
        verbose_name = 'Назначение'
        verbose_name_plural = 'Назначения'


class Classes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numberclass = models.IntegerField(db_column='numberClass', verbose_name=u"Номер класса")  # Field name made lowercase.
    titleclass = models.CharField(db_column='titleClass', max_length=1, verbose_name=u"Заголовок класса")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'classes'
        unique_together = (('numberclass', 'titleclass'),)
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class Daysweek(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nameday = models.CharField(db_column='nameDay', max_length=15, blank=True, null=True, verbose_name=u"День недели")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'daysweek'
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'


class Numberslesson(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    time_start = models.TimeField(blank=True, null=True, verbose_name=u"Время начала урока")
    time_end = models.TimeField(blank=True, null=True, verbose_name=u"Время окончания урока")

    class Meta:
        managed = False
        db_table = 'numberslesson'
        verbose_name = 'Номер урока'
        verbose_name_plural = 'Номера уроков'


class Register(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    schoolboyid = models.ForeignKey('Schoolboys', models.DO_NOTHING, db_column='schoolboyId', verbose_name=u"Ученик")  # Field name made lowercase.
    shedulelesson = models.ForeignKey('Schedule', models.DO_NOTHING, db_column='shedulelesson', verbose_name=u"Урок по расписанию")
    rating = models.IntegerField(blank=True, null=True, verbose_name=u"Оценка")
    visit = models.BooleanField(blank=True, null=True,default=True, verbose_name=u"Присутствовал/отсутствовал")

    class Meta:
        managed = False
        db_table = 'register'
        verbose_name = 'Запись журнала'
        verbose_name_plural = 'Записи журнала'


class Roles(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    namerole = models.CharField(db_column='nameRole', max_length=32, blank=True, null=True, verbose_name=u"Роль")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roles'
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class Schedule(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    dayweek = models.ForeignKey(Daysweek, models.DO_NOTHING, db_column='dayWeek', verbose_name=u"День недели")  # Field name made lowercase.
    numberlesson = models.ForeignKey(Numberslesson, models.DO_NOTHING, db_column='numberLesson', verbose_name=u"Номер урока")  # Field name made lowercase.
    school_subject = models.ForeignKey(Appointedteachers, models.DO_NOTHING, db_column='school_subject', verbose_name=u"Предмет")
    datelesson = models.DateField(db_column='dateLesson', blank=True, null=True, verbose_name=u"Дата урока")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'schedule'
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Schoolboys(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    schoolboys_role = models.ForeignKey(Roles, models.DO_NOTHING, db_column='schoolboys_role', verbose_name=u"Роль")
    class_field = models.ForeignKey(Classes, models.DO_NOTHING, db_column='class', verbose_name=u"Класс")  # Field renamed because it was a Python reserved word.
    schoolboyss_login = models.CharField(unique=True, max_length=64, verbose_name=u"Логин")
    schoolboys_password = models.CharField(unique=True, max_length=64, verbose_name=u"Пароль")
    firstname = models.CharField(db_column='FirstName', unique=True, max_length=64, verbose_name=u"Имя")  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', unique=True, max_length=64, verbose_name=u"Фамилия")  # Field name made lowercase.
    patronymic = models.CharField(db_column='Patronymic', unique=True, max_length=64, verbose_name=u"Отчество")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'schoolboys'
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'


class Subjects(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    namesubject = models.CharField(db_column='NameSubject', max_length=32, verbose_name=u"Предмет")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subjects'
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Teachers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    teachers_role = models.ForeignKey(Roles, models.DO_NOTHING, db_column='teachers_role', verbose_name=u"Роль")
    teachers_login = models.CharField(unique=True, max_length=64, verbose_name=u"Логин")
    teachers_password = models.CharField(unique=True, max_length=64, verbose_name=u"Пароль")
    firstname = models.CharField(db_column='FirstName', unique=True, max_length=32, verbose_name=u"Имя")  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', unique=True, max_length=32, verbose_name=u"Фамилия")  # Field name made lowercase.
    patronymic = models.CharField(db_column='Patronymic', unique=True, max_length=32, verbose_name=u"Отчество")  # Field name made lowercase.
    experience = models.IntegerField(blank=True, null=True, verbose_name=u"Стаж")

    class Meta:
        managed = False
        db_table = 'teachers'
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

class Users(models.Model):
    user = models.OneToOneField(User)
    class_field = models.ForeignKey(Classes, models.DO_NOTHING, db_column='class', verbose_name=u"Класс")  # Field renamed because it was a Python reserved word.
    role = models.ForeignKey(Roles, models.DO_NOTHING, db_column='schoolboys_role', verbose_name=u"Роль")
    firstname = models.CharField(db_column='FirstName', unique=True, max_length=64, verbose_name=u"Имя")  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', unique=True, max_length=64, verbose_name=u"Фамилия")  # Field name made lowercase.
    patronymic = models.CharField(db_column='Patronymic', unique=True, max_length=64, verbose_name=u"Отчество")  # Field name made lowercase.
    def __unicode__(self):
        return self.user
 
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'



# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User, Group

class Appointedteachers(models.Model):
    appointed_id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey('Users', on_delete=models.CASCADE, limit_choices_to={'role': 'Учитель'},  verbose_name=u"Учитель")
    subject = models.ForeignKey('Subjects', models.DO_NOTHING, verbose_name=u"Предмет")
    class_field = models.ForeignKey('Classes', models.DO_NOTHING, db_column='class', verbose_name=u"Класс")  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'appointedteachers'
        unique_together = (('teacher', 'subject', 'class_field'),)
        verbose_name = 'Назначение'
        verbose_name_plural = 'Назначения'


class Classes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numberclass = models.IntegerField(db_column='numberClass', verbose_name=u"Номер класса")  # Field name made lowercase.
    titleclass = models.CharField(db_column='titleClass', max_length=1, verbose_name=u"Заголовок класса")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'classes'
        unique_together = (('numberclass', 'titleclass'),)
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class Daysweek(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nameday = models.CharField(db_column='nameDay', max_length=15, blank=True, null=True, verbose_name=u"День недели")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'daysweek'
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'


class Numberslesson(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    time_start = models.TimeField(blank=True, null=True, verbose_name=u"Время начала урока")
    time_end = models.TimeField(blank=True, null=True, verbose_name=u"Время окончания урока")

    class Meta:
        managed = False
        db_table = 'numberslesson'
        verbose_name = 'Номер урока'
        verbose_name_plural = 'Номера уроков'


class Register(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    schoolboyid = models.ForeignKey('Users', on_delete=models.CASCADE, limit_choices_to={'role': 'Ученик'}, db_column='schoolboyId', verbose_name=u"Ученик")  # Field name made lowercase.
    shedulelesson = models.ForeignKey('Schedule', models.DO_NOTHING, db_column='shedulelesson', verbose_name=u"Урок по расписанию")
    rating = models.IntegerField(blank=True, null=True, verbose_name=u"Оценка")
    visit = models.BooleanField(blank=True, null=True,default=True, verbose_name=u"Присутствовал/отсутствовал")

    class Meta:
        managed = False
        db_table = 'register'
        verbose_name = 'Запись журнала'
        verbose_name_plural = 'Записи журнала'


# class Roles(models.Model):
#     id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
#     namerole = models.CharField(db_column='nameRole', max_length=32, blank=True, null=True, verbose_name=u"Роль")  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'roles'
#         verbose_name = 'Роль'
#         verbose_name_plural = 'Роли'


class Schedule(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    dayweek = models.ForeignKey(Daysweek, models.DO_NOTHING, db_column='dayWeek', verbose_name=u"День недели")  # Field name made lowercase.
    numberlesson = models.ForeignKey(Numberslesson, models.DO_NOTHING, db_column='numberLesson', verbose_name=u"Номер урока")  # Field name made lowercase.
    school_subject = models.ForeignKey(Appointedteachers, models.DO_NOTHING, db_column='school_subject', verbose_name=u"Предмет")
    datelesson = models.DateField(db_column='dateLesson', blank=True, null=True, verbose_name=u"Дата урока")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'schedule'
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


# class Schoolboys(models.Model):
#     id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
#     schoolboys_role = models.ForeignKey(Roles, models.DO_NOTHING, db_column='schoolboys_role', verbose_name=u"Роль")
#     class_field = models.ForeignKey(Classes, models.DO_NOTHING, db_column='class', verbose_name=u"Класс")  # Field renamed because it was a Python reserved word.
#     schoolboyss_login = models.CharField(unique=True, max_length=64, verbose_name=u"Логин")
#     schoolboys_password = models.CharField(unique=True, max_length=64, verbose_name=u"Пароль")
#     firstname = models.CharField(db_column='FirstName', unique=True, max_length=64, verbose_name=u"Имя")  # Field name made lowercase.
#     lastname = models.CharField(db_column='LastName', unique=True, max_length=64, verbose_name=u"Фамилия")  # Field name made lowercase.
#     patronymic = models.CharField(db_column='Patronymic', unique=True, max_length=64, verbose_name=u"Отчество")  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'schoolboys'
#         verbose_name = 'Ученик'
#         verbose_name_plural = 'Ученики'


class Subjects(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    namesubject = models.CharField(db_column='NameSubject', max_length=32, verbose_name=u"Предмет")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subjects'
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


# class Teachers(models.Model):
#     id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
#     teachers_role = models.ForeignKey(Roles, models.DO_NOTHING, db_column='teachers_role', verbose_name=u"Роль")
#     teachers_login = models.CharField(unique=True, max_length=64, verbose_name=u"Логин")
#     teachers_password = models.CharField(unique=True, max_length=64, verbose_name=u"Пароль")
#     firstname = models.CharField(db_column='FirstName', unique=True, max_length=32, verbose_name=u"Имя")  # Field name made lowercase.
#     lastname = models.CharField(db_column='LastName', unique=True, max_length=32, verbose_name=u"Фамилия")  # Field name made lowercase.
#     patronymic = models.CharField(db_column='Patronymic', unique=True, max_length=32, verbose_name=u"Отчество")  # Field name made lowercase.
#     experience = models.IntegerField(blank=True, null=True, verbose_name=u"Стаж")

#     class Meta:
#         managed = False
#         db_table = 'teachers'
#         verbose_name = 'Учитель'
#         verbose_name_plural = 'Учителя'

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patronymic = models.CharField(db_column='Patronymic', unique=True, max_length=64, verbose_name=u"Отчество")  # Field name made lowercase.
    class_field = models.ForeignKey(Classes, models.DO_NOTHING, db_column='class', verbose_name=u"Класс")  # Field renamed because it was a Python reserved word.
    role = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='role', verbose_name=u"Роль")
    # firstname = models.CharField(db_column='FirstName', unique=True, max_length=64, verbose_name=u"Имя")  # Field name made lowercase.
    # lastname = models.CharField(db_column='LastName', unique=True, max_length=64, verbose_name=u"Фамилия")  # Field name made lowercase.
    def __unicode__(self):
        return self.user
 
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

# T123ch456


{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="{% static 'main\css\index.css' %}" rel="stylesheet" type="text/css">
    <!-- Bootstrap CSS CDN -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4" crossorigin="anonymous">
    <!-- Our Custom CSS -->
    <link rel="stylesheet" href="{% static 'main\css\styleforteach.css' %}">

    <!-- Font Awesome JS -->
    <script defer src="https://use.fontawesome.com/releases/v5.0.13/js/solid.js" integrity="sha384-tzzSw1/Vo+0N5UhStP3bvwWPq+uvzCMfrN1fEFe+xBmv1C/AtVX5K0uZtmcHitFZ" crossorigin="anonymous"></script>
    <script defer src="https://use.fontawesome.com/releases/v5.0.13/js/fontawesome.js" integrity="sha384-6OIrr52G08NpOFSZdxxz1xdNSndlD4vdcf/q2myIUVO0VsqaGHJsB0RaBE01VTOY" crossorigin="anonymous"></script>
</head>
<body>
    <div class="wrapper">
        <!-- Sidebar  -->
        <nav id="sidebar">
            <div class="sidebar-header">
                <h3>Bootstrap Sidebar</h3>
            </div>
    
            <ul class="list-unstyled components">
                <p>Dummy Heading</p>
                <li class="active">
                    <a href="#homeSubmenu" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">Home</a>
                    <ul class="collapse list-unstyled" id="homeSubmenu">
                        <li>
                           <a href="#">Home 1</a>
                        </li>
                        <li>
                            <a href="#">Home 2</a>
                        </li>
                        <li>
                            <a href="#">Home 3</a>
                        </li>
                    </ul>
                </li>
                <li>
                    <a href="#">About</a>
                </li>
                <li>
                    <a href="#pageSubmenu" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">Pages</a>
                    <ul class="collapse list-unstyled" id="pageSubmenu">
                        <li>
                            <a href="#">Page 1</a>
                        </li>
                        <li>
                            <a href="#">Page 2</a>
                        </li>
                        <li>
                            <a href="#">Page 3</a>
                        </li>
                    </ul>
                </li>
                <li>
                    <a href="#">Portfolio</a>
                </li>
                <li>
                    <a href="#">Contact</a>
                </li>
            </ul>
    
            <ul class="list-unstyled CTAs">
                <li>
                    <a href="https://bootstrapious.com/tutorial/files/sidebar.zip" class="download">Download source</a>
                </li>
                <li>
                    <a href="https://bootstrapious.com/p/bootstrap-sidebar" class="article">Back to article</a>
                </li>
            </ul>
        </nav>
    
            <!-- Page Content  -->
        <div id="content">
    
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <div class="container-fluid">
    
                    <button type="button" id="sidebarCollapse" class="btn btn-info">
                        <svg class="svg-inline--fa fa-align-left fa-w-14" aria-hidden="true" data-prefix="fas" data-icon="align-left" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" data-fa-i2svg=""><path fill="currentColor" d="M288 44v40c0 8.837-7.163 16-16 16H16c-8.837 0-16-7.163-16-16V44c0-8.837 7.163-16 16-16h256c8.837 0 16 7.163 16 16zM0 172v40c0 8.837 7.163 16 16 16h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16zm16 312h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16zm256-200H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16h256c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16z"></path></svg><!-- <i class="fas fa-align-left"></i> -->
                        <span>Toggle Sidebar</span>
                    </button>
                    <button class="btn btn-dark d-inline-block d-lg-none ml-auto" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <svg class="svg-inline--fa fa-align-justify fa-w-14" aria-hidden="true" data-prefix="fas" data-icon="align-justify" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" data-fa-i2svg=""><path fill="currentColor" d="M0 84V44c0-8.837 7.163-16 16-16h416c8.837 0 16 7.163 16 16v40c0 8.837-7.163 16-16 16H16c-8.837 0-16-7.163-16-16zm16 144h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16zm0 256h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16zm0-128h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16z"></path></svg><!-- <i class="fas fa-align-justify"></i> -->
                    </button>
    
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="nav navbar-nav ml-auto">
                            <li class="nav-item active">
                                <a class="nav-link" href="#">Page</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">Page</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">Page</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">Page</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
    
            <h2>Классы</h2>
            <div class="line"></div>
            {% block content%}
                {% for el in classes %}
                <h2>{{el.numberclass}} {{el.titleclass}}</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            
                    <div class="line"></div>
                {% endfor %}
            {% endblock %}
        </div>
    </div>
    
        <!-- jQuery CDN - Slim version (=without AJAX) -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <!-- Popper.JS -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js" integrity="sha384-cs/chFZiN24E4KMATLdqdvsezGxaGsi4hLGOzlXwp5UZB1LY//20VyM2taTB4QvJ" crossorigin="anonymous"></script>
        <!-- Bootstrap JS -->
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js" integrity="sha384-uefMccjFJAIv6A+rW+L4AHf99KvxDjWSu1z9VI8SKNVmz4sk7buKt/6v9KI65qnm" crossorigin="anonymous"></script>
    
        <script type="text/javascript">
            $(document).ready(function () {
                $('#sidebarCollapse').on('click', function () {
                    $('#sidebar').toggleClass('active');
                });
            });
        </script> 


    
    <script src="{% static 'main\js\jquery.min.js' %}"></script>
    <script src="{% static 'main\js\jquery-migrate-3.0.1.min.js' %}"></script>
    <script src="{% static 'main\js\popper.min.js' %}"></script>
    <script src="{% static 'main\js\bootstrap.min.js' %}"></script>
    <script src="{% static 'main\js\jquery.easing.1.3.js' %}"></script>
    <script src="{% static 'main\js\jquery.waypoints.min.js' %}"></script>
    <script src="{% static 'main\js\jquery.stellar.min.js' %}"></script>
    <script src="{% static 'main\js\owl.carousel.min.js' %}"></script>
    <script src="{% static 'main\js\jquery.magnific-popup.min.js' %}"></script>
    <script src="{% static 'main\js\aos.js' %}"></script>
    <script src="{% static 'main\js\jquery.animateNumber.min.js' %}"></script>
    <script src="{% static 'main\js\scrollax.min.js' %}"></script>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBVWaKrjvy3MaE7SQ74_uJiULgl1JY0H2s&sensor=false"></script>
    <script src="{% static 'main\js\google-map.js' %}"></script>
    <script src="{% static 'main\js\main.js' %}"></script>
</body>
</html>






# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver


class Appointedteachers(models.Model):
    appointed_id = models.AutoField(primary_key=True)
    teacher_user = models.ForeignKey('auth.user', on_delete=models.CASCADE,  verbose_name=u"Учитель")
    subject = models.ForeignKey('Subjects', models.DO_NOTHING, verbose_name=u"Предмет")
    # class_field = models.ForeignKey('Classes', models.DO_NOTHING, db_column='class', verbose_name=u"Класс")  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'appointedteachers'
        unique_together = (('teacher_user', 'subject'),) #(('teacher_user', 'subject', 'class_field'),)
        verbose_name = 'Назначение'
        verbose_name_plural = 'Назначения'


class Classes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numberclass = models.IntegerField(db_column='numberClass', verbose_name=u"Номер класса")  # Field name made lowercase.
    titleclass = models.CharField(db_column='titleClass', max_length=1, verbose_name=u"Заголовок класса")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'classes'
        unique_together = (('numberclass', 'titleclass'),)
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class Daysweek(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nameday = models.CharField(db_column='nameDay', max_length=15, blank=True, null=True, verbose_name=u"День недели")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'daysweek'
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'


class Numberslesson(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    time_start = models.TimeField(blank=True, null=True, verbose_name=u"Время начала урока")
    time_end = models.TimeField(blank=True, null=True, verbose_name=u"Время окончания урока")

    class Meta:
        managed = False
        db_table = 'numberslesson'
        verbose_name = 'Номер урока'
        verbose_name_plural = 'Номера уроков'



class Register(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    schoolboyid = models.ForeignKey('Users', on_delete=models.CASCADE, limit_choices_to={'role': 'Ученик'}, db_column='schoolboyId', verbose_name=u"Ученик")  # Field name made lowercase.
    shedulelesson = models.ForeignKey('Schedule', models.DO_NOTHING, db_column='shedulelesson', verbose_name=u"Урок по расписанию")
    rating = models.IntegerField(blank=True, null=True, verbose_name=u"Оценка")
    visit = models.BooleanField(blank=True, null=True,default=True, verbose_name=u"Присутствовал/отсутствовал")

    class Meta:
        managed = False
        db_table = 'register'
        verbose_name = 'Запись журнала'
        verbose_name_plural = 'Записи журнала'


# class Roles(models.Model):
#     id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
#     namerole = models.CharField(db_column='nameRole', max_length=32, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'roles'


class Schedule(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    dayweek = models.ForeignKey(Daysweek, models.DO_NOTHING, db_column='dayWeek', verbose_name=u"День недели")  # Field name made lowercase.
    numberlesson = models.ForeignKey(Numberslesson, models.DO_NOTHING, db_column='numberLesson', verbose_name=u"Номер урока")  # Field name made lowercase.
    school_subject = models.ForeignKey(Appointedteachers, models.DO_NOTHING, db_column='school_subject', verbose_name=u"Предмет")
    school_class = models.ForeignKey(Classes, models.DO_NOTHING, db_column='school_class', verbose_name=u"Класс")
    datelesson = models.DateField(db_column='dateLesson', blank=True, null=True, verbose_name=u"Дата урока")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'schedule'
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


# class Schoolboys(models.Model):
#     id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
#     schoolboys_role = models.ForeignKey(Roles, models.DO_NOTHING, db_column='schoolboys_role')
#     class_field = models.ForeignKey(Classes, models.DO_NOTHING, db_column='class')  # Field renamed because it was a Python reserved word.
#     schoolboyss_login = models.CharField(unique=True, max_length=64)
#     schoolboys_password = models.CharField(unique=True, max_length=64)
#     firstname = models.CharField(db_column='FirstName', unique=True, max_length=64)  # Field name made lowercase.
#     lastname = models.CharField(db_column='LastName', unique=True, max_length=64)  # Field name made lowercase.
#     patronymic = models.CharField(db_column='Patronymic', unique=True, max_length=64)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'schoolboys'


class Subjects(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    namesubject = models.CharField(db_column='NameSubject', max_length=32, verbose_name=u"Предмет")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subjects'
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


# class Teachers(models.Model):
#     id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
#     teachers_role = models.ForeignKey(Roles, models.DO_NOTHING, db_column='teachers_role')
#     teachers_login = models.CharField(unique=True, max_length=64)
#     teachers_password = models.CharField(unique=True, max_length=64)
#     firstname = models.CharField(db_column='FirstName', unique=True, max_length=32)  # Field name made lowercase.
#     lastname = models.CharField(db_column='LastName', unique=True, max_length=32)  # Field name made lowercase.
#     patronymic = models.CharField(db_column='Patronymic', unique=True, max_length=32)  # Field name made lowercase.
#     experience = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'teachers'

class Users(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patronymic = models.CharField(db_column='Patronymic', unique=True, max_length=64, verbose_name=u"Отчество")  # Field name made lowercase.
    class_field = models.ForeignKey(Classes, models.DO_NOTHING, db_column='class', verbose_name=u"Класс")  # Field renamed because it was a Python reserved word.
    # role = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='role', verbose_name=u"Роль")
    # firstname = models.CharField(db_column='FirstName', unique=True, max_length=64, verbose_name=u"Имя")  # Field name made lowercase.
    # lastname = models.CharField(db_column='LastName', unique=True, max_length=64, verbose_name=u"Фамилия")  # Field name made lowercase.
    # def __unicode__(self):
    #     return self.user
 
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Users.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.Users.save()





    #last v
    # This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

# class Roles(models.Model):
#     id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
#     namerole = models.CharField(db_column='nameRole', max_length=32, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'roles'



class Numberslesson(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    time_start = models.TimeField(blank=True, null=True, verbose_name=u"Время начала урока")
    time_end = models.TimeField(blank=True, null=True, verbose_name=u"Время окончания урока")

    class Meta:
        managed = False
        db_table = 'numberslesson'
        verbose_name = 'Номер урока'
        verbose_name_plural = 'Номера уроков'


# class Schoolboys(models.Model):
#     id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
#     schoolboys_role = models.ForeignKey(Roles, models.DO_NOTHING, db_column='schoolboys_role')
#     class_field = models.ForeignKey(Classes, models.DO_NOTHING, db_column='class')  # Field renamed because it was a Python reserved word.
#     schoolboyss_login = models.CharField(unique=True, max_length=64)
#     schoolboys_password = models.CharField(unique=True, max_length=64)
#     firstname = models.CharField(db_column='FirstName', unique=True, max_length=64)  # Field name made lowercase.
#     lastname = models.CharField(db_column='LastName', unique=True, max_length=64)  # Field name made lowercase.
#     patronymic = models.CharField(db_column='Patronymic', unique=True, max_length=64)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'schoolboys'


class Subjects(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    namesubject = models.CharField(db_column='NameSubject', max_length=32, verbose_name=u"Предмет")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subjects'
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


# class Teachers(models.Model):
#     id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
#     teachers_role = models.ForeignKey(Roles, models.DO_NOTHING, db_column='teachers_role')
#     teachers_login = models.CharField(unique=True, max_length=64)
#     teachers_password = models.CharField(unique=True, max_length=64)
#     firstname = models.CharField(db_column='FirstName', unique=True, max_length=32)  # Field name made lowercase.
#     lastname = models.CharField(db_column='LastName', unique=True, max_length=32)  # Field name made lowercase.
#     patronymic = models.CharField(db_column='Patronymic', unique=True, max_length=32)  # Field name made lowercase.
#     experience = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'teachers'
class Daysweek(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nameday = models.CharField(db_column='nameDay', max_length=15, blank=True, null=True, verbose_name=u"День недели")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'daysweek'
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'

class Classes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numberclass = models.IntegerField(db_column='numberClass', verbose_name=u"Номер класса")  # Field name made lowercase.
    titleclass = models.CharField(db_column='titleClass', max_length=1, verbose_name=u"Заголовок класса")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'classes'
        unique_together = (('numberclass', 'titleclass'),)
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

class Appointedteachers(models.Model):
    appointed_id = models.AutoField(primary_key=True)
    teacher_user = models.ForeignKey('auth.user', on_delete=models.CASCADE,  verbose_name=u"Учитель")
    subject = models.ForeignKey('Subjects', models.DO_NOTHING, verbose_name=u"Предмет")
    # class_field = models.ForeignKey('Classes', models.DO_NOTHING, db_column='class', verbose_name=u"Класс")  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'appointedteachers'
        unique_together = (('teacher_user', 'subject'),) #(('teacher_user', 'subject', 'class_field'),)
        verbose_name = 'Назначение'
        verbose_name_plural = 'Назначения'

class Schedule(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    dayweek = models.ForeignKey(Daysweek, models.DO_NOTHING, db_column='dayWeek', verbose_name=u"День недели")  # Field name made lowercase.
    numberlesson = models.ForeignKey(Numberslesson, models.DO_NOTHING, db_column='numberLesson', verbose_name=u"Номер урока")  # Field name made lowercase.
    school_subject = models.ForeignKey(Appointedteachers, models.DO_NOTHING, db_column='school_subject', verbose_name=u"Предмет")
    # class_field = models.ForeignKey(Classes, models.DO_NOTHING, db_column='class', verbose_name=u"Класс")
    datelesson = models.DateField(db_column='dateLesson', blank=True, null=True, verbose_name=u"Дата урока")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'schedule'
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

class Users(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patronymic = models.CharField(db_column='Patronymic', unique=True, max_length=64, verbose_name=u"Отчество")  # Field name made lowercase.
    # class_field = models.OneToOneField(Classes, models.DO_NOTHING, db_column='class', verbose_name=u"Класс")  # Field renamed because it was a Python reserved word.
    # role = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='role', verbose_name=u"Роль")
    # firstname = models.CharField(db_column='FirstName', unique=True, max_length=64, verbose_name=u"Имя")  # Field name made lowercase.
    # lastname = models.CharField(db_column='LastName', unique=True, max_length=64, verbose_name=u"Фамилия")  # Field name made lowercase.
    # def __unicode__(self):
    #     return self.user
 
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Users.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.users.save()


class Register(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    schoolboyid = models.ForeignKey('Users', on_delete=models.CASCADE, limit_choices_to={'role': 'Ученик'}, db_column='schoolboyId', verbose_name=u"Ученик")  # Field name made lowercase.
    shedulelesson = models.ForeignKey('Schedule', models.DO_NOTHING, db_column='shedulelesson', verbose_name=u"Урок по расписанию")
    rating = models.IntegerField(blank=True, null=True, verbose_name=u"Оценка")
    visit = models.BooleanField(blank=True, null=True,default=True, verbose_name=u"Присутствовал/отсутствовал")

    class Meta:
        managed = False
        db_table = 'register'
        verbose_name = 'Запись журнала'
        verbose_name_plural = 'Записи журнала'