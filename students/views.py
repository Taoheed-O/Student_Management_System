from django.shortcuts import render
from .models import Student
# Create your views here.

def index(request):
    students = Student.objects.all()
    context = {"students":students}
    return render(request, "students/index.html", context)