from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from django.core.files import File as FileWrapper


from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor

class Tours(models.Model):

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True)
    last_updated = DateTimeField(auto_now=True)
    Tags = TextField(max_length=100)
    Photo = ImageField(upload_to="/home/ognen/Downloads/project_name/uploads/images")
    Description = TextField(max_length=2000)
    Duration = IntegerField()
    locations = models.ManyToManyField(Locations, related_name='tours')

    # Relationship Fields
    #Locations = models.ForeignKey('tourist.Locations', )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('app_name_tours_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('app_name_tours_update', args=(self.slug,))


class Locations(models.Model):

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True)
    last_updated = DateTimeField(auto_now=True)
    Photo = ImageField(upload_to="/home/ognen/Downloads/project_name/uploads/images")
    MainLocLat = TextField(max_length=100)
    MainLocLon = TextField(max_length=100)
    MainLocRad = TextField(max_length=100)
    Audio = FileField(upload_to="/home/ognen/Downloads/project_name/uploads/audio")
    Description = TextField(max_length=2000)

    Photos = models.ForeignKey('tourist.Photos', )
    PlaceLocations = models.ForeignKey('tourist.PlaceLocations', )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('app_name_locations_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('app_name_locations_update', args=(self.slug,))


class Photos(models.Model):

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True)
    last_updated = DateTimeField(auto_now=True)
    Photo = ImageField(upload_to="/home/ognen/Downloads/project_name/uploads/images")


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('tourist_photos_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('tourist_photos_update', args=(self.slug,))


class PlaceLocations(models.Model):

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True)
    last_updated = DateTimeField(auto_now=True)
    Latitude = TextField(max_length=100)
    Longitude = TextField(max_length=100)
    Radius = IntegerField()


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('app_name_placelocations_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('app_name_placelocations_update', args=(self.slug,))


class Information(models.Model):

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True)
    last_updated = DateTimeField(auto_now=True)
    Photo = ImageField(upload_to="/home/ognen/Downloads/project_name/uploads/images")
    Description = TextField(max_length=2000)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('tourist_information_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('tourist_information_update', args=(self.slug,))


# Create your models here.
