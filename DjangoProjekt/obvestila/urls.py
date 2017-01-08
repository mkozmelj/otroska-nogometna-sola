from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^uredi/(?P<obvestila_id>[0-9]+)', views.detail),
    url(r'^uredi/p/(?P<obvestila_id>[0-9]+)', views.posodobi),
    url(r'^izbrisi/(?P<obvestila_id>[0-9]+)', views.izbrisi)
]