from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from typing import Any

from .models import CustomUser, Student, Teacher, Course, Subject


class UserSelectionForm(forms.Form):
    userTypes = (
        ('student', 'Student'),
        ('teacher', 'Teacher')
    )
    userType = forms.ChoiceField(choices=userTypes)


class StudentSignupForm(UserCreationForm):
    course = forms.ModelChoiceField(
        queryset = Course.objects.all()
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'email'
        )

    @transaction.atomic
    def save(self, commit: bool = True) -> Any:
        print("Saving the student user")

        # Creating a new user with the form details
        user = super().save(commit=False)
        user.username = f"{user.last_name.lower()}{user.first_name[:2].capitalize()}S"
        user.is_student = True
        user.save()

        # Creating a new student table entry with the user details
        student = Student.objects.create(user=user)
        student.course = self.cleaned_data['course']
        print(f"Cleaned data for student: {self.cleaned_data}")
        student.save()

        return student    
        

class TeacherSignupForm(UserCreationForm):
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all()
    )

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'email',          
        )

    @transaction.atomic
    def save(self, commit: bool = ...) -> Any:
        user = super().save(commit=False)

        # Adding teacher specific fields to the user and creating it
        user.is_teacher = True
        user.username = f"{user.last_name.lower()}{user.first_name[:2].capitalize()}T"
        user.save()

        # Creating a teacher model entry with the created user
        teacher = Teacher.objects.create(
            user=user,
            subject=self.cleaned_data['subject']
        )

        return teacher




# class StudentLoginForm(forms.ModelForm):
#     class Meta():
#         model = CustomUser
#         fields = (
#             'email',
#             'password',
#         )