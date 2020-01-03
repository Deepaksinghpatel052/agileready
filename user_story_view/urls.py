from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('add-new', views.add_user_story_view, name='add_user_story_view'),
    path('add-new/', views.add_user_story_view, name='add_user_story_view'),

    path('edit-story/<int:id>', views.edit_user_story_view, name='edit_user_story_view'),
    path('edit-story/<int:id>/', views.edit_user_story_view, name='edit_user_story_view'),

    path('remove-user-story/<int:id>', views.delete_user_story_view, name='delete_user_story_view'),
    path('remove-user-story/<int:id>/', views.delete_user_story_view, name='delete_user_story_view'),

    path('create-copys/<str:ids>', views.select_user_story_view, name='select_user_story_view'),
    path('create-copys/<str:ids>/', views.select_user_story_view, name='select_user_story_view'),

    path('update-table-structure/<str:columnnames>/', views.update_table_structure, name='update_table_structure'),
    path('update-table-structure/<str:columnnames>/', views.update_table_structure, name='update_table_structure'),
]