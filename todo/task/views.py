from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks=Task.objects.all()

    form=Taskform()

    if request.method=='POST':
        form=Taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={'tasks':tasks,'form':form}
    return render(request,'task/index.html',context)

def update(request,pk):
    task = Task.objects.get(id=pk)

    form=Taskform(instance=task)

    if request.method=='POST':
        form=Taskform(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}

    return render(request,'task/update.html',context)

def delete(request,pk):
    item=Task.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('/')
    return render(request,'task/delete.html',{'item':item})
