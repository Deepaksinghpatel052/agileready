from django.urls import path
from . import views

urlpatterns = [
    path('', views.export_data,name='export_data'),
    path('export-data', views.export_data,name='export_data'),
    path('export-data/', views.export_data,name='export_data'),

    path('import-data', views.import_data, name='import_data'),
    path('import-data/', views.import_data, name='import_data'),

    path('add-csv-files', views.add_csv_files, name='add_csv_files'),
    path('test_csv_file', views.test_csv_file, name='test_csv_file'),

    path('get_data_from_database', views.get_data_from_database,name='get_data_from_database'),
    path('file_download/<int:id>', views.file_download,name='file_download'),

    path('download/<str:id>', views.download,name='download'),

    path('get_demo_csv', views.get_demo_csv,name='get_demo_csv'),
]