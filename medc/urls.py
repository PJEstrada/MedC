from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from . import views
from schedule.views import  CalendarByPeriodsView,CreateEventView,DeleteEventView,EventView,EditEventView
from schedule.periods import  Month,Day,Week
admin.autodiscover()

urlpatterns = (
     url(r'^$', views.home, name="home"),
     url(r'^home/$', views.home_view, name="home_view"),


    #Estas URL fueron agregadas basandome en los urls.py del schedule, notar el atributo name, al cual se le agrega _medc al final para cambiar las urls en los links dentro de los templates en templates/agenda
    url(r'^month/(?P<calendar_slug>[-\w]+)/$', CalendarByPeriodsView.as_view(),
    name="monthly_view_medc",
    kwargs={'periods': [Month], 'template_name': 'agenda/month.html'}),
    url(r'^daily/(?P<calendar_slug>[-\w]+)/$',
        CalendarByPeriodsView.as_view(),
        name="daily_view",
        kwargs={'periods': [Day], 'template_name': 'agenda/day.html'}),

    url(r'^weekly/(?P<calendar_slug>[-\w]+)/$',
        CalendarByPeriodsView.as_view(),
        name="weekly_view_medc",
        kwargs={'periods': [Week], 'template_name': 'agenda/week.html'}),


        # Create Event Url
    url(r'^event/create/(?P<calendar_slug>[-\w]+)/$',
        CreateEventView.as_view(),
        name='create_event'),
    url(r'^event/delete/(?P<event_id>\d+)/$',
        DeleteEventView.as_view(),
        name="delete_created_event"),
    url(r'^event/(?P<event_id>\d+)/$',
        EventView.as_view(),
        name="event_medc"),
    url(r'^event/edit/(?P<calendar_slug>[-\w]+)/(?P<event_id>\d+)/$',
        EditEventView.as_view(),
        name='edit_event_medc'),
)
