from django.urls import path
from . import views

urlpatterns = [
    path('records/', views.attendance_list, name='attendance_list'),
    path('  /', views.add_student, name='student_form'),
    path('mark/', views.mark_attendance, name='mark_attendance'),
]
