from django.shortcuts import render,redirect
from .forms import userRegistrationForm,userLoginForm,BasicDetailsForm,EducationDetailsForm,WorkExperienceForm,LanguagesForm,TechnologiesForm,ReferenceForm,PreferenceTableForm
from django.forms import formset_factory
from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.core.exceptions import ValidationError
from django.contrib import messages,auth
from django.contrib.sessions.models import Session
from django.forms import modelformset_factory
from .login_required import login_required_session
from .models import LanguageKnown,TechnologiesKnown,BasicDetails,SSCHSCDETAILS,WorkExperience,Reference,Preference
LanguageKnownFormSet = modelformset_factory(LanguageKnown, form=LanguagesForm, extra=3)
TechnologyKnownFormSet = modelformset_factory(TechnologiesKnown,form =TechnologiesForm,extra = 4 )

@login_required_session
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
                # print("STEP VALUE *****************************************************************************************",step)
                form=EducationDetailsForm()                
                step=2
                
        elif step==2:            
            form = EducationDetailsForm(request.POST)
            form_data_key = f'step_{step}_data'
            if 'next' in request.POST:
                if form.is_valid():
                    education_details = form.cleaned_data                
                    request.session[form_data_key] = education_details               
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
            if 'next' in request.POST:
                if form.is_valid():
                    work_experience_details = form.cleaned_data
                    work_experience_details['from1']=work_experience_details['from1'].isoformat()
                    work_experience_details['to1']=work_experience_details['to1'].isoformat()
                    request.session[form_data_key]=form.cleaned_data
                    formset = formset_factory(LanguagesForm, formset=LanguageKnownFormSet)
                    data = {
              "form-TOTAL_FORMS": "3",
              "form-INITIAL_FORMS": "0",              
            }
                    form = formset(data)
                    # form = LanguageKnownFormSet()
                    step=4
            elif 'previous' in request.POST:
                form_data_key = f'step_{step-1}_data'
                form_data = request.session.get(form_data_key, {})
                form = EducationDetailsForm(initial=form_data)                             
                step=2
        elif step==4:
            form=LanguageKnownFormSet(request.POST)
            form_data_key = f'step_{step}_data'
            if 'next' in request.POST:
                if form.is_valid():               
                    request.session[form_data_key]=form.cleaned_data
                    
                    formset = formset_factory(TechnologiesForm, formset=TechnologyKnownFormSet)
                    data = {
                    "form-TOTAL_FORMS": "4",
                    "form-INITIAL_FORMS": "0",              
                    }
                    form = formset(data)

                    # form = TechnologyKnownFormSet()


                    step=5
            elif 'previous' in request.POST:
                form_data_key = f'step_{step-1}_data'
                form_data = request.session.get(form_data_key, {})
                form = WorkExperienceForm(initial=form_data)                             
                step=3
        elif step==5:
            form=TechnologyKnownFormSet(request.POST)
            form_data_key = f'step_{step}_data'
            print(form.errors)
            if 'next' in request.POST:
                
                if form.is_valid():                    
                    request.session[form_data_key]=form.cleaned_data
                    form=ReferenceForm()
                    step=6
            elif 'previous' in request.POST:
                formset = formset_factory(LanguagesForm, formset=LanguageKnownFormSet)
                data = {
              "form-TOTAL_FORMS": "3",
              "form-INITIAL_FORMS": "0",              
                }
                form = formset(data)
                step=4
        elif step==6:
            form=ReferenceForm(request.POST)
            form_data_key = f'step_{step}_data'
            if 'next' in request.POST:
                if form.is_valid():
                    request.session[form_data_key]=form.cleaned_data
                    form=PreferenceTableForm()
                    step=7
            elif 'previous' in request.POST:
                formset = formset_factory(TechnologiesForm, formset=TechnologyKnownFormSet)
                data = {
                    "form-TOTAL_FORMS": "4",
                    "form-INITIAL_FORMS": "0",              
                    }
                form = formset(data)
                step=5
        elif step==7:
            form=PreferenceTableForm(request.POST)  
            form_data_key = f'step_{step}_data'         
            if 'previous' in request.POST:
                form_data_key = f'step_{step-1}_data'
                form_data = request.session.get(form_data_key, {})
                
                form=ReferenceForm(initial=form_data)  
                step=6
            elif 'submit' in request.POST:
                if form.is_valid():
                    
                    request.session[form_data_key]=form.cleaned_data
                    basic_details = (request.session.get('step_1_data', {}))
                    education_details = request.session.get('step_2_data', {}) 
                    work_experience_details = request.session.get('step_3_data',{})
                    language_known_details = request.session.get('step_4_data',{})
                    technology_known_details = request.session.get('step_5_data',{})
                    reference_details = request.session.get('step_6_data',{})
                    preference_data = request.session.get('step_7_data',{})
                    print(basic_details)                   
                    print(education_details)
                    print(work_experience_details)
                    print(language_known_details)
                    print(technology_known_details)
                    print(reference_details)
                    print(preference_data)
                    basic_obj = BasicDetails.objects.create(**basic_details, user = request.user)
                    SSCHSCDETAILS.objects.create(**education_details, employee_id= basic_obj)
                    WorkExperience.objects.create(**work_experience_details,employee_id= basic_obj)
                    for item in language_known_details:
                        LanguageKnown.objects.create(**item,employee_id = basic_obj)
                    for item in technology_known_details:
                        TechnologiesKnown.objects.create(**item,employee_id = basic_obj )
                    Reference.objects.create(**reference_details,employee_id = basic_obj)
                    Preference.objects.create(**preference_data,employee_id =basic_obj)
                    # Session.objects.filter(session_key=request.session.session_key).delete()
                    return redirect('success')
    else:
            if step == 1:
                form_data_key = f'step_{step}_data'
                form_data = request.session.get(form_data_key, {})
                form = BasicDetailsForm(initial=form_data)
            # elif step==2:
            #     form_data_key = f'step_{step}_data'
            #     form_data = request.session.get(form_data_key, {})                
            #     form = EducationDetailsForm(initial=form_data)
            # elif step==3:
            #     form_data_key = f'step_{step}_data'
            #     form_data = request.session.get(form_data_key, {}) 
            #     form = WorkExperienceForm(initial=form_data)
            # elif step ==4:
            #     form_data_key = f'step_{step}_data'
            #     form_data = request.session.get(form_data_key, {}) 
            #     form = LanguageKnownFormSet()
                
            # elif step ==5:
            #     form = TechnologyKnownFormSet()
            # elif step ==6:
            #     form = ReferenceForm()
            # elif step==7:
            #      form = PreferenceTableForm()
            
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
    Session.objects.filter(session_key=request.session.session_key).delete()
    return redirect('login')

def home(request):
    return render(request,'home.html')

def success(request):
    return render(request,'success.html')