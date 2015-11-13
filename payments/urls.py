from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from . import views

admin.autodiscover()

urlpatterns = (
    url(r'^all/$', views.payments_all, name="payments_all"),
    url(r'^add/$', views.payments_add, name="payments_add"),
    url(r'^create/$', views.payments_create, name="payments_create"),
    url(r'^search/$', views.payments_search, name="payments_search"),
)
