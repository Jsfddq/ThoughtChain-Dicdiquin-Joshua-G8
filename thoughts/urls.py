from django.urls import path
from . import views

urlpatterns = [
    path('', views.node_list, name='node_list'),
    path('create/', views.node_create, name='node_create'),
    path('update/<int:pk>/', views.node_update, name='node_update'),
    path('delete/<int:pk>/', views.node_delete, name='node_delete'),
]