from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from todoprojectapp.models import Task

from todoprojectapp.forms import TaskForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # messages.success(request, 'You are now registered and can log in')
            # Log the user in.
            login(request, user)
            return redirect('dashboard')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def welcome(request):
    print("Welcome View Accessed!")
    return render(request, 'registration/welcome.html')
@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'dashboard/dashboard.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'task/TaskForm.html', {'form': form})

@login_required
def update_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/TaskForm.html', {'form': form})

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('dashboard')
    return render(request, 'task/confirm_delete.html', {'object': task})

@login_required
def user_profile(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'user_profile.html', {'tasks': tasks})