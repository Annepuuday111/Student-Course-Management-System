# Generated by Django 5.0 on 2024-02-20 08:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0008_course_program'),
        ('facultyapp', '0008_alter_coursecontent_chapter_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadWork',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('submission_date', models.DateField(auto_now_add=True)),
                ('file_upload', models.FileField(upload_to='workuploads')),
                ('course_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facultyapp.coursecontent')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.student')),
            ],
            options={
                'db_table': 'uploadwork_table',
            },
        ),
    ]