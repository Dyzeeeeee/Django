from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    # path('add/', views.addTodo, name='add-todo'),
    path('complete-todo/<todo_id>', views.completeTodo, name='complete-todo'),
    # path('deletecompleted/', views.deleteCompleted, name='deletecompleted'),
]