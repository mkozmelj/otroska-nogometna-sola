from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'1', views.poskus_prijave),
    url(r'registracija', views.regist),
]