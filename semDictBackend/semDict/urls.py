from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main/$', views.token_list, name='token_list'),
]
