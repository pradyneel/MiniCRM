from django.urls import path
from . views import tasks, complete

urlpatterns = [
    path('tasks/', tasks, name = "tasks"),
    path('complete/<int:id>', complete, name="complete"),
]