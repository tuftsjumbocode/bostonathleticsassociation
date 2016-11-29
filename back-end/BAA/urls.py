"""BAA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.contrib import admin
from django.conf.urls import url, include
from rest_framework.authtoken import views

# routers

#router = routers.DefaultRouter()
#router.register(r'volunteers/$', )



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    url(r'docs/', include('rest_framework_docs.urls')),
    url(r'interface/', include('interface.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token)
    ]
