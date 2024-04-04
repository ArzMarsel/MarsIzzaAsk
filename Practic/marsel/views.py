from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from .forms import RegistrationForm, LoginForm, CourseForm
from .models import Course, Lecture, Assignment
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Неверное имя пользователя или пароль. Пожалуйста, попробуйте снова.')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('dashboard')


def dashboard(request):
    course = Course.objects.order_by('-date1')
    return render(request, 'main/header.html', {'course': course})


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})


def edit_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CourseForm(instance=course)
    return render(request, 'edit_course.html', {'form': form})


def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('dashboard')
    return render(request, 'delete_course.html', {'course': course})


def view_lectures(request, course_id):
    lectures = Lecture.objects.filter(course_id=course_id)
    return render(request, 'view_lectures.html', {'lectures': lectures})


def view_assignments(request, course_id):
    assignments = Assignment.objects.filter(course_id=course_id)
    return render(request, 'view_assignments.html', {'assignments': assignments})


def grade_assignment(request, assignment_id):
    if request.method == 'POST':
        assignment = Assignment.objects.get(id=assignment_id)
        assignment.grade = request.POST.get('grade')
        assignment.save()
        return redirect('view_assignments')
    else:
        assignment = Assignment.objects.get(id=assignment_id)
        return render(request, 'grade_assignment.html', {'assignment': assignment})


def manage_users(request):
    users = User.objects.all()
    return render(request, 'manage_users.html', {'users': users})


def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('manage_users')
    else:
        return render(request, 'edit_user.html', {'user': user})

# @login_required
# def lectures(request, course_id):
#    course = Course.objects.get(id=course_id)
#    lecture_video = course.lecture_video
#    video_url = lecture_video.url
#    return render(request, 'lectures.html', {'course': course, 'lectures': lectures})

