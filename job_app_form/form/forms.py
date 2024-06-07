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
                                'placeholder':'Username'
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
            'phone',
            'gender',
            'states',
            'zip',
            'relationship',
            'date_of_birth'
        ]
        widgets={
        'date_of_birth' : forms.SelectDateWidget()
        }

class EducationDetailsForm(forms.ModelForm):
    class Meta:
        model = SSCHSCDETAILS
        fields = [
            'name_of_board',
            'passing_year',
            'percentage'
        ]
        

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = [
            'company_name',
            'designation',
            '_from',
            '_to'
        ]
        widgets={
        '_from' : forms.SelectDateWidget(),
         '_to' : forms.SelectDateWidget()
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
class TechnologiesForm(forms.ModelForm):
    class Meta:
        model = TechnologiesKnown
        fields = [
            'technologies_known',
            'level_of_expertise'
        ]
        widgets = {
            'level_of_expertise' : forms.RadioSelect(),
            }
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