from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.showPlayers, name='index'),
    url(r'^teams/$', views.teams , name='teams'),
    url(r'^teams/(?P<num>\d+)/$', views.teams),
    url(r'^teams/delete', views.deleteTeam, name='delete_team'),
    url(r'^countries', views.countries , name='countries'),
    url(r'^create', views.createPlayer , name='create_player'),
    url(r'^edit', views.editPlayer, name='edit_player'),
    url(r'^delete', views.deletePlayer, name='delete_player'),
    url(r'^store', views.storePlayer, name='store_player'),
    url(r'^update', views.updatePlayer, name='update_player'),
]



