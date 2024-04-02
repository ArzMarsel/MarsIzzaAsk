from django.db import models


class Course(models.Model):
    title = models.CharField('Название:', max_length=20)
    description = models.TextField('Описание:')
    date1 = models.DateField('Дата начала:')
    date2 = models.DateField("Дата окончания:")
    teachers = models.TextField('Учителя:')
    lecture_title = models.CharField('Лекции', max_length=100)
    lecture_video = models.FileField(upload_to='media/lectures/', max_length=5*1024*1024)
    video_url = models.URLField('URL видео')

    def __str__(self):
        return self.title


class Exercise(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField('Название задания:', max_length=50)
    description = models.TextField('Описание задания:')
    deadline = models.DateTimeField('Срок сдачи:')

    def __str__(self):
        return self.title


class Solution(models.Model):
    assignment = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    student_name = models.CharField('Имя студента:', max_length=50)
    file = models.FileField(upload_to='solutions/')

    def __str__(self):
        return f"Решение для задания '{self.assignment.title}' от {self.student_name}"

class Exercise(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField('Название задания:', max_length=50)
    description = models.TextField('Описание задания:')
    deadline = models.DateTimeField('Срок сдачи:')

    def __str__(self):
        return self.title


class Solution(models.Model):
    assignment = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    student_name = models.CharField('Имя студента:', max_length=50)
    file = models.FileField(upload_to='solutions/')

    def __str__(self):
        return f"Решение для задания '{self.assignment.title}' от {self.student_name}"
