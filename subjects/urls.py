from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.subject_list, name='list'),
    url(r'(?P<subject_pk>\d+)/(?P<activity_pk>\d+)/$', views.activity_detail, name='activity'),
    url(r'(?P<pk>\d+)/$', views.subject_detail, name='detail'),
]