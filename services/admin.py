from .models import *
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
class QueryResource(resources.ModelResource):

    class Meta:
        model = Query

# Register your models here.
class QueryAdmin(ImportExportModelAdmin):
    resource_class = QueryResource
admin.site.register(Query,QueryAdmin)