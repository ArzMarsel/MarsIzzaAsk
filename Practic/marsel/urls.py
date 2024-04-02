from django.urls import path
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create_course/', views.create_course, name='create_course'),
    path('edit_course/<int:course_id>/', views.edit_course, name='edit_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('view_lectures/<int:course_id>/', views.view_lectures, name='view_lectures'),
    path('view_assignments/<int:course_id>/', views.view_assignments, name='view_assignments'),
    path('grade_assignment/<int:assignment_id>/', views.grade_assignment, name='grade_assignment'),
    path('manage_users/', views.manage_users, name='manage_users'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
]