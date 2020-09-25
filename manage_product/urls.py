from django.urls import path
from . import views

urlpatterns = [
    # path('', views.productview,name='productview'),

    path('', views.index,name='index'),
    path('', views.index,name='index'),

    path('get_data_from_database/', views.get_data_from_database, name='get_data_from_database'),
    path('add-product', views.add_product,name='add_product'),
    path('add-product/', views.add_product,name='add_product'),

    path('update-table-structure/<str:columnnames>', views.update_table_structure,name='update_table_structure'),
    path('update-table-structure/<str:columnnames>/', views.update_table_structure,name='update_table_structure'),

    path('remove-product/<int:id>', views.remove_product,name='remove_product'),
    path('remove-product/<int:id>/', views.remove_product,name='remove_product'),

    path('edit-product/<int:id>', views.edit_product,name='edit_product'),
    path('edit-product/<int:id>/', views.edit_product,name='edit_product'),


]