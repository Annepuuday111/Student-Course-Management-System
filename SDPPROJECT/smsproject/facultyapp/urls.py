from django.urls import path
from . import views

urlpatterns = [

    path("checkfacultylogin",views.checkfacultylogin,name="checkfacultylogin"),
    path("facultyhome",views.facultyhome,name="facultyhome"),
    path("myfcourses",views.facultycourses,name="facultycourses"),
    path("facultychangepwd", views.facultychangepwd, name="facultychangepwd"),
    path("facultyupdatepwd", views.facultyupdatepwd, name="facultyupdatepwd"),
    path('facultyviewcontent/', views.facultyviewcontent, name='facultyviewcontent'),
    path('facultyaddcontent/', views.facultyaddcontent, name='facultyaddcontent'),
    path('contentupdation/<int:id>', views.contentupdation, name='contentupdation'),
    path("updatecontent",views.updatecontent,name="updatecontent"),
    path("viewwork/", views.viewwork, name="viewwork"),
    ]