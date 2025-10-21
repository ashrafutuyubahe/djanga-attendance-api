from django import forms
from .models import Student,Attendance

# form for student model
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields =['first_name','classroom', 'gender', 'residence_status']
        widgets ={
            'first_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'enter student name'
            }),
            'classroom':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'enter classroom name'
            }),
            'gender':forms.RadioSelect(attrs={
                'class':'form-check-input'
            }),
                'residence_status':forms.Select(attrs={
                    'class':'form-select'
                }),
        
        }

