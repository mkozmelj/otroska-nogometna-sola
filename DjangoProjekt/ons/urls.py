from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^obvestila/', include('obvestila.urls')),
    url(r'^index/', include('home.urls')),
    url(r'^$', views.index)
]