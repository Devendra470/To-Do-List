from django.shortcuts import render,redirect
from todo.models import Task
# Create your views here.
def index(request):
    tasks=Task.objects.all()
    if request.method=='POST':
        new_task=request.POST.get('title')
        print(new_task)
        if new_task:
            Task.objects.create(title=new_task)
            return redirect('/')
    return render(request,'todo/index.html',{'tasks':tasks})

def delete_task(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return redirect('/')