from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),

    # path('add-role', views.add_role, name='add_role'),
    # path('add-role/', views.add_role, name='add_role'),

    path('edit-role/<str:id>', views.edit_role, name='edit_role'),
    path('edit-role/<str:id>/', views.edit_role, name='edit_role'),

    path('remove-role/<str:id>', views.remove_role, name='remove_role'),
    path('remove-role/<str:id>/', views.remove_role, name='remove_role'),

    path('get-data', views.get_data, name='get_data'),
    path('get-data/', views.get_data, name='get_data'),


]