from django.urls import path
from . import views

urlpatterns = [
    path("", views.CreateAjax, name="ajaxCall"),
    path("delete/", views.Delete, name="delete"),
]