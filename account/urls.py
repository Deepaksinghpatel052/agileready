from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),

    path('test_mail', views.test_mail,name='test_mail'),
    path('register', views.register,name='register'),
    path('register/', views.register,name='register'),

    path('activate/<slug:uidb64>/<slug:token>', views.account_activate,name='account_activate'),

    path('send_varification_link', views.send_varification_link,name='send_varification_link'),

    path('login', views.login_user,name='login_user'),

    path('send_forgate_password_link', views.send_forgate_password_link,name='send_forgate_password_link'),
    # path('activate', views.account_activate,name='account_activate'),

]