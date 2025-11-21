from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # edit
    path("create", views.create, name="create"),  # postscript
]