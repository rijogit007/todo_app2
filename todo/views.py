from django.shortcuts import render,redirect,get_object_or_404
from todo.models import Task 
# Create your views here.


def index(request):
    data=Task.objects.all().order_by('created_at')
    return render (request,'home.html',{'task':data})



def  add_task(request):
    if request.method=="POST":
        title=request.POST.get('title')
        
        if title:
            Task.objects.create(title=title)
        return redirect('/')
    
    
def delete_task(request,id):
    task=get_object_or_404(Task,id=id)
    task.delete()
    return redirect('/')

    
def edit_task(request,id):
    task=get_object_or_404(Task,id=id)
    
    if request.method=="POST":
        title=request.POST.get('title')
        
        if title:
            Task.title=title
            
            title.save()
            
        return redirect('/')
    
    return render(request,'edit_task.html',{'task':task})    
            

