"""django_raffle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static

from django_raffle import settings
from raffle import views as raffle_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rifa/(?P<pk>\d+)/$', raffle_views.home),
    url(r'^rifa/ganador/(?P<pk>\d+)/$', raffle_views.winner),
    url(r'^rifa/crear/$', raffle_views.create),
    url(r'^rifas/$', raffle_views.list, name='list'),
    url(r'^$', raffle_views.list, name='list'),
    url(r'^api/rifa/resultados/(?P<pk>\d+)/$', raffle_views.results, name='results'),
    url(r'^api/rifa/ganador/(?P<pk>\d+)/$', raffle_views.save_winner, name='save_winner'),
    url(r'^generate_excel/(?P<pk>\d+)/$', raffle_views.generate_excel, name='generate_excel'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

