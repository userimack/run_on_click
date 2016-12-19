from django.conf.urls import url
from app.views import index, click

urlpatterns = [
        url(r'^$',index, name='index'),
        url(r'^/click$',click, name='click'),
    ]
