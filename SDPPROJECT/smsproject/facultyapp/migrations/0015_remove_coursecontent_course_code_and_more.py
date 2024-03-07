# Generated by Django 5.0 on 2024-02-22 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0008_course_program'),
        ('facultyapp', '0014_remove_coursecontent_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursecontent',
            name='course_code',
        ),
        migrations.AddField(
            model_name='coursecontent',
            name='course',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='adminapp.course'),
            preserve_default=False,
        ),
    ]
