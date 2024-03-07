from django import forms
from .models import CourseContent


class AddCourseContentForm(forms.ModelForm):
    class Meta:
        model = CourseContent
        fields = "__all__"
        #exclude = {"faculty","course"}
