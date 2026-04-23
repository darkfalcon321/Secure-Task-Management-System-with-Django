from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, Category
from .forms import PostTask

# Create your views here.

def home(request):
    return render(request, 'base.html')

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = get_object_or_404(Task, id = task_id)
    return render(request, 'task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':    
        form = PostTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  
    else:
        form = PostTask()
    return render(request, 'task_create.html', {'forms': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_tasks(request, category_id):
    category = get_object_or_404(Category, id = category_id)
    tasks = Task.objects.filter(category=category)
    return render(request, 'category_tasks.html', {'category': category, 'tasks': tasks})