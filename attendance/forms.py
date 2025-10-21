from django import forms
from .models import Student,Attendance

# form for student model
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields =['first_name','classroom']
        widgets ={
            'name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'enter student name'
            }),
            'classroom':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'enter classroom name'
            }),
        }

