# -*- coding: utf-8 -*-

from django.urls import path
from django.contrib.auth.urls import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("home", views.homepage),
    path("register", views.registration_view),
    path("logout", views.logout_view),
    path("login", views.login_view),
    path("account", views.account_view, name='account'),
    path("delete", views.delete),
    
    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

