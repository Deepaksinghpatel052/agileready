from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('add-user-story-view', views.add_user_story_view, name='add_user_story_view'),
    path('add-user-story-view/', views.add_user_story_view, name='add_user_story_view'),
    path('edit-user-story-view', views.edit_user_story_view, name='edit_user_story_view'),
    path('edit-user-story-view/', views.edit_user_story_view, name='edit_user_story_view'),


]