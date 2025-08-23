from django.shortcuts import render, redirect,get_object_or_404
from .forms import Userform
from .forms import Patientform
from .models import User
from django.db.models import Q
def user(request):
    if request.method=='POST':
        form=Userform(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form =Userform()     
        
    return render(request,'home.html', {'form':form})
def main(request):
    user=User.objects.all()
    query=request.GET.get('query')
    result=[]
    if query:
        result=User.objects.filter (Q(name__icontains=query)|
        Q(mo_no__icontains=query))
    return render(request,'main.html', {'result': result})
def dashboard(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method=='POST':
        form=Patientform(request.POST)
        if form.is_valid():
            patient=form.save(commit=False)
            patient.user=user
            patient.save()
            return redirect('dashboard',pk=user.pk)    
    else:
           
       form=Patientform()  
       # सिर्फ वही user fetch होगा
    return render(request, 'dashboard.html', {'user': user,'form':form,'patient':user.patient.all()})

