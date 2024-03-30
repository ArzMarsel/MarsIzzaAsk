from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('teacher_login/', views.teacher_login, name='teacher_login'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard')
    path('', views.dashboard, name='dashboard')
]
