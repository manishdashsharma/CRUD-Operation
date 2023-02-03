from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import schoolForm
from .models import school_database
from django.utils import timezone


# Create your views here.


def index(request):

    todoList = school_database.objects.all().order_by('-date')

    return render(request, 'list.html', {'list': todoList})


def saveAction(request):
    print(request.POST)
    todoform = schoolForm(request.POST or None)

    if todoform.is_valid():
        todoform.save()

        return redirect('/')
    return render(request, 'index.html', {'form': todoform})


def edit(request, pk):

    pickTodo = school_database.objects.get(pk=pk)

    editForm = schoolForm(request.POST or None, instance=pickTodo)

    if editForm.is_valid():
        editForm.save()
        return redirect('/')

    return render(request, 'index.html', {'form': editForm})


def deleteAction(request, pk):

    pickTodo = school_database.objects.get(pk=pk)
    pickTodo.delete()

    return redirect('/')