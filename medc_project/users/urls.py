from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from . import views

admin.autodiscover()
urlpatterns = (
    url(r'^login/$', views.user_login, name="login"),
    url(r'^logout/$', views.user_login, name="logout"),
)
