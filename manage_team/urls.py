from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),

    path('remove-team/<int:id>', views.remove_team,name='remove_team'),
    path('remove-team/<int:id>/', views.remove_team,name='remove_team'),

    path('edit-team/<int:id>', views.edit_team,name='edit_team'),
    path('edit-team/<int:id>/', views.edit_team,name='edit_team'),
]