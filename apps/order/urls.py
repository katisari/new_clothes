from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^login$', views.login),
    url(r'^$', views.index),
    url(r'^login_process$', views.login_process),
    url(r'^admin$', views.admin),
    url(r'^order$', views.order),
    url(r'^addcart$', views.addcart),
    url(r'^pics/api$', views.photo_api),
    url(r'^logoff$', views.logoff),
]                            # anticipation of all the routes that will be coming soon