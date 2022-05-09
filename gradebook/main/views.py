from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from .models import Classes, Useres, Schooler,Fullschedule, Teachers, Appointedteachers, Daysweek, Numberslesson, Register, Schedule, Subjects
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth.decorators import user_passes_test
from datetime import date, timedelta
import datetime
from .forms import HometaskForms, RaitingForms
#from .models import Appointedteachers, Classes, Daysweek, Numberslesson, Register, Schedule, Subjects, Users
# Create your views here.
# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = auth.authenticate(username=username, password=password)
#     if user is not None and user.is_active:
#         # Правильный пароль и пользователь "активен"
#         auth.login(request, user)
#         # Перенаправление на "правильную" страницу
#         return HttpResponseRedirect("?next=/mypage/")
#     # else:
#     #     # Отображение страницы с ошибкой
#     #     return HttpResponseRedirect("/ge/q/")

def auth(request):
    group = Group.objects.get(pk=1).name
    usgroup = request.user.groups.filter(name=group).exists()
    urluser = ''
    if usgroup:
        urluser = '/teacher'
    else:
        urluser = 'learner'
    return render(request, 'main/auth.html', {'urluser':urluser})
def is_in_multiple_groups(user):
    group = Group.objects.get(pk=1).name
    return user.groups.filter(name=group).exists()
def is_in_multiple_groups2(user):
    group = Group.objects.get(pk=2).name
    return user.groups.filter(name=group).exists()
# def login(request):
#     return render(request, 'main/login2.html')
@login_required
@user_passes_test(is_in_multiple_groups)
def teacher(request):
    classes = Classes.objects.all()
    # subjects = Subjects.objects.filter()
    userone = Useres.objects.filter(user__username = request.user.username).values('id')
    # userone = userone.filter(user__username = request.user.username)
    # subjects = userone[0]['id']
    teachere = Teachers.objects.filter(user__id = userone[0]['id']).values('id')
    apointed = Appointedteachers.objects.filter(teacher_user__id = teachere[0]['id']).values('appointed_id')
    sub = []
    for i in range(len(apointed)):
        sub.append(apointed[i]['appointed_id'])
    subjects = Subjects.objects.filter(appointedteachers__appointed_id__in = sub)
    schedule = Schedule.objects.filter(school_subject__appointed_id__in = sub).order_by('numberlesson')
    daysweek = Daysweek.objects.all()
    shedweek = []
    daysofweekfull = []
    for i in range(len(daysweek)):
        shedweek.append([])
        sheduledays = schedule.filter(dayweek = daysweek[i]).values('numberlesson')
        sheduledaysid = schedule.filter(dayweek = daysweek[i]).values('id')
        # daysweekes = Daysweek.objects.all().values('id')
        shedweek[i].append(daysweek[i].nameday)
        shedweek[i].append([])
        for j in range(len(sheduledaysid)):
            shedweek[i][1].append([])
            # if i == 1:
            #     ut = 1
                # class2 = Classes.objects.get(schedule__id = sheduledaysid[j]['id'])# .distinct()    # subjects = Subjects.objects.filter()
                # subjec2 = Subjects.objects.get(appointedteachers__appointed_id = sheduledaysid[j]['id']) #.distinct()
            class1 = Classes.objects.get(schedule__id = sheduledaysid[j]['id'])# .distinct()    # subjects = Subjects.objects.filter()
            subjec1 = Subjects.objects.get(appointedteachers__schedule__id = sheduledaysid[j]['id']) #.distinct()
            if not class1:
                break
            else:
                shedweek[i][1][j].append(sheduledays[j]['numberlesson'])
                shedweek[i][1][j].append(class1.numberclass)
                shedweek[i][1][j].append(class1.titleclass)
                shedweek[i][1][j].append(subjec1.namesubject)
    today = date.today().weekday()
    # subjects = Subjects.objects.filter(Appointedteachers__teacher_user__id = userone[0]['id'])
    return render(request, 'main/teacher.html', {'shedweek': shedweek[today], 'subjects': subjects})
    # if request.user.is_authenticated():
    #     return render(request, 'main/teacher.html') #{'classes': classes}
    # else:
    #     return render(request, 'main/anonim.html')
