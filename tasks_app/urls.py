from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('tasks/', task_list, name = 'task_list'), 
    path('tasks/<int:task_id>/', task_detail, name='task_detail'),
    path('tasks/new/', task_create, name='task_create'),
    path('category/', category_list, name = 'category_list'),
    path('category/<int:category_id>/', category_tasks, name='category_tasks')
]


