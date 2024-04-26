from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from adminapp.models import Student, Course
from facultyapp.models import CourseContent, UploadWork, CourseQuiz
from .models import QuizResult
from django.conf import settings
from django.core.mail import send_mail

def studenthome(request):
    sid = request.session["sid"]

    student=Student.objects.get(studentid=sid)
    print(student)

    return render(request,"studenthome.html",{"sid":sid,"student":student})

def checkstudentlogin(request):
    sid = request.POST["sid"]
    pwd = request.POST["pwd"]
    flag=Student.objects.filter(Q(studentid=sid)&Q(password=pwd))
    print(flag)
    if flag:
        print("login sucess")
        request.session["sid"] = sid

        student = Student.objects.get(studentid=sid)
        print(student)

        return render(request,"studenthome.html", {"sid":sid, "student":student})
    else:
        msg = "Login Failed"
        return render(request, "studentlogin.html", {"message":msg})
        #return HttpResponse("Login Failed")

def studentchangepwd(request):
    sid = request.session["sid"]
    return render(request, "studentchangepwd.html", {"sid": sid})

def studentupdatepwd(request):
    sid = request.session["sid"]
    opwd=request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(sid,opwd,npwd)

    flag=Student.objects.filter(Q(studentid=sid)&Q(password=opwd))

    if flag:
        print("Old Pwd is Correct")
        Student.objects.filter(studentid=sid).update(password=npwd)
        print("Updated Successfully..!")
        msg = "Password Updated Successfully"
    else:
        print("Old Pwd is Invalid")
        msg = "Old Password is Incorrect"

    return render(request, "studentchangepwd.html", {"sid": sid, "message": msg})

def studentcourses(request):
    sid = request.session["sid"]
    return render(request,"studentcourses.html", {"sid": sid})

def studentcoursecontent(request,ccode):
    sid = request.session["sid"]
    print(sid)
    content = CourseContent.objects.filter(Q(course_code=ccode))
    return render(request,"studentcoursecontent.html", {"sid": sid, "coursecontent": content})

def studentquiz(request,ccode):
    sid = request.session["sid"]
    print(sid)
    content = CourseQuiz.objects.filter(Q(course_code=ccode)).distinct('quiz_title')
    return render(request,"studentquiz.html", {"sid": sid, "CourseQuiz": content})

def displaystudentcourses(request):
    sid = request.session["sid"]
    ay = request.POST["ay"]
    sem = request.POST["sem"]

    courses = Course.objects.filter(Q(academicyear=ay)&Q(semester=sem))

    return render(request, "displaystudentcourses.html",{"courses":courses,"sid":sid})

def studentcontent(request):
    sid = request.session["sid"]
    return render(request,"studentcontent.html",{"sid":sid})

def displaycourselist(request):
    sid = request.session["sid"]
    ay = request.POST["ay"]
    sem = request.POST["sem"]

    courses = Course.objects.filter(Q(academicyear=ay)&Q(semester=sem))

    return render(request, "displaycourselist.html",{"courses":courses,"sid":sid})


def uploadwork(request):
    sid = request.session["sid"]
    if request.method == 'POST':
        sid = request.POST.get('sid')
        topic = request.POST.get('topic')
        uploaded_file = request.FILES.get('file')

        if sid and topic and uploaded_file:
            upload = UploadWork.objects.create(student_id=sid, topic_name=topic, uploded_file=uploaded_file.name)
            message = "Work uploaded successfully..!"

            # subject = 'Work Uploaded Successfully'
            # message = ('Dear Student, your Work has been Uploaded Successfully.'
            #            )
            # from_email = 'annepuuday111@gmail.com'
            # recipient_list = [Student.email]
            # send_mail(subject, message, from_email, recipient_list)

        else:
            message = "Please fill in all the fields."

        return render(request, 'uploadwork.html', {"sid": sid, "message": message, "upload": upload})
    else:
        sid = request.session.get("sid")
        return render(request, 'uploadwork.html', {"sid": sid})

def attemptquiz(request, quiz_title):
    sid = request.session["sid"]
    quiz = CourseQuiz.objects.filter(quiz_title=quiz_title)
    questions = CourseQuiz.objects.filter(quiz_title=quiz_title)
    return render(request, 'attemptquiz.html', {'questions': questions, 'sid': sid, 'quiz': quiz})

def submitquiz(request):
    sid = request.session["sid"]

    if QuizResult.objects.filter(sid=sid).exists():
        return HttpResponse("Quiz is already taken.")

    if request.method == "POST":
        score = 0
        total_questions = 0

        for key, value in request.POST.items():
            if key.startswith('answer') and value:
                total_questions += 1
                question_number = int(key.replace('answer', ''))
                question = CourseQuiz.objects.get(pk=request.POST[f'question{question_number}'])
                if value == question.answer:
                    score += 1

        percentage = (score / total_questions) * 100 if total_questions != 0 else 0

        if percentage >= 70:
            grade = 'A'
        elif percentage >= 60:
            grade = 'B'
        elif percentage >= 50:
            grade = 'C'
        elif percentage >= 40:
            grade = 'D'
        else:
            grade = 'F',

        print(grade,sid,percentage)
        quizresult = QuizResult(sid=sid, quiz_title=question.quiz_title, quiz_score=score)
        QuizResult.save(quizresult)
        return render(request, 'quizresult.html', {'percentage': percentage, 'grade': grade, "sid": sid,"quiz_title":question.quiz_title})

    else:
        error_message = "Failed to Save The Quiz"
        return render(request, 'error.html', {'error_message': error_message, "sid": sid})