def Tshedule(request):
    # subjects = Subjects.objects.filter()
    userone = Useres.objects.filter(user__username = request.user.username).values('id')
    # userone = userone.filter(user__username = request.user.username)
    # subjects = userone[0]['id']
    teachere = Teachers.objects.filter(user__id = userone[0]['id']).values('id')
    apointed = Appointedteachers.objects.filter(teacher_user__id = teachere[0]['id']).values('appointed_id')
    sub = []
    daysweek = Daysweek.objects.all()
    for i in range(len(apointed)):
        sub.append(apointed[i]['appointed_id'])
    shedule = Schedule.objects.filter(school_subject__appointed_id__in = sub).order_by('numberlesson')
    # time = shedule[0]['datelesson']
    shed = Schedule.objects.filter(school_subject__appointed_id__in = sub).order_by('numberlesson').values('id')
    shed_id=[]
    for i in range(len(shed)):
        shed_id.append(shed[i]['id'])
    # subjects = Subjects.objects.filter(appointedteachers__appointed_id__in = sub)
    classes = Classes.objects.filter(schedule__school_subject__appointed_id__in = sub)# .distinct()    # subjects = Subjects.objects.filter()
    subjects = Subjects.objects.filter(appointedteachers__appointed_id__in = sub) #.distinct()
    shedweek = []
    daysofweekfull = []
    for i in range(len(daysweek)):
        shedweek.append([])
        sheduledays = shedule.filter(dayweek = daysweek[i]).values('numberlesson')
        sheduledaysid = shedule.filter(dayweek = daysweek[i]).values('id')
        # daysweekes = Daysweek.objects.all().values('id')
        shedweek[i].append(daysweek[i].nameday)
        shedweek[i].append([])
        for j in range(len(sheduledaysid)):
            shedweek[i][1].append([])
            # if i == 1:
            #     ut = 1
                # class2 = Classes.objects.get(schedule__id = sheduledaysid[j]['id'])# .distinct()    # subjects = Subjects.objects.filter()
                # subjec2 = Subjects.objects.get(appointedteachers__appointed_id = sheduledaysid[j]['id']) #.distinct()
            class1 = Classes.objects.get(schedule__id = sheduledaysid[j]['id'])# .distinct()    # subjects = Subjects.objects.filter()
            subjec1 = Subjects.objects.get(appointedteachers__schedule__id = sheduledaysid[j]['id']) #.distinct()
            if not class1:
                break
            else:
                shedweek[i][1][j].append(sheduledays[j]['numberlesson'])
                shedweek[i][1][j].append(class1.numberclass)
                shedweek[i][1][j].append(class1.titleclass)
                shedweek[i][1][j].append(subjec1.namesubject)
    # subjects = Subjects.objects.filter(Appointedteachers__teacher_user__id = userone[0]['id'])
    # daysofweekfull = [i for i in range(len(shedweek))]
    # lessonofdayfull = [[j for j in range(1,len(shedweek[i]))] for i in range(len(shedweek))]
    # permissions = Permission.objects.filter(user=request.user)
    # us = permissions[0]
    #te = Subjects.objects.filter(schedule__school_subject__appointed_id = sub) #.distinct()
    return render(request, 'main/Tshedule.html', {'shedweek': shedweek, 'schedule': shedule})

