from django.conf.urls import url
from . import views

app_name = 'food_list'
urlpatterns = [
    # ex: /food_list
    url(r'^$', views.index, name='index'),
    # ex: /food_list/3
    # TODO: make it 20170630
    url(r'^(?P<dailyfoodlist_id>[0-9]+)/$', views.daily_list, name='daily_list'),
    # ex: /food_list/food
    url(r'^food/$', views.food_index, name='food_index'),
    # ex: /food_list/food/3
    url(r'^food/(?P<food_id>[0-9]+)/$', views.food, name='food_detail')
]
