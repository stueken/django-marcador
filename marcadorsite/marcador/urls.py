from django.conf.urls import url


urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', 'marcador.views.bookmark_user',
        name='marcador_bookmark_user'),
    url(r'^create/$', 'marcador.views.bookmark_create',
        name='marcador_bookmark_create'),
    url(r'^edit/(?P<pk>\d+)/$', 'marcador.views.bookmark_edit',
        name='marcador_bookmark_edit'),
    url(r'^$', 'marcador.views.bookmark_list', name='marcador_bookmark_list'),
]
