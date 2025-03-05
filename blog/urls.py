from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='post_list'),
       path('post', views.list, name='post_list'),
    
    path('post/<int:id>/', views.detail, name='post_detail'),
]
