# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Appointedteachers(models.Model):
    teacer = models.OneToOneField('Teachers', models.DO_NOTHING, primary_key=True)
    subject = models.ForeignKey('Subjects', models.DO_NOTHING)
    class_field = models.ForeignKey('Classes', models.DO_NOTHING, db_column='class')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'appointedteachers'
        unique_together = (('teacer', 'subject', 'class_field'),)


class Classes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numberclass = models.IntegerField(db_column='numberClass')  # Field name made lowercase.
    titleclass = models.CharField(db_column='titleClass', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'classes'


class Daysweek(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nameday = models.CharField(db_column='nameDay', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'daysweek'


class Numberslesson(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    time_start = models.DateTimeField(blank=True, null=True)
    time_end = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'numberslesson'


class Register(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    teacher = models.ForeignKey(Appointedteachers, models.DO_NOTHING, db_column='teacher', related_name='teacher2teachers')
    schoolboyid = models.ForeignKey('Schoolboys', models.DO_NOTHING, db_column='schoolboyId')  # Field name made lowercase.
    school_subject = models.ForeignKey(Appointedteachers, models.DO_NOTHING, db_column='school_subject', related_name='school_subject2school_subjects')
    shedulelesson = models.ForeignKey('Schedule', models.DO_NOTHING, db_column='shedulelesson')
    rating = models.IntegerField(blank=True, null=True)
    visit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'register'


class Roles(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    namerole = models.CharField(db_column='nameRole', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roles'


class Schedule(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    dayweek = models.ForeignKey(Daysweek, models.DO_NOTHING, db_column='dayWeek')  # Field name made lowercase.
    numberlesson = models.ForeignKey(Numberslesson, models.DO_NOTHING, db_column='numberLesson')  # Field name made lowercase.
    school_subject = models.ForeignKey(Appointedteachers, models.DO_NOTHING, db_column='school_subject', related_name='schedule_subject2schedule_subjects')
    class_field = models.ForeignKey(Appointedteachers, models.DO_NOTHING, db_column='class', related_name='class2classes')  # Field renamed because it was a Python reserved word.
    datelesson = models.DateTimeField(db_column='dateLesson', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'schedule'


class Schoolboys(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    schoolboys_role = models.ForeignKey(Roles, models.DO_NOTHING, db_column='schoolboys_role')
    class_field = models.ForeignKey(Classes, models.DO_NOTHING, db_column='class')  # Field renamed because it was a Python reserved word.
    schoolboyss_login = models.CharField(unique=True, max_length=64)
    schoolboys_password = models.CharField(unique=True, max_length=64)
    firstname = models.CharField(db_column='FirstName', unique=True, max_length=64)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', unique=True, max_length=64)  # Field name made lowercase.
    patronymic = models.CharField(db_column='Patronymic', unique=True, max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'schoolboys'


class Subjects(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    namesubject = models.CharField(db_column='NameSubject', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subjects'


class Teachers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    teachers_role = models.ForeignKey(Roles, models.DO_NOTHING, db_column='teachers_role')
    teachers_login = models.CharField(unique=True, max_length=64)
    teachers_password = models.CharField(unique=True, max_length=64)
    firstname = models.CharField(db_column='FirstName', unique=True, max_length=32)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', unique=True, max_length=32)  # Field name made lowercase.
    patronymic = models.CharField(db_column='Patronymic', unique=True, max_length=32)  # Field name made lowercase.
    experience = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teachers'

<!-- <h2>Классы</h2>
            <div class="line"></div> -->
            <!-- {% block content%}
                {% for el in classes %}
                <h2>{{el.numberclass}} {{el.titleclass}}</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            
                    <div class="line"></div>
                {% endfor %}
            {% endblock %} -->