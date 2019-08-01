"""djangostart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from app01 import views

# from ..apps import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^demo01/$', views.demo01),
    url(r'^demo02/$', views.demo02),
    url(r"^demo_form2/$", views.demo_form2),
    url(r"^demo_form_db/$", views.demo_form_db),
    # url包含
    url(r'^route_base/', include('apps.route_base.urls',namespace='route_base')),
    url(r'^route_resolve/', include('apps.route_resolve.urls',namespace='route_resolve')),
    url(r'^django_templates/', include('apps.django_templates.urls', namespace='django_templates')),
    url(r'^forms_base/', include('apps.forms_base.urls', namespace='forms_base')),
    url(r'^forms_base/', include('apps.forms_base.urls', namespace='forms_auth')),

]
