from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /gameapp/
    url(r'^$', views.index, name='index'),
    url(r'^developerhome/$', views.developerhome, name='developerhome'),
    url(r'^developerhome/addgame/$', views.addgame, name='addgame'),
    url(r'^developerhome/delete/(?P<game_id>[0-9]+)/$', views.deletegame, name='deletegame'),
    url(r'^developerhome/edit/(?P<game_id>[0-9]+)/$', views.editgame, name='editgame'),
    url(r'^developerhome/allgames/$', views.allgames, name='allgames'),
    url(r'^playerhome/$', views.playerhome, name='playerhome'),
    url(r'^playerhome/searchresults/$', views.searchresults, name='searchresults'),
    url(r'^register/$', views.registration, name='registration'),
    url(r'^playerhome/mygames/$', views.mygames, name='mygames'),
    url(r'^playerhome/gameplay/(?P<game_id>[0-9]+)/$', views.gameplay, name='mygames'),
    url(r'^success/(?P<game_id>[0-9]+)/$', views.success, name='success'),
    url(r'^cancel/(?P<game_id>[0-9]+)/$', views.cancel, name='cancel'),
    url(r'^error/(?P<game_id>[0-9]+)/$', views.error, name='error'),
    url(r'^logout/$', views.logout_view, name='logout'),
]
