from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('get_data_from_database/', views.get_data_from_database, name='get_data_from_database'),


    # path('/<str:set_statue>/<str:set_statue_2>', views.index, name='index'),
    # path('/<str:set_statue>/<str:set_statue_2>/<str:csv_id>', views.index, name='index'),

    # path('test_data', views.test_data, name='test_data'),
    path('add-new', views.add_job_story_view, name='add_job_story_view'),
    path('get_file_data', views.get_file_data, name='get_file_data'),

    path('add-new/', views.add_job_story_view, name='add_job_story_view'),

    path('get-data', views.get_data, name='get_data'),
    path('get-data/', views.get_data, name='get_data'),

    path('add-csv-files/', views.add_csv_files, name='add_csv_files'),
    path('add-csv-files', views.add_csv_files, name='add_csv_files'),

    path('edit-story/<int:id>', views.edit_job_story_view, name='edit_job_story_view'),
    path('edit-story/<int:id>/', views.edit_job_story_view, name='edit_job_story_view'),

    path('remove-job-story/<int:id>', views.delete_job_story_view, name='delete_job_story_view'),
    path('remove-job-story/<int:id>/', views.delete_job_story_view, name='delete_job_story_view'),


    path('remove-story-file/<int:id>', views.remove_story_file, name='remove_story_file'),
    path('remove-story-file/<int:id>/', views.remove_story_file, name='remove_story_file'),

    path('create-copys/<str:ids>', views.select_job_story_view, name='select_job_story_view'),
    path('create-copys/<str:ids>/', views.select_job_story_view, name='select_job_story_view'),

    path('update-table-structure/<str:columnnames>/', views.update_table_structure, name='update_table_structure'),
    path('update-table-structure/<str:columnnames>/', views.update_table_structure, name='update_table_structure'),

    path('get-criteria-data', views.get_criteria_data, name='get_criteria_data'),
    path('get-criteria-data/', views.get_criteria_data, name='get_criteria_data'),

    path('get-conversations-data', views.get_conversations_data, name='get_conversations_data'),
    path('get-conversations-data/', views.get_conversations_data, name='get_conversations_data'),

]