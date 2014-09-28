from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Serie, Temporada, Capitulo

class IndexView(ListView):

	template_name = 'videos/index.html'
	model = Serie
	context_object_name = "series"

class SerieListView(TemplateView):

	template_name = 'videos/series_list.html'

	def get_context_data(self, **kwargs):
		context = super(SerieListView, self).get_context_data(**kwargs)
		serie = Serie.objects.get(slug2 = kwargs['slug_serie'])
		temporadas = Temporada.objects.filter(serie = serie).order_by('orden')
		capitulos = []
		for temporada in temporadas:
			capitulos.append(Capitulo.objects.filter(temporada=temporada).order_by('orden'))
		context['lista_capitulos'] = zip(temporadas, capitulos)
		context['serie'] = serie
		return context


class SerieDetailView(TemplateView):

	template_name = 'videos/series_detail.html'

	def get_context_data(self, **kwargs):
		context = super(SerieDetailView, self).get_context_data(**kwargs)
		capitulo = Capitulo.objects.get(slug = kwargs['slug_capitulo'])
		context['serie'] = capitulo.temporada.serie
		context['capitulo'] = capitulo
		return context