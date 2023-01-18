"""accounts URL configuration

The 'urlpatterns' routes the URL routes to the local app views.
"""

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'accounts'

# urlpatterns = [
#     # path('', views.homePage, name='account-home'),
#     path('accountLogin/', views.accountLogin, name='account-login'),
#     path('accountSignup/', views.accountSignup, name='account-signup'),
# ]

urlpatterns = [
    path('', views.HomePageView.as_view(), name='account-home'),
    path('login/', LoginView.as_view(), name='account-login'),
    path('login/', LogoutView.as_view(), name='account-logout'),
    path('signup/', views.AccountSignupView.as_view(), name='account-signup'),
    path('studentAccountSignup/', views.StudentSignupView.as_view(), name='account-signup-student'),
    path('teacherAccountSignup/', views.TeacherSignupView.as_view(), name='account-signup-teacher'),
    path('profile/', views.AccountProfile.as_view(), name='account-profile'),
    path(r'<int:pk>/', views.AccountProfile.as_view(), name='account-profile'),
    # path('<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
]