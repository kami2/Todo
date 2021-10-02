from django.urls import path
from . import views

urlpatterns = [
    path('', views.todoappOverview, name="todoapp-overview"),
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
    path('task-new/', views.taskNew, name="task-new"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
  ]