"""medc_project URL Configuration

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
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # MedC Home
    url(r'^schedule/', include("schedule.urls")),
    url(r'^', include("medc.urls")),
    url(r'^users/', include("users.urls")),
    url(r'^schedule/', include("schedule.urls")),
    url(r'^patients/', include("patients.urls")),
    url(r'^payments/', include("payments.urls")),
]
if not settings.DEBUG:
    urlpatterns += (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

# handler404 = 'medc.views.error404'
# handler500 = 'medc.views.error404'
# handler400 = 'medc.views.error404'
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)