from django.urls import path
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('edit/<int:id>', views.edit, name='edit'),
        path('remove-goal/<int:id>', views.remove_goal, name='remove_goal'),

        path('get-data', views.get_data, name='get_data'),
        path('get-data/', views.get_data, name='get_data'),
]