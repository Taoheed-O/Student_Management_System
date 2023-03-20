from django.urls import path
from . import views


app_name = "students"


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>',views.view_student, name='view_student'),
    path("add/", views.add, name="add"),
    path('<int:pk>/update', views.update, name='update'),
]

