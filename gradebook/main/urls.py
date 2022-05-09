from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth, name='auth'),
    # path('login', views.login, name='login'),
    path('teacher', views.teacher, name='teacher'),
    path('learner', views.learner, name='learner'),
    path('Tshedule', views.Tshedule, name='Teacher shedule'),
    path('Lshedule', views.Lshedule, name='Learner shedule'),
    path('Ldnevnik', views.Ldnevnik, name='Learner dnevnik'),
    path('Tdnevnik', views.Tdnevnik, name='Teacher dnevnik'),
    path('<int:pk>', views.ObjectDetailView.as_view(), name='object-detail'),
    path('<int:pk>t', views.TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>r', views.RegisterCreateView.as_view(), name='register-create')
    # path('director', views.director, name='director'),
    # path('login/', views.LoginView.as_view(), name='login')
]
