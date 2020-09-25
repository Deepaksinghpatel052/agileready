from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('filter/<str:product_token>/<str:backlog_token>/<str:team_token>', views.filter, name='filter'),

    path('get_data_from_database/', views.get_data_from_database, name='get_data_from_database'),

    path('add-iteration', views.add_iteration, name='add_iteration'),
    path('add-iteration/', views.add_iteration, name='add_iteration'),

    path('get_backlogs', views.get_backlogs, name='get_backlogs'),

    path('get_user_story', views.get_user_story, name='get_user_story'),

    path('get_team', views.get_team, name='get_team'),

    path('edit-iteration/<int:id>', views.edit_iteration, name='edit_iteration'),
    path('edit-iteration/<int:id>/', views.edit_iteration, name='edit_iteration'),

    path('get_storyes_scores_and_size', views.get_storyes_scores_and_size, name='get_storyes_scores_and_size'),

    path('remove-iteration/<int:id>/', views.remove_iteration, name='remove_iteration'),

    path('update-table-structure/<str:columnnames>/', views.update_table_structure, name='update_table_structure'),
    path('update-table-structure/<str:columnnames>/', views.update_table_structure, name='update_table_structure'),
]