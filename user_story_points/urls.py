from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),


    path('add-story-point', views.add_story_point, name='add_story_point'),
    path('add-story-point/', views.add_story_point, name='add_story_point'),

    path('edit-story-point/<str:id>', views.edit_story_point, name='edit_story_point'),
    path('edit-story-point/<str:id>/', views.edit_story_point, name='edit_story_point'),

    path('delete-story-point/<str:id>', views.delete_story_point, name='delete_story_point'),
    path('delete-story-point/<str:id>/', views.delete_story_point, name='delete_story_point'),


]