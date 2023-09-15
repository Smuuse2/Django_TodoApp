from django.shortcuts import render,redirect
from home.models import Task
# Create your views here.
def home(request):
    if request.method == "POST":
        
        title = request.POST['title']
        desc = request.POST['desc']

        ins = Task(taskTitle = title, taskDisc = desc)

        ins.save()
        print(title,desc)
        

    return render (request,'index.html')

def task(request):
    
    allTesk = Task.objects.all()
    context = {'task': allTesk}
    # for item in allTesk:
    #  print(item.taskDisc)
    return render (request,'task.html',context)

def delete(request,id):
 
   mem = Task.objects.get(id=id)
   mem.delete()
   return redirect('task')