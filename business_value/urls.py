from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),


    path('edit-business-value/<str:id>', views.edit_business_value, name='edit_business_value'),
    path('edit-business-value/<str:id>/', views.edit_business_value, name='edit_business_value'),
    #
    path('remove-business-value/<str:id>', views.remove_business_value, name='remove_business_value'),
    path('remove-business-value/<str:id>/', views.remove_business_value, name='remove_business_value'),
    #
    # path('get-data', views.get_data, name='get_data'),
    # path('get-data/', views.get_data, name='get_data'),


]