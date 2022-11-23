from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('create-post', views.create_post, name='create_post'),
    path('account', views.account, name='account'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'),
     name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'),
     name='password_change_done'),
     path('ban_warning', views.ban_warning, name='ban_warning'),
]