def Tdnevnik(request):
    userone = Useres.objects.filter(user__username = request.user.username).values('id')
    teachere = Teachers.objects.filter(user__id = userone[0]['id']).values('id')
    #apointed = Appointedteachers.objects.filter(teacher_user__id = teachere[0]['id']).values('appointed_id')
    fullschedule = Fullschedule.objects.filter(day__school_subject__teacher_user__id = teachere[0]['id']).order_by('datelesson')
    fullscheduledays = Fullschedule.objects.filter(day__school_subject__teacher_user__id = teachere[0]['id']).order_by('datelesson').values('datelesson')
    #te = Subjects.objects.filter(schedule__school_subject__appointed_id = sub) #.distinct()
    daysweek = Daysweek.objects.all()

    allweek = []
    keke = Fullschedule.objects.filter(datelesson = fullscheduledays[0]['datelesson']).values('id')
    kekeid = keke[0]['id']
    start = fullscheduledays[0]['datelesson']
    end = fullscheduledays[len(fullscheduledays)-1]['datelesson']
    i = 0
    delta = timedelta(days=1)
    while start < end:
        # allweek.append(fullscheduledays[i]['datelesson'])
        allweek.append([])
        numbers = fullschedule.filter(datelesson = start)
        numbersid = fullschedule.filter(datelesson = start).values('id')
        allweek[i].append(start)
        # dayweek = daysweek[start.weekday()].values('nameday')
        # allweek[i].append(dayweek[0]['nameday'])
        allweek[i].append(daysweek[start.weekday()].nameday)
        allweek[i].append([])
        for j in range(len(numbers)):
            allweek[i][2].append([])
            number = numbers.filter(id = numbersid[j]['id'])
            lesson = number.values('day__numberlesson')
            home_task = number.values('home_task')
            #teacher = number.values('day__school_subject__teacher_user__user__first_name')
            subj = number.values('day__school_subject__subject__namesubject')
            allweek[i][2][j].append(lesson[0]['day__numberlesson'])
            allweek[i][2][j].append(home_task[0]['home_task'])
            #allweek[i][2][j].append(teacher[0]['day__school_subject__teacher_user__user__first_name'])
            allweek[i][2][j].append(subj[0]['day__school_subject__subject__namesubject'])
            oneid = number.values('id')
            allweek[i][2][j].append(oneid[0]['id'])
        start += delta
        i+=1
    #te = Subjects.objects.filter(schedule__school_subject__appointed_id = sub) #.distinct()
    #contact_list = Contact.objects.all()
    paginator = Paginator(allweek, 7) # Show 7 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/Tdnevnik.html', {'page_obj': page_obj})


def create(request):
    error = ''
    if request.method == 'POST':
        form = HometaskForms(request.POST)
        if form.is_valid:
            form.save()
            return(redirect(''))
        else:
            error = "Форма введена неверно"

    form = HometaskForms()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/updateht.html', data)

class TaskUpdateView(UpdateView):
    model = Fullschedule
    template_name = 'main/updateht.html'
    # context_object_name = 'subjects'
    form_class = HometaskForms

class RegisterCreateView(CreateView):
    # model = Register
    template_name = 'main/updaterg.html'
    # context_object_name = 'subjects'
    form_class = RaitingForms
    # t = 0
    # def get_context_data(self, **kwargs):
    #     context = super(RegisterCreateView, self).get_context_data(**kwargs)
    #     t = self.kwargs.get('pk')
    #     context['ratingses'] = t
    #     return context
    def form_valid(self, form):
        #form.instance.shedulelesson = Creator.objects.get(user=self.request.user)
        fullschedule = Fullschedule.objects.get(id=self.kwargs['pk'])
        self.object = form.save(commit=False)
        self.object.shedulelesson = fullschedule
        self.object.save()
        return super(RegisterCreateView, self).form_valid(form)
    # def get_queryset(self):
    #     userone = Useres.objects.filter(user__username = self.request.user.username).values('id')
    #     register = Register.objects.filter(schoolboyid__user__id = userone[0]['id'])
    #     self.ratingses = register.filter(shedulelesson__day__school_subject=self.kwargs['pk'])
    #     return Subjects.objects.all()
    # form_class.shedulelesson = t

