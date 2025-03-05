from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("post", views.list,name="list"),
   path("post/<int:id>/", views.detail, name="detail"),
    ##path("post/new/", views.create, name="create"),
]