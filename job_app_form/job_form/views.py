from django.shortcuts import render,redirect
from .forms import userRegistrationForm,userLoginForm,BasicDetailsForm,EducationDetailsForm,WorkExperienceForm,LanguagesForm,TechnologiesForm,ReferenceForm,PreferenceTableForm

from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.core.exceptions import ValidationError
from django.contrib import messages,auth
from django.contrib.sessions.models import Session
from django.forms import modelformset_factory
from .models import LanguageKnown,TechnologiesKnown
LanguageKnownFormSet = modelformset_factory(LanguageKnown, form=LanguagesForm, extra=3)
TechnologyKnownFormSet = modelformset_factory(TechnologiesKnown,form =TechnologiesForm,extra = 4 )
def EmployeeForm(request,step=1):
    step = int(request.POST.get('step', 1))
    
    print("i am GET REQUEST")
    if request.method == "POST":
        
        if step==1:   
            form_data_key = f'step_{step}_data'      
            form = BasicDetailsForm(request.POST)
            if form.is_valid():
                basic_details = form.cleaned_data               
                basic_details['date_of_birth'] = basic_details['date_of_birth'].isoformat()
                request.session[form_data_key] = basic_details
                print("STEP VALUE *****************************************************************************************",step)
                form=EducationDetailsForm()                
                step=2
                
        elif step==2:            
            form = EducationDetailsForm(request.POST)
            form_data_key = f'step_{step}_data'
            if form.is_valid():
                request.session[form_data_key] = form.cleaned_data                
                form=WorkExperienceForm()
                step=3
            elif 'previous' in request.POST:
                form_data_key = f'step_{step-1}_data'
                form_data = request.session.get(form_data_key, {})
                form = BasicDetailsForm(initial=form_data)                             
                step=1
                
        elif step==3:
            form=WorkExperienceForm(request.POST)
            form_data_key = f'step_{step}_data'
            if form.is_valid():
                request.session[form_data_key]=form.cleaned_data
                form=LanguageKnownFormSet()
                step=4
            elif 'previous' in request.POST:
                form_data_key = f'step_{step-1}_data'
                form_data = request.session.get(form_data_key, {})
                form = EducationDetailsForm(initial=form_data)                             
                step=2
        elif step==4:
            form=LanguageKnownFormSet(request.POST)
            form_data_key = f'step_{step}_data'
            if form.is_valid():               
                request.session[form_data_key]=form.cleaned_data
                form=LanguageKnownFormSet()
                step=5
            elif 'previous' in request.POST:
                form_data_key = f'step_{step-1}_data'
                form_data = request.session.get(form_data_key, {})
                form = WorkExperienceForm(initial=form_data)                             
                step=2
        elif step==5:
            form=TechnologyKnownFormSet(request.POST)
            if form.is_valid():
                request.session['technology_known_details']=form.cleaned_data
                return redirect('job_form', step=6)
            elif 'previous' in request.POST:
                return redirect('job_form', step=4)
        elif step==6:
            form=ReferenceForm(request.POST)
            if form.is_valid():
                request.session['reference_details']=form.cleaned_data
                return redirect('job_form', step=7)
            elif 'previous' in request.POST:
                return redirect('job_form', step=5)
        elif step==7:
            form=PreferenceTableForm(request.POST)
           
            if 'previous' in request.POST:
                return redirect('job_form', step=6)  
            elif form.is_valid():
                basic_details = request.session.get('basic_details', {})
                education_details = request.session.get('education_details', {}) 
                work_experience_details = request.session.get('work_experience_details',{})
                language_known_details = request.session.get('language_known_details',{})
                technology_known_details = request.session.get('technology_known_details',{})
                reference_details = request.session.get('reference_details',{})
                print(basic_details)
                print(education_details)
                print(work_experience_details)
                print(language_known_details)
                print(technology_known_details)
                print(reference_details)
                return redirect('login')
    else:
            if step == 1:
                form_data_key = f'step_{step}_data'
                form_data = request.session.get(form_data_key, {})
                form = BasicDetailsForm(initial=form_data)
            elif step==2:
                form_data_key = f'step_{step}_data'
                form_data = request.session.get(form_data_key, {})                
                form = EducationDetailsForm()
            elif step==3:
                form = WorkExperienceForm()
            elif step ==4:
                form = LanguageKnownFormSet()
            elif step ==5:
                form = TechnologyKnownFormSet()
            elif step ==6:
                form = ReferenceForm()
            elif step==7:
                 form = PreferenceTableForm()
            
    context = {
           'form': form,           
           'step': step,         
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


