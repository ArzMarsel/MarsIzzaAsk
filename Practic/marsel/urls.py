from django.urls import path
from .views import register, user_login, dashboard

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('dashboard/', dashboard, name='dashboard')
]
