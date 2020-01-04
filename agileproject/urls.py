"""agileproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path('superadmin/', admin.site.urls),
    path('', include('home.urls')),

    path('accounts/login', views.login_page, name='login_page'),
    path('accounts/login/', views.login_page, name='login_page'),

    path('signin', include('home.urls')),
    path('', include('django.contrib.auth.urls')),
    path('password/', include('django.contrib.auth.urls')),

    path('dashboard/', include('dashboard.urls')),
    path('dashboard', include('dashboard.urls')),
    
    path('account/', include('account.urls')),
    path('account', include('account.urls')),

    

    path('account-settings', include('account_settings.urls')),
    path('account-settings/', include('account_settings.urls')),

    path('invite-user', include('invite_user.urls')),
    path('invite-user/', include('invite_user.urls')),


    path('manage-products', include('manage_product.urls')),
    path('manage-products/', include('manage_product.urls')),

    path('user-story-view', include('user_story_view.urls')),
    path('user-story-view/', include('user_story_view.urls')),
    
    path('manage-team', include('manage_team.urls')),
    path('manage-team/', include('manage_team.urls')),

    path('manage-epic-capabilities', include('manage_epic_capability.urls')),
    path('manage-epic-capabilities/', include('manage_epic_capability.urls')),

    path('manage-feature', include('manage_features.urls')),
    path('manage-feature/', include('manage_features.urls')),

    path('manage-backlog', include('manage_backlogs.urls')),
    path('manage-backlog/', include('manage_backlogs.urls')),

    path('product-view', include('product_view.urls')),
    path('product-view/', include('product_view.urls')),

    path('backlog-view', include('backlog_view.urls')),
    path('backlog-view/', include('backlog_view.urls')),

    path('user-profile', include('manage_user_profile.urls')),
    path('user-profile/', include('manage_user_profile.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
