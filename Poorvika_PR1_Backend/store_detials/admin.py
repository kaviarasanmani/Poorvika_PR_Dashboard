from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class ShowRoomAdmin(ImportExportModelAdmin):

    class Meta:
        model = ShowRoom
        Field = ('id','location')


admin.site.register(ShowRoom, ShowRoomAdmin)


class StoreAdmin(ImportExportModelAdmin):

    class Meta:
        model = Store
        Field = ("ID","D_CODE",'ShowRoom','Type','Flate_House_No',
                 'Stree_Building_Name','LandMark','Pincode',
                 'Area','Taluk','District','State','Status',
                 'DOB','Closed')


admin.site.register(Store,StoreAdmin)


class Employee_masteAdmin(ImportExportModelAdmin):
    class Meta:
        model = Employee_master
        Field = (
                'Emp_ID','Full_Name','Designation','Work_Area','Sub_Regions'
                'Location_Type','Work_Area_Code','Office_City','Office_State','Region'
                'Department_Code','Department','Gender','Date_of_Birth','Employee_Type'
                 )


admin.site.register(Employee_master, Employee_masteAdmin)


class PublicationAdmin(ImportExportModelAdmin):
    class Meta:
        model = Publication
        field =(
            'pub_name'
        )


admin.site.register(Publication, PublicationAdmin)


class EditionAdmin(ImportExportModelAdmin):
    class Meta:
        model = Edition
        field = (
            'name'
        )


admin.site.register(Edition, EditionAdmin)


class PageAdmin(ImportExportModelAdmin):
    class Meta:
        model = Page
        field = (
            'name'
        )


admin.site.register(Page, PageAdmin)


class LayoutAdmin(ImportExportModelAdmin):
    class Meta:
        model = Layout
        field = (
            'name'
        )


admin.site.register(Layout, LayoutAdmin)


class BrandAdmin(ImportExportModelAdmin):
    class Meta:
        model = Brand
        field = (
            'name'
        )


admin.site.register(Brand, BrandAdmin)

admin.site.register(EditionSave)