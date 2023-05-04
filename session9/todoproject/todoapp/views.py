from django.shortcuts import render, redirect
from .models import Todo
from datetime import datetime, timedelta
from datetime import date

# Create your views here.
def home(request):
    todos = Todo.objects.all()
    order_todos = todos.order_by('dueday')
    for todo in order_todos:
        todo.remain_day = (todo.dueday - date.today()).days
        print(todo.remain_day)

    return render(request, 'home.html', {'todos':order_todos})

def new(request):
     if request.method == 'POST':
        print(request.POST)
        day = request.POST['dueday']
        print(day)
        new_todo = Todo.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            time = datetime.now(),
            dueday = day 
        )
        return redirect('detail',new_todo.pk)
     
     return render(request, 'new.html')

def detail(request, todo_id):
    details = Todo.objects.get(id=todo_id)

    return render(request, 'detail.html', {'details':details})

def update(request, todo_id):
    updates = Todo.objects.get(id=todo_id)

    if request.method == 'POST':
        day = request.POST['dueday']
        Todo.objects.filter(id = todo_id).update(  
            title = request.POST['title'],
            content = request.POST['content'],
            dueday = day
        )
        return redirect ('detail', todo_id)
    
    return render(request, 'update.html', {'updates':updates})

def delete(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    todo.delete()
    return redirect('home')