from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from . import views

admin.autodiscover()

urlpatterns = (
    url(r'^$', views.records_general, name="records_general"),
    url(r'^search/$', views.records_search, name="records_search"),
    url(r'^single/(?P<id>\d+)/$', views.records_single, name="records_single"),
    url(r'^add/$', views.records_add, name="records_add"),
)
