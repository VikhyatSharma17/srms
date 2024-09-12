from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views import generic
from django.forms import BaseModelForm
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy, reverse

from typing import Any

from .forms import UserSelectionForm, StudentSignupForm, TeacherSignupForm
from .models import CustomUser, Student, Result

# views.py file handles all the requests and generates responses against them whether
# it be HTML page or a new file
# CRUD + L: Create, Read, Update, Delete + List

class HomePageView(generic.TemplateView):
    template_name = 'home.html'


class AccountSignupView(generic.FormView):
    template_name = 'userTypeSelection.html'
    form_class = UserSelectionForm

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        userType = request.POST.get('userType', None)

        if userType == 'student':
            print("Inside AccountSignupView class method POST student")
            return redirect('accounts:account-signup-student')
        elif userType == 'teacher':
            print("Inside AccountSignupView class method POST teacher")
            return redirect("accounts:account-signup-teacher")


class StudentSignupView(generic.CreateView):
    template_name = 'studentSignup.html'
    form_class = StudentSignupForm

    def get_success_url(self):
        return reverse('accounts:account-login')

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        print("Inside form_invalid method of StudentSignupView")
        return super().form_invalid(form)


class StudentDetailView(generic.DetailView):
    template_name = 'accounts/studentDetail.html'
    queryset = Student.objects.all()    # this will automatically get the student details based on the primary key
    context_object_name = 'student'


class StudentCourseDetails(generic.ListView):
    template_name = 'accounts/course.html'


class TeacherSignupView(generic.CreateView):
    template_name = 'teacherSignup.html'
    form_class = TeacherSignupForm

    def get_success_url(self):
        return reverse('accounts:account-login')


class AccountProfile(generic.View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        user = CustomUser.objects.get(pk=request.user.id)
        context = {
            'user': user,
        }
        if user.is_student:
            courseDetails = Student.objects.get(user=user).course
            context['course'] = courseDetails

        return render(request, self.template_name, context=context)


class ResultsView(generic.DetailView):
    template_name = 'accounts/results.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        """Gets the results of the user and returns it to the template

        Args:
            request (HttpRequest): HTTP Request containing user data

        Returns:
            HttpResponse: HTTP response after loading the results template
        """
        currentUser = CustomUser.objects.get(pk=request.user.id)
        print(f"returning results for {currentUser.first_name}")

        if currentUser.is_student:
            print("User is a student")
            studentDetails = Student.objects.get(user=currentUser)
            course = studentDetails.course
            result = Result.objects.filter(stuID=studentDetails.id)
            formattedResults = {}

            print(f"Student course is: {course.courseCode}")
            print(f"Student course is: {course.name}")

            print(f"Rendering template: {self.template_name}")
            print(f"Type of course: {course.subject.all()}")
            
            # vs_result.get(subName=vs_stu.course.subject.all()[0].id).marksObtained
            for subject in course.subject.all():
                formattedResults[subject.name] = result.get(subject=subject.id).marksObtained

            print(f"Formatted results: {formattedResults}")
            context = {
                'course': course,
                'results': formattedResults,
            }

            return render(request, self.template_name, *args, context=context, **kwargs)

        # return super().get(request, *args, **kwargs)


class UserLogoutView(LogoutView):
    """Logs out the current user and redirects them to the home page
    """
    next_page = reverse_lazy('accounts:account-login')


# Function based views; not used now

# def homePage(request):
#     """View for the app home page

#     Args:
#         request (request): HTTP Request
#     """

#     return render(request=request, template_name='home.html')

# def accountSignup(request):
#     """View for the student login 

#     Args:
#         request (request): HTTP Request
#     """
#     form = UserSelectionForm()
#     print("Inside accountSignup method")

#     if request.method == 'POST':
#         print("Inside accountSignup method POST")
#         userType = request.POST.get('userType', 'student')
#         if userType == 'student':
#             print("Inside accountSignup method POST student")
#             return studentSignup(request)
#         elif userType == 'teacher':
#             print("Inside accountSignup method POST teacher")
#             return teacherSignup(request)

#     context = {
#         'form': form
#     }
        
#     return render(request=request, template_name='userTypeSelection.html', context=context)

# def studentSignup(request):
#     """View for the student signup

#     Args:
#         request (request): HTTP Request
#     """
#     form = StudentSignupForm()
#     print("Inside studentSignup method")

#     if request.method == 'POST':
#         print("Inside studentSignup method POST")
#         form = StudentSignupForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('/accounts/accountLogin')

#     context = {
#         'form': form
#     }
#     return render(request=request, template_name='studentSignup.html', context=context)

# def teacherSignup(request):
#     """View for the teacher signup

#     Args:
#         request (request): HTTP Request
#     """
#     form = TeacherSignupForm()

#     if request.method == 'POST':
#         form = TeacherSignupForm(request.POST)

#         if form.is_valid():
#             form.save()    #  Teacher.objects.create()
        
#     context = {
#         'form': form
#     }
#     return render(request=request, template_name='userTypeSelection.html', context=context)

# def accountLogin(request):
#     """View for the login page

#     Args:
#         request (request): HTTP Request
#     """
#     form = UserSelectionForm()

#     if request.method == 'POST':
#         userType = request.POST['userType']
#         if userType == 'student':
#             return studentLogin(request)
#         elif userType == 'teacher':
#             return teacherLogin(request)

#     context = {
#         'form': form
#     }
        
#     return render(request=request, template_name='userTypeSelection.html', context=context)


# def studentLogin(request):
#     """View for the student login

#     Args:
#         request (request): HTTP Request
#     """
#     form = StudentLoginForm()
#     # print("Student signup initial")

#     if request.method == 'POST':
#         # print("Student signup POST")
#         form = StudentLoginForm(request.POST)

#         if form.is_valid():
#             form.save()

#     context = {
#         'form': form
#     }
#     return render(request=request, template_name='studentLogin.html', context=context)

# def teacherLogin(request):
#     """View for the teacher login

#     Args:
#         request (request): HTTP Request
#     """
#     form = StudentSignupForm()
#     # print("Student signup initial")

#     if request.method == 'POST':
#         # print("Student signup POST")
#         form = StudentSignupForm(request.POST)

#         if form.is_valid():
#             form.save()

#     context = {
#         'form': form
#     }
#     return render(request=request, template_name='studentSignup.html', context=context)

# def studentDetailView(request, pk):
    # studentDetail = Student.objects.get(id=pk)

    # context = {
    #     'student': studentDetail
    # }
    # return render(request, 'accounts/studentDetail.html', context=context)