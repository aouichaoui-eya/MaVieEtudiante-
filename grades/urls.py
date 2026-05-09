from django.urls import path
from . import views

app_name = 'grades'

urlpatterns = [
    path('add/', views.add_grade, name='add'),
]