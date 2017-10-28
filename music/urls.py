from django.conf.urls import url
from . import views


app_name = 'music'

urlpatterns = [
    #music/register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #music/album_id/
    url(r'^(?P<pk>[0-9]+)/$', views.Detailview.as_view(), name='detail'),

    # music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='create_album'),

    # music/album/2/
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # music/album/add/2/delete
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='delete_album'),
    # music/favorite_album/
    #url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),



]
