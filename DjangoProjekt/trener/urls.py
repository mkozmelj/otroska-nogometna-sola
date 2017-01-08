from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'logout', views.odjava),
    url(r'dodaj', views.dodaj),
    url(r'zamenjaj', views.zamenjajSliko)
]