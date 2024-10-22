from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'^$', home, name='home'),
    path('login', loginPage, name='login'),
    path('register', registerPage, name='register'),
    path('me', me, name='me'),
    path('logout', doLogout, name='logout')
]
