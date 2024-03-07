from django.urls import path
from . import views

urlpatterns = [

    path("checkstudentlogin",views.checkstudentlogin,name="checkstudentlogin"),
    path("studenthome",views.studenthome,name="studenthome"),
    path("studentchangepwd", views.studentchangepwd, name="studentchangepwd"),
    path("studentupdatepwd", views.studentupdatepwd, name="studentupdatepwd"),
    path("studentcourses",views.studentcourses,name="studentcourses"),
    path("displayscourses",views.displaystudentcourses,name="displaystudentcourses"),
    path("studentcontent",views.studentcontent,name="studentcontent"),
    path("displaycourselist",views.displaycourselist,name="displaycourselist"),
    path("studentcoursecontent/<str:ccode>",views.studentcoursecontent,name="scoursecontent"),
    path('studentcoursecontent/uploadwork/', views.uploadwork, name='uploadwork'),

    ]