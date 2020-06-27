"""sisghoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from apps.core import forms as formularios

from apps.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls'), name='core'),
    path('login/', auth_views.LoginView.as_view(template_name='login/index.html', redirect_authenticated_user = True, authentication_form = formularios.FormLogin), name='login'),
    path('logout/', auth_views.logout_then_login , name='logout'),
    path('login/restablecer_contrasena', auth_views.PasswordResetView.as_view(template_name = 'registration/password_reset_form.html', email_template_name = 'registration/password_reset_email.html', html_email_template_name = 'registration/password_reset_email.html') , name='password_reset'),
    path('login/restablecer_contrasena/done', auth_views.PasswordResetDoneView.as_view(template_name = 'registration/password_reset_done.html') , name='password_reset_done'),
    re_path(r'^login/restablecer_contrasena/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(template_name = 'registration/password_reset_confirm.html') , name='password_reset_confirm'),
    path('login/restablecer_contrasena/complete', auth_views.PasswordResetCompleteView.as_view(template_name = 'registration/password_reset_complete.html') , name='password_reset_complete'),
]
