from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('add-user-story-view', views.add_user_story_view, name='add_user_story_view'),
    path('add-user-story-view/', views.add_user_story_view, name='add_user_story_view'),
    path('edit-user-story-view/<str:id>', views.edit_user_story_view, name='edit_user_story_view'),
    path('edit-user-story-view/<str:id>/', views.edit_user_story_view, name='edit_user_story_view'),
    path('delete-user-story-view/<str:id>', views.delete_user_story_view, name='delete_user_story_view'),
    path('delete-user-story-view/<str:id>/', views.delete_user_story_view, name='delete_user_story_view'),


]