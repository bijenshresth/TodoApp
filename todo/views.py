from django.shortcuts import render, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    todos = Todo.objects.all()
    form = TodoForm()
    return render(request, 'todo/index.html', {"todos": todos, "form": form})


def create(request):
    form = TodoForm(request.POST)
    form.save(commit=True)
    return HttpResponseRedirect(reverse('todo:index'))

def delete(request, id=None):
    post = get_object_or_404(Todo, pk=id)
    post.delete()
    return HttpResponseRedirect(reverse('todo:index'))
    

