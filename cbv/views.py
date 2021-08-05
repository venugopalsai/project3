from django.shortcuts import render
from django.http import HttpResponse
from cbv.models import Stuadd
from cbv.forms import sturegister
from django.views.generic import View,TemplateView,FormView,ListView
# Create your views here.

def funcdisplay(request):
    p1=Stuadd.objects.all()
    return render(request, "display.html", {'details':p1})
    
class clsdisplay(ListView):
    model = Stuadd
    
    
    
    
















def funcview(request):
    p1=Stuadd.objects.all()
    return render(request,"display.html",{'details':p1})

class clsview(View):        
    def get(self,request):
        p1=Stuadd.objects.all()
        return render(request,"display.html",{'details':p1})
    
    
    
    
    
    
    
    
    
    
    
    
    
    

'''
def func(request):
    p1=Stuadd.objects.create(sname="gopal",gender='Male',dob='2021-10-06',email='gopalsai@gmail.com',phone=9098874535)
    p1.save()
    return HttpResponse("value is created")

class clsview(View):        
    def get(self,request):
        p1=Stuadd.objects.create(sname="rani1",gender='Female',dob='2021-10-08',email='rani@gmail.com1',phone=9966885544)
        p1.save()
        return HttpResponse("value is created")
        
def funcdisplay(request):
    p1=Stuadd.objects.all()
    return render(request,"display.html",{'details':p1})

class clsdisplay(View):        
    def get(self,request):
        p1=Stuadd.objects.all()
        return render(request,"display.html",{'details':p1})
        
def funcdisplay(request):
    if request.method=='POST':
        form=sturegister(request.POST)
        if form.is_valid():
            p1=Stuadd.objects.create(sname=form.cleaned_data['sname'],gender=form.cleaned_data['gender'],dob=form.cleaned_data['dob'],email=form.cleaned_data['email'],phone=form.cleaned_data['phone'])
            p1.save()
    form=sturegister
    return render(request,"home.html",{'form':form})

class clsdisplay(View):     
    def post(self,request):
        print("haii")
        if request.method=='POST':
            form=sturegister(request.POST)
            if form.is_valid():
                p1=Stuadd.objects.create(sname=form.cleaned_data['sname'],gender=form.cleaned_data['gender'],dob=form.cleaned_data['dob'],email=form.cleaned_data['email'],phone=form.cleaned_data['phone'])
                p1.save()
                return HttpResponse("valus is created")
                   
    def get(self,request):
        print("get")
        form=sturegister
        return render(request,"home.html",{'form':form})
        
def funcdisplay(request):
    if request.method=='POST':
        form=sturegister(request.POST)
        if form.is_valid():
            print("haii")
            p1=Stuadd.objects.create(sname=form.cleaned_data['sname'],gender=form.cleaned_data['gender'],dob=form.cleaned_data['dob'],email=form.cleaned_data['email'],phone=form.cleaned_data['phone'])
            p1.save()
            return HttpResponse("values is created")
    form=sturegister
    return render(request,"home.html",{'form':form})

class clsdisplay(TemplateView):
    template_name='home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = sturegister
        context["form"] = form
        return context
    def post(self,request):
        print("haii")
        if request.method=='POST':
            form=sturegister(request.POST)
            if form.is_valid():
                p1=Stuadd.objects.create(sname=form.cleaned_data['sname'],gender=form.cleaned_data['gender'],dob=form.cleaned_data['dob'],email=form.cleaned_data['email'],phone=form.cleaned_data['phone'])
                p1.save()
                return HttpResponse("valus is created")
                
def funcdisplay(request):
    if request.method=='POST':
        form=sturegister(request.POST)
        if form.is_valid():
            print("haii")
            p1=Stuadd.objects.create(sname=form.cleaned_data['sname'],gender=form.cleaned_data['gender'],dob=form.cleaned_data['dob'],email=form.cleaned_data['email'],phone=form.cleaned_data['phone'])
            p1.save()
            return HttpResponse("values is created")
    form=sturegister
    return render(request,"home.html",{'form':form})

class clsdisplay(FormView):
    form_class = sturegister
    template_name='home.html'
    
    def form_valid(self, form):
        p1=Stuadd.objects.create(sname=form.cleaned_data['sname'],gender=form.cleaned_data['gender'],dob=form.cleaned_data['dob'],email=form.cleaned_data['email'],phone=form.cleaned_data['phone'])
        p1.save()
        return HttpResponse("values is created")



def funcdisplay(request):
    form=sturegister
    return render(request,'home.html',{'form':form,'name':'venu','age':25})

class clsdisplay(FormView):
    template_name = 'home.html'
    form_class = sturegister
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        form=sturegister
        context['name']='venu'
        context['age']=25
        return context
    
class clsdisplay(TemplateView):
    template_name = 'home.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        form=sturegister
        context['form']=form
        context['name']='venu'
        context['age']=25
        return context  
        
        
def funcdisplay(request):
    p1=Stuadd.objects.all()
    return render(request, "display.html", {'details':p1})
    
class clsdisplay(ListView):
    model = Stuadd
    template_name = 'display.html'
    context_object_name ='details'
    queryset = Stuadd.objects.filter(gender='Male')  
'''