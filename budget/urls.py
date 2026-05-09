from django.urls import path
from . import views

app_name = "budget"

urlpatterns = [
    path("add/", views.add_transaction, name="add"),
]