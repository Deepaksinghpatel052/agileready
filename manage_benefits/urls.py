from django.urls import path
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('edit/<int:id>', views.edit, name='edit'),
        path('remove-benefit/<int:id>', views.remove_benefit, name='remove_benefit'),

        path('get-data', views.get_data, name='get_data'),
        path('get-data/', views.get_data, name='get_data'),
]