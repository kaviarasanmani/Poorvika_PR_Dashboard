from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Release_order,Pub_date,R_edition

admin.site.register(Release_order),
admin.site.register(Pub_date),
admin.site.register(R_edition),

