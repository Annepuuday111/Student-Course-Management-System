from django.urls import path
from . import views

urlpatterns = [

    path("checkfacultylogin",views.checkfacultylogin,name="checkfacultylogin"),
    path("facultyhome",views.facultyhome,name="facultyhome"),
    path("myfcourses",views.facultycourses,name="facultycourses"),
    path("facultychangepwd", views.facultychangepwd, name="facultychangepwd"),
    path("facultyupdatepwd", views.facultyupdatepwd, name="facultyupdatepwd"),
    path('facultyviewcontent/', views.facultyviewcontent, name='facultyviewcontent'),
    path('facultyviewquiz/', views.facultyviewquiz, name='facultyviewquiz'),
    path('facultyaddcontent/', views.facultyaddcontent, name='facultyaddcontent'),
    path('facultyaddquiz/', views.facultyaddquiz, name='facultyaddquiz'),
    path('contentupdation/<int:id>', views.contentupdation, name='contentupdation'),
    path('quizupdation/<int:id>', views.quizupdation, name='quizupdation'),
    path("updatecontent",views.updatecontent,name="updatecontent"),
    path("updatequiz",views.updatequiz,name="updatequiz"),
    path("viewwork/", views.viewwork, name="viewwork"),
    path("facultyviewresult/", views.facultyviewresult, name="facultyviewresult"),
    ]