from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import UserSelectionForm, StudentSignupForm, TeacherSignupForm, StudentLoginForm

# views.py file handles all the requests and generates responses against them whether
# it be HTML page or a new file

def homePage(request):
    """View for the app home page

    Args:
        request (request): HTTP Request
    """

    return render(request=request, template_name='home.html')

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
