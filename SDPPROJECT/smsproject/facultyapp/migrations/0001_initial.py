# Generated by Django 5.0 on 2024-03-14 03:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseQuiz',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_code', models.CharField(max_length=100)),
                ('quiz_title', models.CharField(max_length=100)),
                ('question', models.CharField(max_length=255)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'coursequiz_table',
            },
        ),
        migrations.CreateModel(
            name='UploadWork',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student_id', models.CharField(max_length=15)),
                ('topic_name', models.CharField(max_length=30)),
                ('uploded_file', models.FileField(upload_to='uploadwork/')),
            ],
            options={
                'db_table': 'uplodedwork_table',
            },
        ),
        migrations.CreateModel(
            name='CourseContent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_code', models.CharField(max_length=50)),
                ('chapter_no', models.CharField(max_length=50)),
                ('chapter_name', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('link', models.CharField(max_length=200)),
                ('content', models.FileField(upload_to='coursecontent')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.course')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.faculty')),
            ],
            options={
                'db_table': 'coursecontent_table',
            },
        ),
    ]
