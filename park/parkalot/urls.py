from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index, name="index"),
    url(r'^(?P<k>\w+)/$', views.detail,name="detail"),
    url(r'^qrgenerator.html',views.qr,name="QR-Code"),

    #127.0.0.1:8000/parkstat/DL31CH6787
]