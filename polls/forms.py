from django import forms
from .models import User, Patient 
class Userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','father_name','Email','age','mo_no','village','mother']
class Patientform(forms.ModelForm):
        
    class Meta:
        model=Patient 
        fields=['admit_date','deseas','notes','medicine','bed_no','gardian']  