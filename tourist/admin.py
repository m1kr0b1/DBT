from django.contrib import admin
from django import forms
from .models import Tours, Locations, Photos, PlaceLocations, Information

class ToursAdminForm(forms.ModelForm):

    class Meta:
        model = Tours
        fields = '__all__'


class ToursAdmin(admin.ModelAdmin):
    form = ToursAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'Tags', 'Photo', 'Description', 'Duration']


admin.site.register(Tours, ToursAdmin)


class LocationsAdminForm(forms.ModelForm):

    class Meta:
        model = Locations
        fields = '__all__'


class LocationsAdmin(admin.ModelAdmin):
    form = LocationsAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'Photo', 'MainLocLat', 'MainLocLon', 'MainLocRad', 'Audio']

admin.site.register(Locations, LocationsAdmin)


class PhotosAdminForm(forms.ModelForm):

    class Meta:
        model = Photos
        fields = '__all__'


class PhotosAdmin(admin.ModelAdmin):
    form = PhotosAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'Photo']


admin.site.register(Photos, PhotosAdmin)


class PlaceLocationsAdminForm(forms.ModelForm):

    class Meta:
        model = PlaceLocations
        fields = '__all__'


class PlaceLocationsAdmin(admin.ModelAdmin):
    form = PlaceLocationsAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'Latitude', 'Longitude', 'Radius']


admin.site.register(PlaceLocations, PlaceLocationsAdmin)


class InformationAdminForm(forms.ModelForm):

    class Meta:
        model = Information
        fields = '__all__'


class InformationAdmin(admin.ModelAdmin):
    form = InformationAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'Photo', 'Description']


admin.site.register(Information, InformationAdmin)


