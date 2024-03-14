from django import forms
from .models import CourseContent, CourseQuiz


class AddCourseContentForm(forms.ModelForm):
    class Meta:
        model = CourseContent
        fields = "__all__"
        #exclude = {"faculty","course"}

class AddQuizForm(forms.ModelForm):
    class Meta:
        model = CourseQuiz
        fields = '__all__'
