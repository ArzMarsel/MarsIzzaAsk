from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField('Название:', max_length=20)
    description = models.TextField('Описание:')
    date1 = models.DateField('Дата начала:')
    date2 = models.DateField("Дата окончания:")
    teachers = models.ManyToManyField(User, related_name='courses')
    lecture_title = models.CharField('Лекции', max_length=100)
    lecture_video = models.FileField(upload_to='media/lecture/', max_length=5 * 1024 * 1024)

    def __str__(self):

        return self.title


class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_url = models.URLField()

    def __str__(self):
        return self.title


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    grade = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title
