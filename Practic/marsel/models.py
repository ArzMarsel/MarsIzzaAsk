from django.db import models


class Course(models.Model):
    title = models.CharField('Название:', max_length=20)
    description = models.TextField('Описание:')
    date1 = models.DateField('Дата начала:')
    date2 = models.DateField("Дата окончания:")
    teachers = models.TextField('Учителя:')

    def __str__(self):
        return self.title

