from django.shortcuts import render
from .models import Todo
from .models import Note
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TodoForm
from .forms import NoteForm
import uuid

# Create your views here.
def todo(request):        
    if request.method == 'GET':
        user_name = request.COOKIES.get('user_name')
        tasks = Todo.objects.filter(user=user_name).order_by('-task_id')
        form = TodoForm()
        response = render(request = request, template_name='list.html', context={'tasks': tasks, 'form': form})
        if not request.COOKIES.get('user_name'):     
            response.set_cookie('user_name', str(uuid.uuid4()))
        return response

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
           
            Todo.objects.create(task=task, user=request.COOKIES.get('user_name'))
        return HttpResponseRedirect(reverse('todolist'))

def task(request, task_id):
    if request.method == 'GET':
        todo = Todo.objects.get(pk=task_id)
        form = TodoForm(initial = {'task': todo.task})
        return render(request=request, template_name='detail.html', context={'form': form, 'task_id': task_id})

    if request.method == 'POST':
        if 'save' in request.POST:
            form = TodoForm(request.POST)
            if form.is_valid():
                task = form.cleaned_data['task']
                Todo.objects.filter(pk=task_id).update(task=task)
                
        elif 'completed' in request.POST:
            form = TodoForm(request.POST)
            if form.is_valid():
                task=form.cleaned_data['task']
                print(task)
                Todo.objects.filter(pk=task_id).update(task=task, completed=True)

        elif 'in_progress' in request.POST:
            form = TodoForm(request.POST)
            if form.is_valid():
                task=form.cleaned_data['task']
                print(task)
                Todo.objects.filter(pk=task_id).update(task=task, in_progress=True)

        elif 'delete' in request.POST:
            Todo.objects.filter(pk=task_id).delete()

        return HttpResponseRedirect(reverse('todolist'))  

def notes(request):
    if request.method == 'GET':
        notes = Note.objects.all().order_by('note_id')
        form = NoteForm()
        return render(request = request, template_name='notes.html', context={'notes': notes, 'form': form})

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.cleaned_data['notes']
            Note.objects.create(note_text=note)

        elif 'delete' in request.POST:
            Note.objects.all().delete()
            
        return HttpResponseRedirect(reverse('notes'))
    


