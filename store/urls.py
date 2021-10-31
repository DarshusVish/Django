from django.contrib import admin
from django.urls import path
from .views import index,signup,login,signup_user,logout

urlpatterns = [
    path('', index,name='homepage'),
    path('signup', signup),
    path('NewSignUP', signup_user),
    path('login', login, name='login'),
    path('logout', logout),
]