from django.shortcuts import render,redirect
from .forms import TodosForm
from .models import Todos

# Create your views here.
def createTodos(request):
    context={}
    form=TodosForm
    context["form"]=form
    if request.method=="POST":
        form=TodosForm(request.POST)
        if form.is_valid():
            task=form.cleaned_data.get("task")
            date=form.cleaned_data.get("date")
            status=form.cleaned_data.get("status")
            todo = Todos(task=task, date=date, status=status)
            todo.save()
            return redirect("listtodo")
        form = TodosForm(request.POST)
        context["form"] = form
        return render(request,"todos/createtodos.html",context)
    return render(request,"todos/createtodos.html",context)


def list_todos(request):
    todos=Todos.objects.all()
    context={}
    context["todos"]=todos
    return render(request,"todos/listtodos.html",context)


def view_todos(request,id):
    todo=Todos.objects.get(id=id)
    context={}
    context["todo"]=todo
    return render(request,"todos/viewtodos.html",context)

def delete_todo(request,id):
    todo=Todos.objects.get(id=id)
    todo.delete()
    return redirect("listtodo")


def update_todo(request,id):
    todo=Todos.objects.get(id=id)
    td={
        "task":todo.task,
        "date":todo.date,
        "status":todo.status,
        }
    form=TodosForm(initial=td);
    context={}
    context["form"]=form
    if request.method == "POST":
        form = TodosForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data.get("task")
            date = form.cleaned_data.get("date")
            status = form.cleaned_data.get("status")
            todo.task=task
            todo.date=date
            todo.status=status
            todo.save()
            return redirect("listtodo")
        else:
            context["form"]=form
            return render(request, "todos/updatetodos.html", context)

    return render(request,"todos/updatetodos.html",context)