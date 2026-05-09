from django.urls import path
from . import views

app_name = "revision"

urlpatterns = [
    path("add/", views.add_task, name="add"),
    path("toggle/<int:task_id>/", views.toggle_task, name="toggle"),
    path("delete/<int:task_id>/", views.delete_task, name="delete"),
]