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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views


import django_summernote.urls

handler404 = views.handler404
handler500 = views.handler500

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),


    path('superadmin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
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


    # path('manage-products', include('manage_product.urls')),
    path('manage-products/', include('manage_product.urls')),

    # path('products-view', include('manage_product.urls')),
    path('products-view/', include('manage_product.urls')),

    # path('user-story-view', include('user_story_view.urls')),
    path('user-story-view/', include('user_story_view.urls')),

    path('manage-team', include('manage_team.urls')),
    path('manage-team/', include('manage_team.urls')),

    path('manage-role', include('manage_role.urls')),
    path('manage-role/', include('manage_role.urls')),

    path('manage-epic-capabilities', include('manage_epic_capability.urls')),
    path('manage-epic-capabilities/', include('manage_epic_capability.urls')),

    path('manage-feature', include('manage_features.urls')),
    path('manage-feature/', include('manage_features.urls')),

    # path('manage-backlog', include('manage_backlogs.urls')),
    path('manage-backlog/', include('manage_backlogs.urls')),

    # path('backlog-view', include('manage_backlogs.urls')),
    path('backlog-view/', include('manage_backlogs.urls')),

    # path('iteration-view', include('manage_iterations.urls')),
    path('iteration-view/', include('manage_iterations.urls')),

    path('manage-iteration', include('manage_iterations.urls')),
    path('manage-iteration/', include('manage_iterations.urls')),

    # path('product-view', include('product_view.urls')),
    # path('product-view/', include('product_view.urls')),
    #
    # path('backlog-view', include('backlog_view.urls')),
    # path('backlog-view/', include('backlog_view.urls')),
    #
    path('user-profile', include('manage_user_profile.urls')),
    path('user-profile/', include('manage_user_profile.urls')),

    path('story-points', include('user_story_points.urls')),
    path('story-points/', include('user_story_points.urls')),

    path('manage-team-member', include('manage_team_member.urls')),
    path('manage-team-member/', include('manage_team_member.urls')),

    path('feedback', include('feedback.urls')),
    path('feedback/', include('feedback.urls')),

    path('manage-goals', include('manage_goals.urls')),
    path('manage-goals/', include('manage_goals.urls')),
    # ---------------------------------------------------------
    path('business-value', include('business_value.urls')),
    path('business-value/', include('business_value.urls')),
    #
    # path('manage-scenario', include('ar_scenario.urls')),
    path('manage-scenario/', include('ar_scenario.urls')),

    path('manage-jobmot-set', include('manage_jobmot_set.urls')),
    path('manage-jobmot-set/', include('manage_jobmot_set.urls')),

    path('manage-joboutc-set', include('manage_joboutc_set.urls')),
    path('manage-joboutc-set/', include('manage_joboutc_set.urls')),

    path('manage-jobsit-set', include('manage_jobsit_set.urls')),
    path('manage-jobsit-set/', include('manage_jobsit_set.urls')),

    path('manage-testact-set', include('manage_testact_set.urls')),
    path('manage-testact-set/', include('manage_testact_set.urls')),

    path('manage-testcond-set', include('manage_testcond_set.urls')),
    path('manage-testcond-set/', include('manage_testcond_set.urls')),

    path('manage-testoutc-set', include('manage_testoutc_set.urls')),
    path('manage-testoutc-set/', include('manage_testoutc_set.urls')),


    # path('job-story-view', include('job_story_view.urls')),
    path('job-story-view/', include('job_story_view.urls')),


    # path('bdd-tdd-story-view', include('test_story_view.urls')),
    path('bdd-tdd-story-view/', include('test_story_view.urls')),

    path('words-patterns/', include('words_and_patterns.urls')),

    path('user-story-value/', include('user_story_value.urls')),
    path('feature-value/', include('feature_value.urls')),



    # -------------------------------------------------------------------
    path('manage-benefits', include('manage_benefits.urls')),
    path('manage-benefits/', include('manage_benefits.urls')),

    path('membership', include('subscription.urls')),
    path('membership/', include('subscription.urls')),

    path('data-exchange/', include('data_import_export.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
