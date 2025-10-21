from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    classroom = models.CharField(max_length=50)
    class Meta:
        db_table = "students"

    def __str__(self):
        return f"{self.first_name} - {self.classroom}"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    # status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])
    present = models.BooleanField(default=False)

    class Meta:
        db_table = "attendance"

    def __str__(self):
        # show the student's first_name for readability
        return f"{self.student.first_name} - {self.date} - {'present' if self.present else 'absent'}"