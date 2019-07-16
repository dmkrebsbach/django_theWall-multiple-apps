from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'logout$', views.logout),
    url(r'add_message$', views.add_message),
    url(r'success$', views.success),
    url(r'comment/(?P<messageId>\d+)$', views.comment),
    url(r'delete/(?P<messageId>\d+)$', views.delete),
]