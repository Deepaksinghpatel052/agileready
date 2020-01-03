from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),


    path('add-feature', views.add_features, name='add_features'),
    path('add-feature/', views.add_features, name='add_features'),

    path('edit-feature/<str:id>', views.edit_features, name='edit_features'),
    path('edit-feature/<str:id>/', views.edit_features, name='edit_features'),

    path('delete-feature/<str:id>', views.delete_features, name='delete_features'),
    path('delete-feature/<str:id>/', views.delete_features, name='delete_features'),

    path('get-data', views.get_data, name='get_data'),
    path('get-data/', views.get_data, name='get_data'),

]