@user_passes_test(is_in_multiple_groups2)
def learner(request):
    userone = Useres.objects.filter(user__username = request.user.username).values('id')
    learners = Schooler.objects.filter(user__id = userone[0]['id']).values('class_field')
    schedule = Schedule.objects.filter(school_class__id = learners[0]['class_field']).order_by('numberlesson')
    scheduleid = Schedule.objects.filter(school_class__id = learners[0]['class_field']).values('school_subject')
    sub = []
    for i in range(len(scheduleid)):
        sub.append(scheduleid[i]['school_subject'])
    subjects = Subjects.objects.filter(appointedteachers__appointed_id__in = sub)
    daysweek = Daysweek.objects.all()
    shedweek = []
    daysofweekfull = []
    for i in range(len(daysweek)):
        shedweek.append([])
        sheduledays = schedule.filter(dayweek = daysweek[i]).values('numberlesson')
        sheduledaysid = schedule.filter(dayweek = daysweek[i]).values('id')
        # daysweekes = Daysweek.objects.all().values('id')
        shedweek[i].append(daysweek[i].nameday)
        shedweek[i].append([])
        for j in range(len(sheduledaysid)):
            shedweek[i][1].append([])
            # if i == 1:
            #     ut = 1
                # class2 = Classes.objects.get(schedule__id = sheduledaysid[j]['id'])# .distinct()    # subjects = Subjects.objects.filter()
                # subjec2 = Subjects.objects.get(appointedteachers__appointed_id = sheduledaysid[j]['id']) #.distinct()
            class1 = Classes.objects.get(schedule__id = sheduledaysid[j]['id'])# .distinct()    # subjects = Subjects.objects.filter()
            subjec1 = Subjects.objects.get(appointedteachers__schedule__id = sheduledaysid[j]['id']) #.distinct()
            if not class1:
                break
            else:
                shedweek[i][1][j].append(sheduledays[j]['numberlesson'])
                shedweek[i][1][j].append(class1.numberclass)
                shedweek[i][1][j].append(class1.titleclass)
                shedweek[i][1][j].append(subjec1.namesubject)
    today = date.today().weekday()
    #te = Subjects.objects.filter(schedule__school_subject__appointed_id = sub) #.distinct()
    return render(request, 'main/learner.html', {'subjects': subjects, 'shedweek': shedweek[today]})


def Lshedule(request):
    userone = Useres.objects.filter(user__username = request.user.username).values('id')
    learners = Schooler.objects.filter(user__id = userone[0]['id']).values('class_field')
    schedule = Schedule.objects.filter(school_class__id = learners[0]['class_field']).order_by('numberlesson')
    scheduleid = Schedule.objects.filter(school_class__id = learners[0]['class_field']).values('school_subject')
    sub = []
    daysweek = Daysweek.objects.all()
    for i in range(len(scheduleid)):
        sub.append(scheduleid[i]['school_subject'])
    # classes = Classes.objects.filter(schedule__school_subject__appointed_id__in = sub)# .distinct()    # subjects = Subjects.objects.filter()
    # subjects = Subjects.objects.filter(appointedteachers__appointed_id__in = sub) #.distinct()
    shedweek = []
    daysofweekfull = []
    for i in range(len(daysweek)):
        shedweek.append([])
        sheduledays = schedule.filter(dayweek = daysweek[i]).values('numberlesson')
        sheduledaysid = schedule.filter(dayweek = daysweek[i]).values('id')
        # daysweekes = Daysweek.objects.all().values('id')
        shedweek[i].append(daysweek[i].nameday)
        shedweek[i].append([])
        for j in range(len(sheduledaysid)):
            shedweek[i][1].append([])
            # if i == 1:
            #     ut = 1
                # class2 = Classes.objects.get(schedule__id = sheduledaysid[j]['id'])# .distinct()    # subjects = Subjects.objects.filter()
                # subjec2 = Subjects.objects.get(appointedteachers__appointed_id = sheduledaysid[j]['id']) #.distinct()
            class1 = Classes.objects.get(schedule__id = sheduledaysid[j]['id'])# .distinct()    # subjects = Subjects.objects.filter()
            subjec1 = Subjects.objects.get(appointedteachers__schedule__id = sheduledaysid[j]['id']) #.distinct()
            if not class1:
                break
            else:
                shedweek[i][1][j].append(sheduledays[j]['numberlesson'])
                shedweek[i][1][j].append(class1.numberclass)
                shedweek[i][1][j].append(class1.titleclass)
                shedweek[i][1][j].append(subjec1.namesubject)
    # subjects = Subjects.objects.filter(Appointedteachers__teacher_user__id = userone[0]['id'])
    # daysofweekfull = [i for i in range(len(shedweek))]
    # lessonofdayfull = [[j for j in range(1,len(shedweek[i]))] for i in range(len(shedweek))]
    # permissions = Permission.objects.filter(user=request.user)
    # us = permissions[0]
    #te = Subjects.objects.filter(schedule__school_subject__appointed_id = sub) #.distinct()
    return render(request, 'main/Lschedule.html', {'shedweek': shedweek, 'schedule': schedule})


