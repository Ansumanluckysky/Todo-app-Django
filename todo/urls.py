from django.urls import path
from . import views

urlpatterns=[
    # Add Task
    path('addTask/',views.addTask,name='addTask'),

    #Mark as Done
    path('mark_as_done/<int:pk>',views.mark_as_done,name='mark_as_done'),

    # Edit Feature

    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),

    # Delete Task

    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),



]