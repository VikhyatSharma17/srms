from django.shortcuts import render, redirect, reverse
from django.http import HttpRequest, HttpResponse
from django.views import generic
from django.forms import BaseModelForm

from typing import Any

from .forms import UserSelectionForm, StudentSignupForm, TeacherSignupForm
from .models import Student

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

class TeacherSignupView(generic.CreateView):
    template_name = 'teacherSignup.html'
    form_class = TeacherSignupForm

    def get_success_url(self):
        return reverse('accounts:account-login')
        

# class AccountLoginView():
#     # TODO: Complete the login view 
#     pass


def homePage(request):
    """View for the app home page

    Args:
        request (request): HTTP Request
    """

    return render(request=request, template_name='home.html')

def accountSignup(request):
    """View for the student login 

    Args:
        request (request): HTTP Request
    """
    form = UserSelectionForm()
    print("Inside accountSignup method")

    if request.method == 'POST':
        print("Inside accountSignup method POST")
        userType = request.POST.get('userType', 'student')
        if userType == 'student':
            print("Inside accountSignup method POST student")
            return studentSignup(request)
        elif userType == 'teacher':
            print("Inside accountSignup method POST teacher")
            return teacherSignup(request)

    context = {
        'form': form
    }
        
    return render(request=request, template_name='userTypeSelection.html', context=context)

def studentSignup(request):
    """View for the student signup

    Args:
        request (request): HTTP Request
    """
    form = StudentSignupForm()
    print("Inside studentSignup method")

    if request.method == 'POST':
        print("Inside studentSignup method POST")
        form = StudentSignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/accounts/accountLogin')

    context = {
        'form': form
    }
    return render(request=request, template_name='studentSignup.html', context=context)

def teacherSignup(request):
    """View for the teacher signup

    Args:
        request (request): HTTP Request
    """
    form = TeacherSignupForm()

    if request.method == 'POST':
        form = TeacherSignupForm(request.POST)

        if form.is_valid():
            form.save()    #  Teacher.objects.create()
        
    context = {
        'form': form
    }
    return render(request=request, template_name='userTypeSelection.html', context=context)

def accountLogin(request):
    """View for the login page

    Args:
        request (request): HTTP Request
    """
    form = UserSelectionForm()

    if request.method == 'POST':
        userType = request.POST['userType']
        if userType == 'student':
            return studentLogin(request)
        elif userType == 'teacher':
            return teacherLogin(request)

    context = {
        'form': form
    }
        
    return render(request=request, template_name='userTypeSelection.html', context=context)


def studentLogin(request):
    """View for the student login

    Args:
        request (request): HTTP Request
    """
    form = StudentLoginForm()
    # print("Student signup initial")

    if request.method == 'POST':
        # print("Student signup POST")
        form = StudentLoginForm(request.POST)

        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request=request, template_name='studentLogin.html', context=context)

def teacherLogin(request):
    """View for the teacher login

    Args:
        request (request): HTTP Request
    """
    form = StudentSignupForm()
    # print("Student signup initial")

    if request.method == 'POST':
        # print("Student signup POST")
        form = StudentSignupForm(request.POST)

        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request=request, template_name='studentSignup.html', context=context)

def studentDetailView(request, pk):
    studentDetail = Student.objects.get(id=pk)

    context = {
        'student': studentDetail
    }
    return render(request, 'accounts/studentDetail.html', context=context)