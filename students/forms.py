from django import forms
from .models import Student


class Student(forms.ModelForm):
    class Meta:
        model = Student
        field = ["student_id", "firstname", "lastname", "email", "faculty", "department", "cgpa"]
        labels = {
            "student_id": "student id",
            "firstname": "first name",
            "lastname": "last name",
            "email": "email",
            "faculty": "faculty",
            "departmanet": "department",
            "cgpa":"cgpa"
        }

        widgets = {
            "student_id": forms.NumberInput(attrs="class=form-control"),
            "firstname": forms.TextInput(attrs="class=form-control"),
            "lastname": forms.TextInput(attrs="class=form-control"),
            "email": forms.EmailInput(attrs="class=form-control"),
            "faculty": forms.TextInput(attrs="class=form-control"), 
            "department": forms.TextInput(attrs="class=form-control"),
            "cgpa": forms.NumberInput(attrs="class=form-control")
        }

