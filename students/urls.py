from django.urls import path
from . import views


app_name = "students"


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>',views.view_student, name='view_student'),
    path("add/", views.add, name="add"),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]

