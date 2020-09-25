from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    # path('/', views.index, name='index'),


    path('ar-whyar/', views.whyar, name='whyar'),
    path('ar-whyar', views.whyar, name='whyar'),

    path('view-information/<slug:keyword>/', views.view_information, name='view_information'),
    path('view-information/<slug:keyword>', views.view_information, name='view_information'),


    path('ar-company/', views.company, name='company'),
    path('ar-company', views.company, name='company'),

    path('subscription/', views.subscription, name='subscription'),
    path('subscription/<str:amounte>/<str:packeg_id>', views.subscription, name='subscription'),
    path('subscription', views.subscription, name='subscription'),
    
    path('do_payments', views.do_payments, name='do_payments'),
    path('do_payments/', views.do_payments, name='do_payments'),

    path('ar-usrating/', views.usrating, name='usrating'),
    path('ar-usrating', views.usrating, name='usrating'),

    path('ar-usrating/', views.usrating, name='usrating'),
    path('ar-usrating', views.usrating, name='usrating'),

    path('security', views.security, name='security'),
    path('security/', views.security, name='security'),

    path('privacy', views.privacy, name='privacy'),
    path('privacy/', views.privacy, name='privacy'),

    path('eula', views.eula, name='eula'),
    path('eula/', views.eula, name='eula'),

    path('about-us', views.about_us, name='about_us'),
    path('about-us/', views.about_us, name='about_us'),

    path('contact-us', views.contact_us, name='contact_us'),
    path('contact-us/', views.contact_us, name='contact_us'),

    path('test_data', views.test_data, name='test_data'),

    path('check-login', views.check_login, name='check_login'),


]