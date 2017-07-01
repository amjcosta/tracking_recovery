from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /food_list
    url(r'^$', views.index, name='index'),
    # ex: /food_list/20170630
    url(r'^(?P<dailyfoodlist_id>[0-9]+)/$', views.daily_list, name='daily_list'),
]
