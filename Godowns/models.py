from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.manager import Manager
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models as gismodels
#from django.contrib.gis.db.models.manager import GeoManager

# Create your models here.

Food = (
	('wheat','WHEAT'),
	('rice','RICE'),
	('jowar','JOWAR'),
	('soyabean','SOYABEAN'),
	('turdal','TUR_DAL'),
	)


class Godown(models.Model):
	Name = models.CharField(max_length=200)
	City = models.CharField(max_length=200)
	Food_Type = models.CharField(max_length=100, choices=Food)
	Capacity = models.IntegerField()
	Location = models.PointField(srid=4326)

	objects = GeoManager();
	
	def __unicode__(self):
		return self.name

class Meta:
	verbose_name_plural ="Godown"



class Storage(models.Model):
	Name_of_Godown = models.CharField(max_length=200)
	Food_Type = models.CharField(max_length=100, choices=Food)
	Total_Capacity = models.IntegerField()
	Filled = models.IntegerField()
	Remaining = models.IntegerField()
	City = models.CharField(max_length=200)

	objects = GeoManager();
	godown = models.ForeignKey(Godown, null=True, on_delete= models.SET_NULL)


	def __unicode__(self):
		return self.name


class Meta:
	verbose_name_plural ="Storage"