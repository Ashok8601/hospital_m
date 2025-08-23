from django.contrib import admin
from .models import User
from .models import Patient 
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'father_name', 'Email', 'age', 'mo_no', 'village', 'mother')

admin.site.register(User, UserAdmin)
admin.site.register(Patient)