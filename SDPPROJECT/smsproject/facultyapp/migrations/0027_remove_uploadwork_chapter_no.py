# Generated by Django 5.0 on 2024-02-29 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0026_uploadwork_chapter_no_alter_uploadwork_uploded_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadwork',
            name='chapter_no',
        ),
    ]
