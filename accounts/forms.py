from django import forms
from .models import Student, Teacher


class UserSelectionForm(forms.Form):
    userTypes = (
        ('student', 'Student'),
        ('teacher', 'Teacher')
    )
    userType = forms.ChoiceField(choices=userTypes)


class StudentSignupForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            'course'
        )

class TeacherSignupForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = (
            'first_name',
            'subject'            
        )


class StudentLoginForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'email',
            'password',
        )