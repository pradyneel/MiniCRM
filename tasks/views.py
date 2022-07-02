from django.shortcuts import render, redirect
from . models import Tasks
from main.models import User

#View tasks
def tasks(request):
    
    if request.session.get('user_id', None):
        #Add Task
        if request.method == "POST":
            user_id = request.session['user_id']

            id = request.POST.get('id')
            name = request.POST.get('name')
            company = request.POST.get('company')
            date = request.POST.get('date')
            task = request.POST.get('task')

            newTask = Tasks(task_id = id, name = name.lower(), company = company.lower(), date = date, task = task, status = False, user_id = user_id)
            newTask.save()

            return redirect('tasks')
    
        #View Task
        if request.method == "GET":
            user_id = request.session['user_id']
            user = User.objects.get(id = user_id)
            task = Tasks.objects.all().filter(user_id = user_id)

            completed = filter(lambda x: x.status == True , task)
            pending = filter(lambda x: x.status == False, task)

            context = {
                "task1" : completed,
                "task2" : pending,
                "user" : user,
            }

            return render(request, "tasks/tasks.html", context)
        
    else:
        context = {'message' : 'Login to View the Home Page' , 'class' : 'danger' }
        return redirect('authenticate')


def complete(request, id):
    task = Tasks.objects.get(id = id)
    task.status = True
    task.save()
    return redirect('tasks')

