from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'(?P<page_title>)/$', views.page_detail),
]
