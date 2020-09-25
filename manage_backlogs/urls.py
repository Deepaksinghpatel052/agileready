from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('backlog-view', views.backlogview, name='backlogview'),
    path('backlog-view/', views.backlogview, name='backlogview'),

    path('filter/<str:product_token>/<str:team_token>', views.filter, name='filter'),

    # path('manage', views.index, name='index'),
    # path('manage/', views.index, name='index'),

    path('update-table-structure/<str:columnnames>', views.update_table_structure, name='update_table_structure'),
    path('update-table-structure/<str:columnnames>/', views.update_table_structure, name='update_table_structure'),

    path('add-backlog', views.add_backlog, name='add_backlog'),
    path('add-backlog/', views.add_backlog, name='add_backlog'),

    path('edit-backlog/<str:id>', views.edit_backlog, name='edit_backlog'),
    path('edit-backlog/<str:id>/', views.edit_backlog, name='edit_backlog'),

    path('delete-backlog/<str:id>', views.delete_backlog, name='delete_backlog'),
    path('delete-backlog/<str:id>/', views.delete_backlog, name='delete_backlog'),

    path('export-backlog', views.export_backlog, name='export_backlog'),
    path('export-backlog/', views.export_backlog, name='export_backlog'),

    path('get_data_from_database/', views.get_data_from_database, name='get_data_from_database'),


]