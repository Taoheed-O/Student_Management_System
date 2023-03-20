from django.shortcuts import render
from .models import Student
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import StudentForm 
# Create your views here.

def index(request):
    students = Student.objects.all()
    context = {"students":students}
    return render(request, "students/index.html", context)


def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse("index"))


def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
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
            return render(request, "students/add.html", {
                "form": StudentForm(),
                "success": True
                })
    else:
        form = StudentForm()
        return render(request, "students/add.html", {
            'form': StudentForm()
        })
        
 
def update(request, id):
    if request.method == 'POST':
        student =  Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/update.html', {
                'form': form,
                'success': True
            })
    else:
        student = Student.objects.get(pk=id)
        form =  StudentForm(instance=student)
        return render(request, 'students/update.html', {
            'form':form,
        })
