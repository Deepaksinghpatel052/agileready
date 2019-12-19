from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    # path('/', views.index, name='index'),

    path('ar-whyar/', views.whyar, name='whyar'),
    path('ar-whyar', views.whyar, name='whyar'),

    path('ar-company/', views.company, name='company'),
    path('ar-company', views.company, name='company'),

    path('subscription/', views.subscription, name='subscription'),
    path('subscription', views.subscription, name='subscription'),

    path('ar-usrating/', views.usrating, name='usrating'),
    path('ar-usrating', views.usrating, name='usrating'),


]