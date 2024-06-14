from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser,BasicDetails,SSCHSCDETAILS,WorkExperience,LanguageKnown,TechnologiesKnown,Reference,Preference
import re
class userRegistrationForm(UserCreationForm):
  
    class Meta:
        model=CustomUser
        fields = ['first_name','last_name','username','email','phone','password1','password2']

        widgets = {
            'first_name' :  forms.TextInput(attrs={
                                   'class':'form-control',
                                   'placeholder':'First Name'
                               }),
            'last_name' : forms.TextInput(attrs={
                                   'class':'form-control',
                                   'placeholder':'Last Name'
                               }),
            'username' :  forms.TextInput(attrs={
                                   'class':'form-control',
                                   'placeholder':'Username'
                               }),
            'email' : forms.EmailInput(attrs={
                                   'class':'form-control',
                                   'placeholder':'Email'
                               }),
            'phone' : forms.NumberInput(attrs={
                                   'class':'form-control',
                                   'placeholder':'Phone'
                               }),
            'password1' : forms.PasswordInput(attrs={
                                   'class':'form-control',
                                   'placeholder':'Password'
                               }),
            'password2' : forms.PasswordInput(attrs={
                                   'class':'form-control',
                                   'placeholder':'Password2'
                               }),
           
        }
    def clean(self):
        super(userRegistrationForm, self).clean()
        firstName = self.cleaned_data.get('first_name')
        lastName = self.cleaned_data.get('last_name')
        phone = self.cleaned_data.get('phone')
        email = self.cleaned_data.get('email')
        
        
        if firstName == "" or firstName == None:           
           self._errors['firstName'] = self.error_class([
                'FirstName is Required']) 
        if lastName == "" or lastName == None:           
           self._errors['lastName'] = self.error_class([
                'LastName is Required'])
        if email == "" or email == None:           
           self._errors['email'] = self.error_class([
                'Email is Required'])
        if len(phone) < 10:           
            self._errors['phone'] = self.error_class([
                'Minimum 10 characters required'])           
        
        return self.cleaned_data
    
class userLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
                                   'class':'form-control',
                                   'placeholder':'Username'
                               }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                                'class':'form-control',
                                'placeholder':'Password'
                            }))
    


class BasicDetailsForm(forms.ModelForm):
    class Meta:
        model = BasicDetails
        fields = [
            'firstName',
            'lastName',
            'designation',
            'address1',
            'address2',
            'email',
            'cities',
            'phone',
            'gender',
            'states',
            'zip',
            'relationship',
            'date_of_birth'
        ]
        widgets={
        'date_of_birth' : forms.SelectDateWidget(),
        'gender': forms.RadioSelect()
        }
        def __init__(self, *args, **kwargs):
        # Pop 'step' parameter from kwargs, defaulting to None if not present
            step = kwargs.pop('step', None)
            
            # Call the parent class's __init__ method
            super().__init__(*args, **kwargs)
            
            # Check if 'step' parameter is provided
            if step is not None:
                # Perform any initialization based on the step if needed
                pass

class EducationDetailsForm(forms.ModelForm):
    class Meta:
        model = SSCHSCDETAILS
        fields = [
            'name_of_board',
            'passing_year',
            'percentage'
        ]
    
SSCHSCDetailsFormset = forms.formset_factory(EducationDetailsForm, extra=1)

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = [
            'company_name',
            'designation',
            'from1',
            'to1'
        ]
        widgets={
        'from1' : forms.DateInput(attrs={"type": "date"}),
         'to1' : forms.DateInput(attrs={"type": "date"})
        }
class LanguagesForm(forms.ModelForm):
    class Meta:
        model = LanguageKnown
        fields = [
            'language_known',
            'can_read',
            'can_write',
            'can_speak'
        ]
    def clean(self):
        cleaned_data = super().clean()
        language_known = cleaned_data.get('language_known')
        can_read = cleaned_data.get('can_read')
        can_write = cleaned_data.get('can_write')
        can_speak = cleaned_data.get('can_speak')
        
        if language_known and not (can_read or can_write or can_speak):
            raise forms.ValidationError(
                'If you select a language, you must select at least one of can_read, can_write, or can_speak.'
            )
        
        if (can_read or can_write or can_speak) and not language_known:
            raise forms.ValidationError(
                'If you select can_read, can_write, or can_speak, you must also select language_known.'
            )

        return cleaned_data
class TechnologiesForm(forms.ModelForm):
    class Meta:
        model = TechnologiesKnown
        fields = [
            'technologies_known',
            'level_of_expertise'
        ]
        widgets = {
            'level_of_expertise' : forms.RadioSelect(attrs={'class': 'form-check-inline'}),
            }
    def clean(self):
        cleaned_data = super().clean()
        technologies_known = cleaned_data.get('technologies_known')
        level_of_expertise = cleaned_data.get('level_of_expertise')
        
        if technologies_known and not level_of_expertise:
            raise forms.ValidationError(
                'If You select the technology then you select atleast one level of expertise'
            )
        if level_of_expertise and not technologies_known:
            raise forms.ValidationError(
                'Select the Technology First'
            )
class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = [
            'name',
            'contact_no',
            'Relation'
        ]
class PreferenceTableForm(forms.ModelForm):
    class Meta:
        model = Preference
        fields = [
            'preference_location',
            'notice_period',
            'expected_ctc',
            'current_ctc',
            'department'
        ]