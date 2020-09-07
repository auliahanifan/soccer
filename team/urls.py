from django.conf.urls import url
from .views import view_teams
 
 
urlpatterns = [
    url(r'^$', view_teams),
]