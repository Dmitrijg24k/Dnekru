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
from datetime import date, timedelta
import datetime
from django.urls import reverse
# teiuy6h3la путь от request до response в Джанго
class Classes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numberclass = models.IntegerField(db_column='numberClass')  # Field name made lowercase.
    titleclass = models.CharField(db_column='titleClass', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'classes'
        unique_together = (('numberclass', 'titleclass'),)
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

class Useres(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # patronymic = models.CharField(db_column='Patronymic', unique=True, max_length=64, verbose_name=u"Отчество")  # Field name made lowercase.
    # class_field = models.OneToOneField('Classes', on_delete=models.CASCADE)  # Field renamed because it was a Python reserved word.
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
        Useres.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.useres.save()

class Schooler(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    user = models.OneToOneField(Useres, on_delete=models.CASCADE)
    class_field = models.ForeignKey('Classes', on_delete=models.CASCADE,  verbose_name=u"Класс")
    role = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='role', verbose_name=u"Роль")
    class Meta:
        db_table = 'schooler'
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

# class Name(models.Model):
#     id = models.AutoField(db_column='Id', primary_key=True)
#     user = models.OneToOneField(Useres, on_delete=models.CASCADE)
#     name = models.CharField(db_column='Name', max_length=32)
#     class Meta:
#         db_table = 'name'
#         verbose_name = 'Имя'
#         verbose_name_plural = 'Имена'

class Teachers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    user = models.OneToOneField(Useres, on_delete=models.CASCADE)
    role = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='role', verbose_name=u"Роль")
    class Meta:
        db_table = 'Teachers'
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

class Appointedteachers(models.Model):
    appointed_id = models.AutoField(primary_key=True)
    teacher_user = models.ForeignKey('Teachers', on_delete=models.CASCADE,  verbose_name=u"Учитель")
    subject = models.ForeignKey('Subjects', models.DO_NOTHING, verbose_name=u"Предмет")
    # class_field = models.ForeignKey('Classes', models.DO_NOTHING, db_column='class', verbose_name=u"Класс")  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'appointedteachers'
        unique_together = (('teacher_user', 'subject'),) #(('teacher_user', 'subject', 'class_field'),)
        verbose_name = 'Назначение'
        verbose_name_plural = 'Назначения'


class Daysweek(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nameday = models.CharField(db_column='nameDay', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'daysweek'
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'


class Numberslesson(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    time_start = models.TimeField(blank=True, null=True)
    time_end = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'numberslesson'
        verbose_name = 'Номер урока'
        verbose_name_plural = 'Номера уроков'


class Register(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    schoolboyid = models.ForeignKey('Schooler', on_delete=models.CASCADE, db_column='schoolboyId', verbose_name=u"Ученик")  # Field name made lowercase.
    shedulelesson = models.ForeignKey('Fullschedule', models.DO_NOTHING, db_column='shedulelesson', verbose_name=u"Урок по расписанию")
    rating = models.IntegerField(blank=True, null=True, verbose_name=u"Оценка")
    visit = models.BooleanField(blank=True, null=True,default=True, verbose_name=u"Присутствовал/отсутствовал")

    class Meta:
        managed = False
        db_table = 'register'
        verbose_name = 'Запись журнала'
        verbose_name_plural = 'Записи журнала'
    def get_absolute_url(self):
        return 'Tdnevnik'

class Schedule(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    dayweek = models.ForeignKey(Daysweek, models.DO_NOTHING, db_column='dayWeek')  # Field name made lowercase.
    numberlesson = models.ForeignKey(Numberslesson, models.DO_NOTHING, db_column='numberLesson')  # Field name made lowercase.
    school_class = models.ForeignKey(Classes, models.DO_NOTHING, db_column='school_class')
    school_subject = models.ForeignKey(Appointedteachers, models.DO_NOTHING, db_column='school_subject')
    # home_task = models.CharField(db_column='Task', max_length=255)
    # datelesson = models.DateField(db_column='dateLesson', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'schedule'
        verbose_name = 'Урок'
        verbose_name_plural = 'Расписание'
    def get_absolute_url(self):
        return '/'


class Fullschedule(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    day = models.OneToOneField(Schedule, models.DO_NOTHING, db_column='day')
    home_task = models.CharField(db_column='home_task', max_length=255)
    datelesson = models.DateField(db_column='datelesson', blank=True, null=True)  # Field name made lowercase.
    
    def get_absolute_url(self):
        return 'Tdnevnik'

    class Meta:
        managed = False
        db_table = 'fullschedule'
        verbose_name = 'Заполненный урок'
        verbose_name_plural = 'Заполненные уроки'

#-----------------
@receiver(post_save, sender=Schedule)
def create_shedule_day(sender, instance, created, **kwargs):
    if created:
        todaymonth = date.today().month
        delta = timedelta(days=7)
        year = date.today().year
        if todaymonth <= 6:
            start_date = date(year, 1, 6)
            end_date = date(year, 6, 27)
        else:
            start_date = date(year, 6, 28)
            end_date = date(year, 12, 31)
        deltaone = timedelta(days=1)
        while start_date.weekday() != instance.dayweek.id-1: #instance.dayweek.id
            start_date += deltaone
            print(start_date.weekday(), instance.dayweek.id)
        while start_date <= end_date:
            Fullschedule.objects.create(day=instance, datelesson = start_date)
            start_date += delta

@receiver(post_save, sender=Schedule)
def save_shedule_day(sender, instance, **kwargs):
    instance.fullschedule.save()


class Subjects(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    namesubject = models.CharField(db_column='NameSubject', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subjects'
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
# teiuy6h3la