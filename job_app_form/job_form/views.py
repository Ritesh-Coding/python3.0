from django.shortcuts import get_object_or_404, render,redirect
from .forms import userRegistrationForm,userLoginForm,BasicDetailsForm,EducationDetailsForm,WorkExperienceForm,LanguagesForm,TechnologiesForm,ReferenceForm,PreferenceTableForm
from django.forms import formset_factory
from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.core.exceptions import ValidationError
from django.contrib import messages,auth
from django.contrib.sessions.models import Session
from django.forms import modelformset_factory
from django.http import JsonResponse
from django.core.paginator import Paginator
from .login_required import login_required_session,admin_required_session
from .models import LanguageKnown,TechnologiesKnown,BasicDetails,SSCHSCDETAILS,WorkExperience,Reference,Preference,StateCityMaster
LanguageKnownFormSet = modelformset_factory(LanguageKnown, form=LanguagesForm, extra=3)
TechnologyKnownFormSet = modelformset_factory(TechnologiesKnown,form =TechnologiesForm,extra = 4 )

@login_required_session
@admin_required_session
def updateForm(request,id):
    return redirect('/job-application-form/')

@login_required_session
def cities(request):
      state = request.GET.get('state')
      print("My state",state)
      results = StateCityMaster.objects.filter(city_state = state).values('city_name')
      print(results,"******************************************")
      
      return JsonResponse(list(results),safe=False)    
      

@login_required_session
def dashboard(request):
    user = request.user
    userData = BasicDetails.objects.filter(user_id = user.id)

    
    paginator = Paginator(userData, 10)  # Show 10 contacts per page.
    page_number = request.GET.get("page")
    print(page_number,"hsfdiudsigfisfdjiosdgsfjifddjgfi")
    page_obj3 = paginator.get_page(page_number)

    context = {
                'data' : page_obj3,
                }
    return render(request,'landingPage.html',context)

@login_required_session
@admin_required_session
def adminDashBoard(request):
    user = request.user
    userData = BasicDetails.objects.all().values()

    paginator1 = Paginator(userData, 10)  # Show 10 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator1.get_page(page_number)

    adminData = BasicDetails.objects.filter(user_id = user.id)

    paginator2 = Paginator(adminData, 10)  # Show 10 contacts per page.
    page_number2 = request.GET.get("p")
    page_obj2 = paginator2.get_page(page_number2)
   
    context = {             
            "allUser": page_obj,
            "adminData" : page_obj2,
    }
    return render(request,'landingPage.html',context)

@login_required_session
@admin_required_session
def confirmDelete(request,id):
    context={
        "id":id
    }
    return render(request,"confirmDelete.html",context)


@login_required_session
def EmployeeForm(request,step=1):
    step = int(request.POST.get('step', 1))    
    states = StateCityMaster.objects.distinct('city_state')
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
                    educaitonData = []
                    for x in range(len(dict(request.POST)['name_of_board'])):
                        educaitonData.append({
                            'name_of_board' : dict(request.POST)['name_of_board'][x],
                            'passing_year':dict(request.POST)['passing_year'][x],
                            'percentage':dict(request.POST)['percentage'][x]
                        })
                    # education_details = form.cleaned_data
                    # print("********************************************************************",educaitonData)
                    # print("*********************************************************************",education_details)                                    
                    request.session[form_data_key] = educaitonData               
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
                    # work_experience_details = form.cleaned_data                  
                    experienceData = []
                    for x in range(len(dict(request.POST)['company_name'])):
                        experienceData.append({
                            'company_name' : dict(request.POST)['company_name'][x],
                            'designation':dict(request.POST)['designation'][x],
                            'from1':dict(request.POST)['from1'][x],                            
                            'to1':dict(request.POST)['to1'][x],                       
                        })
                    # print(experienceData,"************")
                    # work_experience_details['from1']=work_experience_details['from1'].isoformat()
                    # work_experience_details['to1']=work_experience_details['to1'].isoformat()
                    # request.session[form_data_key]=work_experience_details

                    request.session[form_data_key]=experienceData

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
                                
                form = EducationDetailsForm()                             
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
                    print(form.cleaned_data)
                    referenceData = []
                    for x in range(len(dict(request.POST)['name'])):
                        referenceData.append({
                            'name' : dict(request.POST)['name'][x],
                            'contact_no':dict(request.POST)['contact_no'][x],
                            'Relation':dict(request.POST)['Relation'][x],                                              
                        })
                    request.session[form_data_key]=referenceData
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
                    for item in education_details:
                        SSCHSCDETAILS.objects.create(**item, employee_id= basic_obj)

                    for item in work_experience_details:
                        WorkExperience.objects.create(**item,employee_id= basic_obj)
                    for item in language_known_details:
                        if len(item)!=0:
                            LanguageKnown.objects.create(**item,employee_id = basic_obj)
                    for item in technology_known_details:
                        if len(item)!=0:
                            TechnologiesKnown.objects.create(**item,employee_id = basic_obj )
                    for item in reference_details:
                        Reference.objects.create(**item,employee_id = basic_obj)
                    Preference.objects.create(**preference_data,employee_id =basic_obj)
                    try:
                        del request.session['step_1_data']
                        del request.session['form_2_data']
                        del request.session['form_3_data']
                        del request.session['form_4_data']
                        del request.session['form_5_data']
                        del request.session['form_6_data']
                        del request.session['form_7_data']
                    except KeyError:
                        pass
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
            "stateDropdownResults" : states,
      
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
                    if user.is_superuser:
                        return redirect('adminDashboard')
                     
                    else:
                       return redirect('dashboard')
                  
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

