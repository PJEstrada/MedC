from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from . import views

admin.autodiscover()
urlpatterns = (
    url(r'^login/$', views.user_login, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/users/login'},name="logout"),
)
