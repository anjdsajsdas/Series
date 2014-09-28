from django.db import models
from django.template.defaultfilters import slugify

class Serie(models.Model):

	name = models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	image = models.ImageField(upload_to = 'serie')
	slug = models.SlugField(editable=False)
	slug2 = models.SlugField(max_length=100)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super(Serie, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

class Temporada(models.Model):

	serie = models.ForeignKey(Serie)
	name = models.CharField(max_length=50)
	orden = models.PositiveIntegerField()

	def __unicode__(self):
		return "%s - %s" % (self.serie.name, self.name)

class Capitulo(models.Model):

	temporada = models.ForeignKey(Temporada)
	name = models.CharField(max_length=50)
	video = models.CharField(max_length=50)
	orden = models.PositiveIntegerField()
	slug = models.SlugField(null=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.id:
			capitulo = "%s capitulo %s temporada %s" % ( self.temporada.serie.name, self.orden, self.temporada.orden)
			self.slug = slugify(capitulo)
		super(Capitulo, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