@login_required_session
def success(request):
    return render(request,'success.html')

@login_required_session
def deleteForm(request,id):
    basicDetails = BasicDetails.objects.get(id = id)
    basicDetails.delete()
    return redirect('adminDashboard')

@login_required_session
def userData(request,id):
   
    BasicDetailsData = BasicDetails.objects.filter(id = id).values()
    educationDetailsData = SSCHSCDETAILS.objects.filter(employee_id_id = id).values()
    workExperienceData = WorkExperience.objects.filter(employee_id_id = id).values()
    languagesKnownData =  LanguageKnown.objects.filter(employee_id_id = id).values()
    technologiesKnownData = TechnologiesKnown.objects.filter(employee_id_id = id).values()
    referenceData = Reference.objects.filter(employee_id_id = id).values()
    preferenceData = Preference.objects.filter(employee_id_id = id).values()

    # print(BasicDetailsData)
    # print(educationDetailsData)
    # print(workExperienceData)
    # print(languagesKnownData)
    # print(technologiesKnownData)
    # print(referenceData)
    # print(preferenceData)
    context =  {
        "userId":id,
        "basicDetails":BasicDetailsData,
        "educationDetails":educationDetailsData,
        "workExperience":workExperienceData,
        "languagesKnown":languagesKnownData,
        "technologiesKnown":technologiesKnownData,
        "reference":referenceData,
        "preference":preferenceData,
       
    }
    return render(request,'userData.html',context)




