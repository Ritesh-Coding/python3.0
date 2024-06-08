from django.shortcuts import render,redirect
from .forms import userRegistrationForm,userLoginForm,BasicDetailsForm,EducationDetailsForm,WorkExperienceForm,LanguagesForm,TechnologiesForm,ReferenceForm,PreferenceTableForm

from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.core.exceptions import ValidationError
from django.contrib import messages,auth
from django.contrib.sessions.models import Session


def EmployeeForm(request):
    saveBasicDetails = BasicDetailsForm()
    saveEducationDetails = EducationDetailsForm()
    saveWorkExperience = WorkExperienceForm()
    saveLanguagesKnown= LanguagesForm()
    saveTechnologiesForm = TechnologiesForm()
    saveReferenceForm = ReferenceForm()
    savePreferenceForm = PreferenceTableForm()

    if request.method == "POST":
        
        saveBasicDetails = BasicDetailsForm(request.POST)
        saveEducationDetails = EducationDetailsForm(request.POST)
        saveWorkExperience = WorkExperienceForm(request.POST)
        saveLanguagesKnown = LanguagesForm(request.POST)
        saveTechnologiesForm = TechnologiesForm(request.POST)
        saveReferenceForm = ReferenceForm(request.POST)
        savePreferenceForm = PreferenceTableForm(request.POST)
        if saveBasicDetails.is_valid():
            saveBasicDetails.save()
            saveEducationDetails.save()
            saveWorkExperience.save()
            saveLanguagesKnown.save()
            saveTechnologiesForm.save()
            saveReferenceForm.save()
            savePreferenceForm.save()
            return redirect('register')
    context = {
            "basicDetailsForm" :saveBasicDetails,
            "educationDetailsForm" :saveEducationDetails,
            "workExperienceForm" : saveWorkExperience,
            "languageForm":saveLanguagesKnown,
            "technologyForm":saveTechnologiesForm,
            "referenceForm":saveReferenceForm,
            "preferenceForm":savePreferenceForm           
    }
    
    return render(request,'job_form.html',context)
    

def RegistrationForm(request):
    saveUserForm = userRegistrationForm()
    
    if request.method == "POST":
        saveUserForm = userRegistrationForm(request.POST)
        
        if saveUserForm.is_valid():            
            saveUserForm.save()
            
            return redirect('login')
    context = {
        "modalform":saveUserForm
    }
    return render(request,'register.html',context)

def LoginForm(request):
    form= userLoginForm()
    if request.method == "POST":
        form = userLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user) 
                    #  set user-specific data in the session
                    request.session['username'] = username
                    request.session.save() 
                    
                    return redirect('employeeForm')
            else:                
                messages.error(request, 'Invalid credentials')
                return redirect('login')   
    
    return render(request, 'login.html', {'loginform': form})
    

def user_logout(request):
    logout(request)
    # Session.objects.filter(session_key=request.session.session_key).delete()
    return redirect('login')


# def jobApplication(request):
#     # form = employeeDetailsForm()
#     return  render(request,'job_form.html')

