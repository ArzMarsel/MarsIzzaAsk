from django.db import models


class Course(models.Model):
    title = models.CharField('Название:', max_length=20)
    description = models.TextField('Описание:')
    date1 = models.DateField('Дата начала:')
    date2 = models.DateField("Дата окончания:")
    teachers = models.TextField('Учителя:')
    lecture_title = models.CharField('Лекции', max_length=100)
    lecture_video = models.FileField(upload_to='media/lecture/', max_length=5*1024*1024)

    def __str__(self):
        return self.title

