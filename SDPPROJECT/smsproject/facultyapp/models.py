from django.db import models
from adminapp.models import Faculty, Course

class CourseContent(models.Model):
    id = models.AutoField(primary_key=True)
    course_code = models.CharField(max_length=50,blank=False)
    faculty = models.ForeignKey(Faculty,blank=False,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,blank=False,on_delete=models.CASCADE)
    chapter_no = models.CharField(max_length=50, blank=False)
    chapter_name = models.CharField(max_length=100, blank=False)
    topic = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=300,blank=False)
    link = models.CharField(max_length=200,blank=False)
    content = models.FileField(blank=False,upload_to="coursecontent")

    class Meta:
        db_table = "coursecontent_table"

class UploadWork(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.CharField(max_length=15,blank=False)
    topic_name = models.CharField(max_length=30,blank=False)
    uploded_file = models.FileField(blank=False,upload_to="uploadwork/")

    class Meta:
        db_table = "uplodedwork_table"