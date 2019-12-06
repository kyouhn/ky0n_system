from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'sendmail'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
]