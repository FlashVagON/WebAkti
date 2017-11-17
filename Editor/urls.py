from django.conf.urls import url
from Editor import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^list/$', views.PostsListView.as_view()),
    url(r'^post/$', views.addact),
]