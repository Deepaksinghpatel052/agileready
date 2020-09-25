from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),

    path('get-data', views.get_data, name='get_data'),
    path('get-data/', views.get_data, name='get_data'),

    path('set_default_data/', views.set_default_data, name='set_default_data'),
    path('set_default_data', views.set_default_data, name='set_default_data'),


    path('pass-change', views.pass_change, name='pass_change'),
    path('pass-change/', views.pass_change, name='pass_change'),
]