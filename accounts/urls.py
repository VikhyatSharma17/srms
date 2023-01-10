"""accounts URL configuration

The 'urlpatterns' routes the URL routes to the local app views.
"""

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.homePage, name='account-home'),
    path('accountLogin/', views.accountLogin, name='account-login'),
    path('accountSignup/', views.accountSignup, name='account-signup'),
]