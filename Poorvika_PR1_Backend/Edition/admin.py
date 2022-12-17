from django.contrib import admin
from .models import Publication,Edition,State,District,Edition_save
from import_export.admin import ImportExportModelAdmin

# 


class PublicationAdmin(ImportExportModelAdmin):
        
    class Meta:
        model =Publication()
        Field = ('id',)


admin.site.register(Publication, PublicationAdmin)

class EditionAdmin(ImportExportModelAdmin):
        
    class Meta:
        model =Edition()
        Field = ('id',)


admin.site.register(Edition, EditionAdmin)

class StateAdmin(ImportExportModelAdmin):
        
    class Meta:
        model =State()
        Field = ('id',)


admin.site.register(State, StateAdmin)


class DistrictAdmin(ImportExportModelAdmin):
        
    class Meta:
        model =District()
        Field = ('id',)


admin.site.register(District, DistrictAdmin)


admin.site.register(Edition_save)