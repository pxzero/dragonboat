from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^boat_activation', views.boatActive, name='boat_activation'),
]
