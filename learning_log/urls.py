"""
URL configuration for learning_log project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib.sitemaps.views import sitemap
from .sitemap import TopicSitemap
from django.views.generic import TemplateView

sitemaps = {
    'topics': TopicSitemap,
}



urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('', include('learning_logs.urls', namespace='learning_logs')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path('google1234567890abcdef.html', TemplateView.as_view(template_name='google1234567890abcdef.html', content_type='text/html'))
]
