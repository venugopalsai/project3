from django.shortcuts import render,redirect 
from django.http import HttpResponse
from studentadd.models import Stuadd

# Create your views here.
def home(request):
    if request.method=="POST":
        name=request.POST['sname']
        gender=request.POST['gender']
        dob=request.POST['dob']
        email=request.POST['email']
        phno=request.POST['phno']
        user=Stuadd.objects.create(sname=name,gender=gender,dob=dob,email=email,phone=phno)
        user.save()
        return HttpResponse(f"Form Submitted{name,gender,dob,email,phno}")
    return render(request,'add.html')

def display(request):
    data=Stuadd.objects.all()
    return render(request,'display.html',{"details":data})

def delete(request,sid):
    data=Stuadd.objects.get(id=sid)
    data.delete()
    return redirect(display)

def update(request,sid):
    if request.method=="POST":
        name=request.POST['sname']
        gender=request.POST['gender']
        dob=request.POST['dob']
        email=request.POST['email']        
        phno=request.POST['phno']
        user=Stuadd.objects.filter(id=sid).update(sname=name,gender=gender,dob=dob,email=email,phone=phno)
        return redirect('display')
    data=Stuadd.objects.get(id=sid)
    return render(request,'update.html',{'data':data})