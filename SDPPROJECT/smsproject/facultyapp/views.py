from django.db.models import Q
from adminapp.models import Faculty, FacultyCourseMapping,Course
from .forms import AddCourseContentForm, AddQuizForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import CourseContent, UploadWork, CourseQuiz
from django.http import HttpResponse
from studentapp.models import QuizResult


def checkfacultylogin(request):
    fid = request.POST["fid"]
    pwd = request.POST["pwd"]
    flag=Faculty.objects.filter(Q(facultyid=fid)&Q(password=pwd))
    print(flag)
    if flag:
        print("login sucess")
        request.session["fid"] = fid
        faculty = Faculty.objects.get(facultyid=fid)
        return render(request,"facultyhome.html", {"fid":fid,"faculty":faculty})
    else:
        msg = "Login Failed"
        return render(request, "facultylogin.html", {"message":msg})
        #return HttpResponse("Login Failed")


def facultyhome(request):
    fid = request.session["fid"]
    print("Faculty ID:", fid)
    faculty = Faculty.objects.get(facultyid=fid)
    print(faculty)

    return render(request, "facultyhome.html",{"fid": fid,"faculty":faculty})


def facultycourses(request):
    fid = request.session["fid"]
    print("Faculty ID:"+fid)

    mappingcourses =FacultyCourseMapping.objects.all()
    fmcourses=[]
    for course in mappingcourses:
        #print(course.faculty.facultyid)
        if(course.faculty.facultyid ==int(fid)):
            fmcourses.append(course)

    print(fmcourses)
    count = len(fmcourses)

    return render(request, "facultycourses.html",{"fid": fid,"fmcourses":fmcourses,"count":count})

def facultychangepwd(request):
    fid = request.session["fid"]
    return render(request, "facultychangepwd.html", {"fid": fid})

def facultyupdatepwd(request):
    fid = request.session["fid"]
    opwd=request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(fid,opwd,npwd)

    flag=Faculty.objects.filter(Q(facultyid=fid)&Q(password=opwd))

    if flag:
        print("Old Pwd is Correct")
        Faculty.objects.filter(facultyid=fid).update(password=npwd)
        print("Updated Successfully..!")
        msg = "Password Updated Successfully"
    else:
        print("Old Pwd is Invalid")
        msg = "Old Password is Incorrect"

    return render(request, "facultychangepwd.html", {"fid":fid,"message":msg})

def facultyaddcontent(request):
    fid = request.session["fid"]
    if request.method == "POST":
        form = AddCourseContentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.data)
            form.save()
            return redirect('facultyaddcontent')
        msg = "Content Added Successfully"
    else:
        form = AddCourseContentForm()
        msg = "Content Added Failed"
    return render(request, 'facultyaddcontent.html', {"fid": fid,"form":form,"msg":msg})

def facultyaddquiz(request):
    fid = request.session.get("fid")
    if request.method == 'POST':
        form = AddQuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultyaddquiz')
        # msg = "Quiz Added Successfully"
    else:
        form = AddQuizForm()
        # msg = "Quiz Added Failed"
    return render(request, 'facultyaddquiz.html', {'form': form,"fid": fid})

def facultyviewcontent(request):
    fid = request.session["fid"]
    print(fid)
    content = CourseContent.objects.filter(Q(faculty__facultyid=fid))
    return render(request, 'facultyviewcontent.html',{"fid": fid, "coursecontent": content})

def facultyviewquiz(request):
    fid = request.session["fid"]
    print(fid)
    content = CourseQuiz.objects.all()
    return render(request, 'facultyviewquiz.html',{"fid": fid, "CourseQuiz": content})

def contentupdation(request, id):
    fid= request.session["fid"]
    content = get_object_or_404(CourseContent, pk=id)
    if request.method == "POST":
        form = AddCourseContentForm(request.POST, instance=content)
        if form.is_valid():
            form.save()
            return HttpResponse("Content Updated Successfully")
        else:
            return HttpResponse("Updation Failed")
    else:
        form = AddCourseContentForm(instance=content)
    return render(request, "contentupdation.html", {"form": form, "fid":fid,"content":content})

def quizupdation(request, id):
    fid= request.session["fid"]
    content = get_object_or_404(CourseQuiz, pk=id)
    if request.method == "POST":
        form = AddQuizForm(request.POST, instance=content)
        if form.is_valid():
            form.save()
            return HttpResponse("Content Updated Successfully")
        else:
            return HttpResponse("Updation Failed")
    else:
        form = AddQuizForm(instance=content)
    return render(request, "quizupdation.html", {"form": form, "fid":fid,"content":content})


def updatecontent(request):
    fid = request.session.get("fid")
    content = CourseContent.objects.all()
    count = Faculty.objects.count()
    return render(request, "updatecontent.html", {"content": content, "count": count, "fid": fid})

def updatequiz(request):
    fid = request.session.get("fid")
    content = CourseQuiz.objects.all()
    count = Faculty.objects.count()
    return render(request, "updatecontent.html", {"content": content, "count": count, "fid": fid})

def viewwork(request):
    fid = request.session.get("fid")
    course_contents = UploadWork.objects.all()
    context = {'course_contents': course_contents, 'fid': fid}
    return render(request, 'viewwork.html', context)

def facultyviewresult(request):
    fid = request.session.get("fid")
    quiz_results = QuizResult.objects.all()
    context = {'quiz_results': quiz_results, 'fid': fid}
    return render(request, 'facultyviewresult.html', context)

