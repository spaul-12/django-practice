from django.urls import path
from . import views

urlpatterns = [
    path('',views.apioverview,name="home"),
    path('tasklist/',views.tasklist,name="tasklist"),
    path('task-detail/<str:pk>',views.taskdetail,name="detail"),
    path('task-update/<str:pk>',views.taskupdate,name="taskupdate"),
    path('task-create/',views.createtask,name="taskcreate"),
    path('deletetask/<str:pk>/',views.deltask,name="delete")
]