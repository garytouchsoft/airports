from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Airport


class AirportResource(resources.ModelResource):

    def get_instance(self, instance_loader, row):
        try:
            params = {}
            for key in instance_loader.resource.get_import_id_fields():
                field = instance_loader.resource.fields[key]
                params[field.attribute] = field.clean(row)
            return self.get_queryset().get(**params)
        except Exception:
            return None

    class Meta:
        model = Airport
        fields = ('name', 'icao', 'latitude', 'longitude')


class AirportAdmin(ImportExportModelAdmin):
    resource_class = AirportResource


admin.site.register(Airport, AirportAdmin)
