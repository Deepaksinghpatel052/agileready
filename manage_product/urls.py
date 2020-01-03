from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('add-product', views.add_product,name='add_product'),
    path('add-product/', views.add_product,name='add_product'),

    path('remove-product/<int:id>', views.remove_product,name='remove_product'),
    path('remove-product/<int:id>/', views.remove_product,name='remove_product'),

    path('edit-product/<int:id>', views.edit_product,name='edit_product'),
    path('edit-product/<int:id>/', views.edit_product,name='edit_product'),

]