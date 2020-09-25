from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),

    path('filter/<str:token>', views.filter, name='filter'),

    path('get_data_from_database/', views.get_data_from_database, name='get_data_from_database'),

    # path('activate/<slug:uidb64>/<slug:token>', views.account_activate, name='account_activate'),
    #
    path('add-scenario', views.add_scenario, name='add_scenario'),
    path('add-scenario/', views.add_scenario, name='add_scenario'),
    #
    path('edit-scenario/<str:id>', views.edit_scenario, name='edit_scenario'),
    path('edit-scenario/<str:id>/', views.edit_scenario, name='edit_scenario'),
    #
    path('remove-scenario/<str:id>', views.remove_scenario, name='remove_scenario'),
    path('remove-scenario/<str:id>/', views.remove_scenario, name='remove_scenario'),
    #
    # path('get-data', views.get_data, name='get_data'),
    # path('get-data/', views.get_data, name='get_data'),

    path('update-table-structure/<str:columnnames>/', views.update_table_structure, name='update_table_structure'),
    path('update-table-structure/<str:columnnames>/', views.update_table_structure, name='update_table_structure'),


    #


]