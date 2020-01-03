from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('add-backlog', views.add_backlog, name='add_backlog'),
    path('add-backlog/', views.add_backlog, name='add_backlog'),

    path('edit-backlog/<str:id>', views.edit_backlog, name='edit_backlog'),
    path('edit-backlog/<str:id>/', views.edit_backlog, name='edit_backlog'),

    path('delete-backlog/<str:id>', views.delete_backlog, name='delete_backlog'),
    path('delete-backlog/<str:id>/', views.delete_backlog, name='delete_backlog'),

    path('export-backlog', views.export_backlog, name='export_backlog'),
    path('export-backlog/', views.export_backlog, name='export_backlog'),


]