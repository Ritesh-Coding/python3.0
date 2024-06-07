from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import CustomUser,BasicDetails,SSCHSCDETAILS,WorkExperience,LanguageKnown,TechnologiesKnown,Preference,Reference


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
         'phone'
        )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(BasicDetails)
admin.site.register(SSCHSCDETAILS)
admin.site.register(WorkExperience)
admin.site.register(LanguageKnown)
admin.site.register(TechnologiesKnown)
admin.site.register(Reference)
admin.site.register(Preference)
