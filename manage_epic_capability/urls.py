from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),


    path('add-epic-capabilities', views.add_epic_capabilities, name='add_epic_capabilities'),
    path('add-epic-capabilities/', views.add_epic_capabilities, name='add_epic_capabilities'),

    path('get_capanility/<int:id>', views.get_capanility, name='get_capanility'),

    path('edit-epic-capabilities/<str:id>', views.edit_epic_capabilities, name='edit_epic_capabilities'),
    path('edit-epic-capabilities/<str:id>/', views.edit_epic_capabilities, name='edit_epic_capabilities'),

    path('delete-epic-capabilities/<str:id>', views.delete_epic_capabilities, name='delete_epic_capabilities'),
    path('delete-epic-capabilities/<str:id>/', views.delete_epic_capabilities, name='delete_epic_capabilities'),

]