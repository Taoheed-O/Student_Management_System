from django.shortcuts import render
from .models import Student
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import Student_form 
# Create your views here.

def index(request):
    students = Student.objects.all()
    context = {"students":students}
    return render(request, "students/index.html", context)


def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse("index"))


def add(request):
    if request.method == "post":
        form = Student_form(request.post)
        if form.is_valid():
            new_student_id = form.cleaned_data["student_id"]
            new_firstname = form.cleaned_data["firstname"]
            new_lastname = form.cleaned_data["lastname"]
            new_email = form.cleaned_data["email"]
            new_faculty = form.cleaned_data["faculty"]
            new_departmant = form.cleaned_data["department"]
            new_cgpa = form.cleaned_data["cgpa"]

            new_student = Student(
                student_id = new_student_id,
                firstname = new_firstname,
                lastname = new_lastname,
                email = new_email,
                faculty = new_faculty,
                department = new_departmant,
                cgpa = new_cgpa,
            )
            new_student.save()
            context = {"form": Student_form(), "success": True}
            return render("students/add.html", context)
        else:
            form = Student_form()
            context = {"form": Student_form()}
            return render("students/add.html", context)
        
