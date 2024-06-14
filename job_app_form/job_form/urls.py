from django.urls import path
from . import views

urlpatterns= [
    path('',views.home,name='home'),
    path('register/',views.RegistrationForm,name='register'),
    path('login/',views.LoginForm,name='login'),    
    path('logout/', views.user_logout, name='logout'),
    path('job-application-form/', views.EmployeeForm, name='employeeForm'),
    path('success/', views.success, name='success'),
    path('userData/<int:id>/',views.userData,name='userData'),
    path('updateForm/<int:id>',views.updateForm,name='updateForm'),
    path('deleteForm/<int:id>/',views.deleteForm,name='deleteForm'),
    path('confirmDelete/<int:id>/',views.confirmDelete,name='confirmDelete'),
    path('admin-dashboard/',views.adminDashBoard,name='adminDashboard'),
    path('dashboard',views.dashboard,name="dashboard"),
    path('api/cities',views.cities,name='cities'),
    path('update-job-application-form/<int:id>/',views.updateEmployeeForm,name='updateEmployeeForm')

]