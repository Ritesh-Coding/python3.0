from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

from django.core.exceptions import ValidationError
class CustomUser(AbstractUser):    
    phone = models.CharField(max_length=15, null=False,blank=False)

    def __str__(self):
        return self.first_name
    
GENDER_CHOICES=(
    ('male','Male'),
    ('female','Female')
)
RELATIONSHIP_STATUS=(
    ('single','Single'),
    ('married','Married')
)

def validate_phone(value):
    an_integer = value
    a_string = str(an_integer)
    length = len(a_string)

    if length > 10 or length!=10:
        raise ValidationError(
            ('contact No is not valid')
        )
def validate_zip(value):
    an_integer = value
    a_string = str(an_integer)
    length = len(a_string)
    if length > 6 or length!=6:
        raise ValidationError(
            ('zip is not valid')
        )
class BasicDetails(models.Model):
     user = models.ForeignKey(
         settings.AUTH_USER_MODEL,on_delete=models.RESTRICT,default=1
     )
     firstName = models.CharField(max_length=15,null=False,blank=False,
                                  validators=[
                                      RegexValidator(
                 regex=r'^[a-zA-Z\s-]+$',
                 message="Enter a valid First name.",
                 code="invalid_registration",
                     ),
                 ])
     lastName =  models.CharField(max_length=15,null=False,blank=False,
                                  validators=[
                                      RegexValidator(
                 regex=r'^[a-zA-Z\s-]+$',
                 message="Enter a valid Last name.",
                 code="invalid_registration",
                     ),
                 ])
     designation = models.CharField(max_length=15,null=False,blank=False,
                                    validators=[
                                      RegexValidator(
                 regex=r'^[a-zA-Z\s-]+$',
                 message="Enter a valid Last name.",
                 code="invalid_registration",
                     ),
                 ])
     address1 = models.TextField(null=False,blank=False)
     address2 = models.TextField()
     email =  models.EmailField(null=False,blank=False)
     phone =  models.CharField(blank=False,null=False,validators=[validate_phone])
     gender = models.CharField(max_length=6,choices=GENDER_CHOICES,blank=False,null=False)
     cities = models.CharField(max_length=20,null=True,blank=True)
     states = models.CharField(max_length=25,blank=False,null=False)
     zip = models.CharField(blank=False,null=False,validators=[validate_zip])
     relationship = models.CharField(max_length=8,choices=RELATIONSHIP_STATUS,blank=False,null=False)
     date_of_birth= models.DateField(null=False,blank=False,
                                   )
     
     def __str__(self):
         
         return self.firstName,self.lastName
BOARD_NAME = (
    ("GSEB","GSEB"),
    ("CBSC","CBSC"),
    ("Bachelor_Degree","Bachelor_Degree"),
    ("Master_Degree","Master_Degree"),
    ("PHD","PHD"),

)

class SSCHSCDETAILS(models.Model):
    employee_id= models.ForeignKey(BasicDetails,on_delete=models.CASCADE,null=True)
   
    name_of_board = models.CharField(choices=BOARD_NAME,
        max_length=15,
        default = None,        
        )
    
    passing_year = models.CharField(blank=False,null=False, validators=[
                                      RegexValidator(
                 regex=r'^(19\d{2}|20[0-9]{2})$',
                 message="Enter a valid Passing Year.",
                 code="invalid_registration",
                     ),
                 ])
    percentage = models.CharField(blank=False,null=False, validators=[
                                      RegexValidator(
                 regex=r'^100(\.0{1,2})?$|^(\d{1,2}(\.\d{1,2})?)$',
                 message="Enter a valid Percentage.",
                 code="invalid_registration",
                     ),
                 ])
    def __str__(self):
        return self.name_of_board
    
class WorkExperience(models.Model):
    employee_id= models.ForeignKey(BasicDetails,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=15,null=False,blank=False,
                                  validators=[
                                      RegexValidator(
                 regex=r'^[a-zA-Z\s-]+$',
                 message="Enter a valid Company name.",
                 code="invalid_registration",
                     ),
                 ])
    
    designation = models.CharField(max_length=15,null=False,blank=False,
                                  validators=[
                                      RegexValidator(
                 regex=r'^[a-zA-Z\s-]+$',
                 message="Enter a valid Designation name.",
                 code="invalid_registration",
                     ),
                 ])
    from1 = models.DateField(null=False,blank=False,
                               )
    to1 = models.DateField(null=False,blank=False,
                                    )
    
    def __str__(self):
        return self.company_name
    
LANGUAGE_CHOICES = (
    ('hindi','Hindi'),
    ('gujarati','Gujarati'),
    ('english','English')
)
class LanguageKnown(models.Model):
    employee_id= models.ForeignKey(BasicDetails,on_delete=models.CASCADE)
    language_known = models.CharField(max_length=15,choices=LANGUAGE_CHOICES)
    can_read = models.BooleanField(default=False)
    can_write= models.BooleanField(default=False)
    can_speak = models.BooleanField(default=False)

    def __str__(self):
        return self.language_known
TECHNOLOGY_KNOWN=(
    ('php','PHP'),
    ('mysql','MYSQL'),
    ('laravel','LARAVEL'),
    ('oracle','ORACLE')
)
TECHNOLOGY_LIST=(
    ('beginner','Begineer'),
    ('mediator','Mediator'),
    ('expertise','Expertise')
)

class TechnologiesKnown(models.Model):
    employee_id= models.ForeignKey(BasicDetails,on_delete=models.CASCADE)
    technologies_known = models.CharField(max_length=15,choices=TECHNOLOGY_KNOWN)
    level_of_expertise = models.CharField(choices=TECHNOLOGY_LIST,
        max_length=9,                
        )
    def __str__(self):
        return self.technologies_known
    
class Reference(models.Model):
    employee_id= models.ForeignKey(BasicDetails,on_delete=models.CASCADE)
    name = models.CharField(max_length=15,null=False,blank=False,
                                  validators=[
                                      RegexValidator(
                 regex=r'^[a-zA-Z\s-]+$',
                 message="Enter a valid  name.",
                 code="invalid_registration",
                     ),
                 ])
    contact_no =  models.CharField(blank=False,null=False,validators=[validate_phone])
    Relation = models.CharField(max_length=15,null=False,blank=False,
                                  validators=[
                                      RegexValidator(
                 regex=r'^[a-zA-Z\s-]+$',
                 message="Enter a valid  name.",
                 code="invalid_registration",
                     ),
                 ])
    def __str__(self):
        return self.name
DEPARTMENT_CHOICE=(
    ('development','Development'),
    ('department','Department'),
    ('marketing','Marketing')
)
class Preference(models.Model):
    employee_id= models.ForeignKey(BasicDetails,on_delete=models.CASCADE)
    preference_location = models.TextField()
    notice_period = models.CharField(max_length=15,blank=False,null=False)
    expected_ctc = models.CharField(max_length=15,blank=False,null=False)
    current_ctc = models.CharField(max_length=15)
    department = models.CharField(max_length=25,choices=DEPARTMENT_CHOICE,blank=False,null=False)

    def __str__(self):
        return self.department
    

class StateCityMaster(models.Model):
    city_id = models.IntegerField()
    city_name = models.CharField(max_length=120)
    city_state = models.CharField(max_length=120)

    def __str__(self):
        return self.city_name