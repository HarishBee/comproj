"""
URL configuration for bab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView,PasswordResetConfirmView, PasswordResetCompleteView
from babapp import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('home/',TemplateView.as_view(template_name='social_app/home.html'),name='home'),
    path('login',views.login, name='login'),
    path('register',views.register,name='register'),
    path('verify',views.verify,name='verify'),
    path('home',views.home,name='home'),
    path('accounts/', include('allauth.urls')),
    path('forgot',views.forgot,name='forgot'),
    path('password',views.password,name='password'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_reset_email',views.password_reset_email,name='password_reset_email'),
    path('social-auth/',include('social_django.urls',namespace='social')),
    
]

