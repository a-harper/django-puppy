from django.conf.urls import url

from . import views

urlpatterns = [
    # e.g. /puppy/
    url(r'^$', views.index, name='index')
]