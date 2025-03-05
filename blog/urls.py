from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
       path('post', views.list, name='post_list'),
    
    path('post/<int:id>/', views.detail, name='post_detail'),
]
