from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-csv-files', views.add_csv_files, name='add_csv_files'),
    path('read_csv_files', views.read_csv_files, name='read_csv_files'),
    path('read_csv_file_for_user_story/<int:file_id>', views.read_csv_file_for_user_story, name='read_csv_file_for_user_story'),
    path('read_csv_file_for_iteration', views.read_csv_file_for_iteration, name='read_csv_file_for_iteration'),
    path('get_user_name', views.get_user_name, name='get_user_name'),

    path('my-subscription', views.my_subscription, name='my_subscription'),

    path('logout', views.logout, name='logout'),
    path('logout/', views.logout, name='logout'),
]