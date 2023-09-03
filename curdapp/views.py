from django.shortcuts import render,HttpResponse,redirect
from .models import empolyee

# Create your views here.
def home(request):
    return HttpResponse("hellp aro")


def myfun(request):
    if(request.method=="POST"):
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mob']
        data=empolyee.objects.create(name=name,mobile=mobile,email=email)
        data.save() 
        return redirect('dashboard')  
    else:
        return render(request,'index.html')
    

def dashboard(request):
    data=empolyee.objects.all()
    return render(request,'dashboard.html',{'data':data})


def delete(request,key):
    data=empolyee.objects.get(id=key)
    data.delete()
    return redirect('dashboard')


def edit(request,key):
    data=empolyee.objects.get(id=key)
    return render(request,'edit.html',{'data':data})
def doedit(request,key):
    if(request.method=="POST"):
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mob')
        data=empolyee.objects.get(id=key)
        data.name=name
        data.email=email
        data.mobile=mobile
        data.save()
        return redirect('dashboard')
    else:
        return render(request,'index.html')
    

    



    
