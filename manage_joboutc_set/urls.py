from django.urls import path
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('edit/<int:id>', views.edit, name='edit'),
        path('remove-Joboutc-Set/<int:id>', views.remove_Joboutc_Set, name='remove_Joboutc_Set'),
        #
        # path('get-data', views.get_data, name='get_data'),
        # path('get-data/', views.get_data, name='get_data'),
]