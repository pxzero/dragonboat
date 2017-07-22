from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^become_caption', views.become_caption, name='become_caption'),
    url(r'^search_boat', views.search_boat, name='search_boat'),
    url(r'^become_follower', views.become_follower, name='become_follower'),
]