@login_required_session
@admin_required_session
def updateEmployeeForm(request,id,step=1):
    step = int(request.POST.get('step', 1))    
    states = StateCityMaster.objects.distinct('city_state')
    if request.method == "POST":
        
        if step==1:   
            form_data_key = f'step_{step}_data'      
            form = BasicDetailsForm(request.POST)
            print("my post form ",request.POST)
            if form.is_valid():
                basic_details = form.cleaned_data               
                basic_details['date_of_birth'] = basic_details['date_of_birth'].isoformat()
                request.session[form_data_key] = basic_details
                # print("STEP VALUE *****************************************************************************************",step)
                education_formset = modelformset_factory(model=SSCHSCDETAILS,form = EducationDetailsForm,extra=0)   
                form= education_formset(queryset=SSCHSCDETAILS.objects.filter(employee_id_id = id))
                step=2                
        elif step==2:            
            # form = EducationDetailsForm(request.POST)
            education_formset = modelformset_factory(model=SSCHSCDETAILS,form = EducationDetailsForm,extra=0)   
            form = education_formset(request.POST)
            form_data_key = f'step_{step}_data'
            if 'next' in request.POST:
                if form.is_valid():
                    educaitonData = []
                    # print(dict(request.POST)['form-0-name_of_board'],"shgbfduiashfiusdgsdufgjusfdhgbbfds")
                    for x in range(len(dict(request.POST)['form-0-name_of_board'])):
                        educaitonData.append({
                            'name_of_board' : dict(request.POST)['form-'+str(x)+'-name_of_board'][x],
                            'passing_year':dict(request.POST)['form-'+str(x)+'-passing_year'][x],
                            'percentage':dict(request.POST)['form-'+str(x)+'-percentage'][x]
                        })
                    education_details = form.cleaned_data
                    form_data_key=form.cleaned_data
                    print("********************************************************************",educaitonData)
                    print("*********************************************************************",education_details)                        
                    print(form.data, "FORM data ===")
                    print("\n \n")
                    print("recived data", request.POST)
                
                    print(form.errors,'siudfiiodfgioiofdgo')                                 
                    workExperienceFormset = modelformset_factory(model=WorkExperience,form = WorkExperienceForm,extra=0)   
                    form = workExperienceFormset(queryset=WorkExperience.objects.filter(employee_id_id = id))
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
                    # work_experience_details = form.cleaned_data                  
                    experienceData = []
                    for x in range(len(dict(request.POST)['company_name'])):
                        experienceData.append({
                            'company_name' : dict(request.POST)['company_name'][x],
                            'designation':dict(request.POST)['designation'][x],
                            'from1':dict(request.POST)['from1'][x],                            
                            'to1':dict(request.POST)['to1'][x],                       
                        })                   

                    request.session[form_data_key]=experienceData
                else:
                    languageKnownSet = modelformset_factory(model=LanguageKnown,form = LanguagesForm,extra=0)   
                    form = languageKnownSet(queryset=LanguageKnown.objects.filter(employee_id_id = id))
                    step=4
            elif 'previous' in request.POST:
                form_data_key = f'step_{step-1}_data'
                form_data = request.session.get(form_data_key, {})
                
                form = EducationDetailsForm(initial=form_data)                             
                step=2
        elif step==4:
            form=LanguageKnownFormSet()
            form_data_key = f'step_{step}_data'
            if 'next' in request.POST:
                if form.is_valid():               
                    request.session[form_data_key]=form.cleaned_data 
                    
                else:                  
                    techchnologyFormset = modelformset_factory(model=TechnologiesKnown,form = TechnologiesForm,extra=0)   
                    form = techchnologyFormset(queryset=TechnologiesKnown.objects.filter(employee_id_id = id))
                    step=5
            elif 'previous' in request.POST:
                form_data_key = f'step_{step-1}_data'
                form_data = request.session.get(form_data_key, {})
                form = WorkExperienceForm(initial=form_data)                             
                step=3
        elif step==5:
            form=TechnologyKnownFormSet()
            form_data_key = f'step_{step}_data'
            print(form.errors)
            if 'next' in request.POST:
                
                if form.is_valid():                    
                    request.session[form_data_key]=form.cleaned_data
                else:
                    referenceFormset = modelformset_factory(model=Reference,form = ReferenceForm,extra=0)   
                    form = referenceFormset(queryset=Reference.objects.filter(employee_id_id = id))
                    step=6
            elif 'previous' in request.POST:
                formset = formset_factory(LanguagesForm, formset=LanguageKnownFormSet)
                data = {
              "form-TOTAL_FORMS": "3",
              "form-INITIAL_FORMS": "0",              
                }
                form = formset(data)
                # form = LanguageKnownFormSet()
                step=4
        elif step==6:
            form=ReferenceForm(request.POST)
            form_data_key = f'step_{step}_data'
            if 'next' in request.POST:
                if form.is_valid():
                    print(form.cleaned_data)
                    referenceData = []
                    for x in range(len(dict(request.POST)['name'])):
                        referenceData.append({
                            'name' : dict(request.POST)['name'][x],
                            'contact_no':dict(request.POST)['contact_no'][x],
                            'Relation':dict(request.POST)['Relation'][x],                                              
                        })
                    request.session[form_data_key]=referenceData
                else:
                    form_data = get_object_or_404(Preference,employee_id_id=id)               
                    form = PreferenceTableForm(instance=form_data)
                    
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
                    for item in education_details:
                        SSCHSCDETAILS.objects.create(**item, employee_id= basic_obj)

                    for item in work_experience_details:
                        WorkExperience.objects.create(**item,employee_id= basic_obj)
                    for item in language_known_details:
                        if len(item)!=0:
                            LanguageKnown.objects.create(**item,employee_id = basic_obj)
                    for item in technology_known_details:
                        if len(item)!=0:
                            TechnologiesKnown.objects.create(**item,employee_id = basic_obj )
                    for item in reference_details:
                        Reference.objects.create(**item,employee_id = basic_obj)
                    Preference.objects.create(**preference_data,employee_id =basic_obj)
                    try:
                        del request.session['step_1_data']
                        del request.session['form_2_data']
                        del request.session['form_3_data']
                        del request.session['form_4_data']
                        del request.session['form_5_data']
                        del request.session['form_6_data']
                        del request.session['form_7_data']
                    except KeyError:
                        pass
                    return redirect('success')
    else:
            if step == 1:
                form_data = get_object_or_404(BasicDetails,id=id)               
                form = BasicDetailsForm(instance=form_data)
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
            "stateDropdownResults" : states,
            "updateForm" : True
    }
    
    return render(request,'job_form.html',context)