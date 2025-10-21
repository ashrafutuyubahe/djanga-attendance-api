from datetime import timezone
from django.shortcuts import redirect, render
from attendance.models import Attendance, Student
from django.http import JsonResponse
from  django.utils import timezone
from attendance.forms import StudentForm



# Create your views here.


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentForm()   
            #pop out the message using alert in html
            message = 'Student added successfully!'
            
            return render(request, 'attendance/add_student.html', {
                'form': form,
                'message': message
            })
            # StudentForm()            
            # return redirect('mark_attendance')
    else:
        form = StudentForm()    
        return render(request, 'attendance/add_student.html', {'form': form})
    
def mark_attendance(request):
    students = Student.objects.all()
    date = timezone.now().date()
    if request.method == 'POST':
        for student in students:
            is_present = request.POST.get(f'present_{student.id}') == 'on'
            Attendance.objects.update_or_create(
                student=student,
                date=date,
                defaults={'present': is_present}
            )
        return redirect('attendance_list')
    return render(request, 'attendance/mark_attendance.html', {'students': students, 'date': date})

def attendance_list(request):
    records = Attendance.objects.select_related('student').order_by('-date')
    # records = Attendance.objects.select_related('student').all()
    return render(request, 'attendance/attendance_list.html', {'attendance_records': records})

