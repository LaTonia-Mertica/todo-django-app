from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name='todolist'),
    path('<int:task_id>', views.task, name='task'),
    path('notes', views.notes, name='notes'),
]


