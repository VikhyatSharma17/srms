from django.db import models
from django.contrib.auth.models import AbstractUser


class Subject(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.name}"


class Course(models.Model):
    name = models.CharField(max_length=35)
    courseCode = models.CharField(max_length=8)

    subject = models.ManyToManyField(Subject)
 
    def __str__(self):
        return f"{self.courseCode} - {self.name}"
        

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


# class Student(CustomUser):
#     class Meta:
#         verbose_name = 'Student'
#         verbose_name_plural = 'Students'
#     # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')    # delete the student field when the user is deleted 

#     course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

#     def __str__(self):
#         return f"{self.first_name}"

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')    # delete the student field when the user is deleted 
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


# class Teacher(CustomUser):
#     class Meta:
#         verbose_name = 'Teacher'
#         verbose_name_plural = 'Teachers'
#     # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')    # delete the teacher field when the user is deleted

#     subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher_profile')    # delete the teacher field when the user is deleted
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    
class Result(models.Model):
    stuID = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)

    marksObtained = models.IntegerField()

    def __str__(self):
        return f"{self.stuID} - {self.subject}"