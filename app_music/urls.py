from django.conf.urls import url
# from django.urls import path
from . import views

# namespacing
app_name = 'app_music'

urlpatterns = [
    # /app_music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /app_music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail' ),

    # /app_music/<album_id>/favorite/
    # url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name = 'favorite'),

    # /app_music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /app_music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /app_music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
]