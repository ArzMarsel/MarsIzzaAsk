# Generated by Django 5.0.3 on 2024-04-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marsel', '0004_alter_course_lecture_video_exercise_solution'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='video_url',
            field=models.URLField(default=1, verbose_name='URL видео'),
            preserve_default=False,
        ),
    ]
