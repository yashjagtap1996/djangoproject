from django.shortcuts import render,redirect
from .form import StudentForm
from .models import Student

# Create your views here.

def Navbar(request):
    template_name="navbar.html"
    return render(request,template_name)

def Data(request):
    data=Student.objects.all()
    template_name="Data.html"
    context={'data':data}
    return render(request,template_name,context)

def Form(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("data")
    form=StudentForm()
    template_name="Form.html"
    context={'form':form}
    return render(request,template_name,context)

def Delete(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    return redirect("data")

def Update(request,id):
    data=Student.objects.get(id=id)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("data")
    form=StudentForm(instance=data)
    template_name="update.html"
    context={'form':form}
    return render(request,template_name,context)
