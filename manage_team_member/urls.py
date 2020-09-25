from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),


    path('edit-team-member/<str:id>', views.edit_team_member, name='edit_team_member'),
    path('edit-team-member/<str:id>/', views.edit_team_member, name='edit_team_member'),
    path('update_root_user/<str:id>/', views.update_root_user, name='update_root_user'),

    path('delete-team-member/<str:id>', views.delete_team_member, name='delete_team_member'),
    path('delete-team-member/<str:id>/', views.delete_team_member, name='delete_team_member'),
]