def Ldnevnik(request):
    userone = Useres.objects.filter(user__username = request.user.username).values('id')
    learners = Schooler.objects.filter(user__id = userone[0]['id']).values('class_field')
    fullscheduledays = Fullschedule.objects.filter(day__school_class__id = learners[0]['class_field']).order_by('datelesson').values('datelesson')

    daysweek = Daysweek.objects.all()

    allweek = []
    start = fullscheduledays[0]['datelesson']
    end = fullscheduledays[len(fullscheduledays)-1]['datelesson']
    i = 0
    delta = timedelta(days=1)
    while start < end:
        # allweek.append(fullscheduledays[i]['datelesson'])
        allweek.append([])
        numbers = Fullschedule.objects.filter(datelesson = start)
        numbersid = Fullschedule.objects.filter(datelesson = start).values('id')
        allweek[i].append(start)
        # dayweek = daysweek[start.weekday()].values('nameday')
        # allweek[i].append(dayweek[0]['nameday'])
        allweek[i].append(daysweek[start.weekday()].nameday)
        allweek[i].append([])
        for j in range(len(numbers)):
            allweek[i][2].append([])
            number = numbers.filter(id = numbersid[j]['id'])
            lesson = number.values('day__numberlesson')
            home_task = number.values('home_task')
            #teacher = number.values('day__school_subject__teacher_user__user__first_name')
            subj = number.values('day__school_subject__subject__namesubject')
            allweek[i][2][j].append(lesson[0]['day__numberlesson'])
            allweek[i][2][j].append(home_task[0]['home_task'])
            #allweek[i][2][j].append(teacher[0]['day__school_subject__teacher_user__user__first_name'])
            allweek[i][2][j].append(subj[0]['day__school_subject__subject__namesubject'])
        start += delta
        i+=1
    #contact_list = Contact.objects.all()
    paginator = Paginator(allweek, 7) # Show 7 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # fa = allweek[0]
    # te = Subjects.objects.filter(schedule__school_subject__appointed_id = sub) #.distinct()
    return render(request, 'main/Ldnevnik.html', {'page_obj': page_obj})



class ObjectDetailView(DetailView):
    model = Subjects
    template_name = 'main/details_view.html'
    context_object_name = 'subjects'
    def get_context_data(self, **kwargs):
        context = super(ObjectDetailView, self).get_context_data(**kwargs)
        context['ratings'] = self.regist
        return context
    def get_queryset(self):
        userone = Useres.objects.filter(user__username = self.request.user.username).values('id')
        register = Register.objects.filter(schoolboyid__user__id = userone[0]['id'])
        self.regist = register.filter(shedulelesson__day__school_subject__subject=self.kwargs['pk'])
        return Subjects.objects.all()
