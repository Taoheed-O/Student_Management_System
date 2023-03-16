from django.shortcuts import render
from .models import Student
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    students = Student.objects.all()
    context = {"students":students}
    return render(request, "students/index.html", context)


def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse("index"))