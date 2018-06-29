from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^order$', views.order),
    url(r'^addcart$', views.addcart),
    url(r'^pics/api$', views.photo_api)
]                            # anticipation of all the routes that will be coming soon