from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^obvestila/', include('obvestila.urls')),
    url(r'^index/', include('home.urls')),
    url(r'^urniki/', include('urniki.urls')),
    url(r'^galerija/', include('galerija.urls')),
    url(r'^prijava/', include('prijava.urls')),
    url(r'^trener/', include('trener.urls')),
    url(r'^$', views.index)
]