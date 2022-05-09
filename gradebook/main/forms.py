from .models import Classes, Useres, Schooler,Fullschedule, Teachers, Appointedteachers, Daysweek, Numberslesson, Register, Schedule, Subjects
from django.forms import ModelForm, TextInput, DateTimeInput, ModelChoiceField

class UtiliModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        # print('label')
        return obj.datelesson

class HometaskForms(ModelForm):
    #datelesson = UtiliModelChoiceField(queryset=Fullschedule.objects.all()) 
    class Meta:
        model = Fullschedule
        fields = ['home_task']



class UtilisateurModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        # print('label')
        return obj.user.user.first_name +" " + obj.user.user.last_name

class RaitingForms(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop("request")
    #     super(RaitingForms, self).__init__(*args, **kwargs)
    #     self.fields["schoolboyid"].queryset = Schooler.objects.filter(owner=self.request.user)
    #     self.fields["whatever"].queryset = WhateverModel.objects.filter(user=self.request.user)
    schoolboyid = UtilisateurModelChoiceField(queryset=Schooler.objects.all()) 
    class Meta:
        model = Register
        fields = ['schoolboyid', 'rating', 'visit']