from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
        url(r'^post/new/$', views.post_new, name='post_new'),
        url(r'^post/register/$', views.post_register, name='post_register'),
        url(r'^post/log_in/$', views.log_in, name='log_in'),
        url(r'^post/log_out/$', views.log_out, name='log_out'),
        ]