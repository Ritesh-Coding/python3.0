from django.urls import path
from . import views

urlpatterns= [
    path('register/',views.RegistrationForm,name='register'),
    path('login/',views.LoginForm,name='login'),    
    path('logout/', views.user_logout, name='logout'),
    path('job-application-form/', views.EmployeeForm, name='employeeForm'),
]