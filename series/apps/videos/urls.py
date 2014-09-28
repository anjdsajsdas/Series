from django.conf.urls import patterns, url
from .views import IndexView, SerieListView, SerieDetailView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
    url(r'^serie/(?P<slug_serie>[-\w]+)/$', SerieListView.as_view(), name = "lista_capitulos"),
    url(r'^ver/(?P<slug_capitulo>[-\w]+)/$', SerieDetailView.as_view()),
)
