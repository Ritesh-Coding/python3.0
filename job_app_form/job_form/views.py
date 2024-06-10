from django.shortcuts import render,redirect
from .forms import userRegistrationForm,userLoginForm,BasicDetailsForm,EducationDetailsForm,WorkExperienceForm,LanguagesForm,TechnologiesForm,ReferenceForm,PreferenceTableForm

from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.core.exceptions import ValidationError
from django.contrib import messages,auth
from django.contrib.sessions.models import Session
from django.forms import modelformset_factory
from .models import LanguageKnown
LanguageKnownFormSet = modelformset_factory(LanguageKnown, form=LanguagesForm, extra=3)
def EmployeeForm(request):
    # saveBasicDetails = BasicDetailsForm()
    # saveEducationDetails = EducationDetailsForm()
    # saveWorkExperience = WorkExperienceForm()
    saveLanguagesKnown= LanguageKnownFormSet()
    # saveTechnologiesForm = TechnologiesForm()
    # saveReferenceForm = ReferenceForm()
    # savePreferenceForm = PreferenceTableForm()
    print("i am GET REQUEST")
    if request.method == "POST":
        print("i am not valid")
        # saveBasicDetails = BasicDetailsForm(request.POST)
        # saveEducationDetails = EducationDetailsForm(request.POST)
        # saveWorkExperience = WorkExperienceForm(request.POST)
        saveLanguagesKnown = LanguageKnownFormSet(request.POST)
        # saveTechnologiesForm = TechnologiesForm(request.POST)
        # saveReferenceForm = ReferenceForm(request.POST)
        # savePreferenceForm = PreferenceTableForm(request.POST)
        if saveLanguagesKnown.is_valid():
            # saveBasicDetails.save()
            # saveEducationDetails.save()
            # saveWorkExperience.save()
            # saveLanguagesKnown.save()
            # saveTechnologiesForm.save()
            # saveReferenceForm.save()
            # savePreferenceForm.save()
            print(request.POST)
            return redirect('login')
        else:
            saveBasic = saveLanguagesKnown.errors
            print(saveBasic)
            
    context = {
            # "basicDetailsForm" :saveBasicDetails,
            # "educationDetailsForm" :saveEducationDetails,
            # "workExperienceForm" : saveWorkExperience,
            "languageForm":LanguageKnownFormSet(queryset=LanguageKnown.objects.none()),
            # "technologyForm":saveTechnologiesForm,
            # "referenceForm":saveReferenceForm,
            # "preferenceForm":savePreferenceForm           
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


    return  render(request,'job_form.html')


# from django.shortcuts import render, redirect
# from .forms import Step1Form, Step2Form, Step3Form
# from .models import Step1, Step2, Step3

# def multi_step_form(request):
#     step = int(request.POST.get('step', 1))

#     if request.method == 'POST':
#         if step == 1:
#             form = Step1Form(request.POST)
#             if form.is_valid():
#                 request.session['step1_data'] = form.cleaned_data
#                 return redirect('multi_step_form')
#         elif step == 2:
#             if 'previous' in request.POST:
#                 return redirect('multi_step_form', {'step': 1})
#             form = Step2Form(request.POST)
#             if form.is_valid():
#                 request.session['step2_data'] = form.cleaned_data
#                 return redirect('multi_step_form', {'step': 3})
#         elif step == 3:
#             if 'previous' in request.POST:
#                 return redirect('multi_step_form', {'step': 2})
#             form = Step3Form(request.POST)
#             if form.is_valid():
#                 request.session['step3_data'] = form.cleaned_data

#                 # Save all data to the database
#                 step1_data = request.session.get('step1_data')
#                 step2_data = request.session.get('step2_data')
#                 step3_data = form.cleaned_data

#                 Step1.objects.create(**step1_data)
#                 Step2.objects.create(**step2_data)
#                 Step3.objects.create(**step3_data)

#                 # Clear session data
#                 del request.session['step1_data']
#                 del request.session['step2_data']
#                 del request.session['step3_data']

#                 return redirect('success')

#     else:
#         if step == 1:
#             initial_data = request.session.get('step1_data', {})
#             form = Step1Form(initial=initial_data)
#         elif step == 2:
#             initial_data = request.session.get('step2_data', {})
#             form = Step2Form(initial=initial_data)
#         elif step == 3:
#             initial_data = request.session.get('step3_data', {})
#             form = Step3Form(initial=initial_data)

#     return render(request, 'multi_step_form.html', {'form': form, 'step': step})

# def success(request):
#     return render(request, 'success.html')


