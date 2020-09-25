from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('add-profile', views.add_profile, name='add_profile'),
    path('add-profile/', views.add_profile, name='add_profile'),
    #
    path('edit-user-profile/<str:id>', views.edit_user_profile, name='edit_user_profile'),
    path('edit-user-profile/<str:id>/', views.edit_user_profile, name='edit_user_profile'),
    #
    path('delete-user-profile/<int:id>', views.delete_user_profile, name='delete_user_profile'),
    path('delete-user-profile/<int:id>/', views.delete_user_profile, name='delete_user_profile'),


    path('get-data', views.get_data, name='get_data'),
    path('get-data/', views.get_data, name='get_data'),
    #
    # path('export-backlog', views.export_backlog, name='export_backlog'),
    # path('export-backlog/', views.export_backlog, name='export_backlog'),


]