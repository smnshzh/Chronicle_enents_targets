from django.contrib import admin
from .models import *
from import_export.admin import ExportActionMixin
class SalaLineAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ['code','name']
class ProductTargetGroupAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ["code","name"]
class CenterAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ["code","name"]
class CenterTargetDefindeAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ["center","month"]
class SuperviserAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ["code","name","center"]
class VisitorAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ["code","name","line","line2","cneter"]
    list_editable = ["name","line","line2","cneter"]
class SetVisitorTargetAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ["visitor","pgroup","qnty"]
admin.site.register(SaleLine,SalaLineAdmin)
admin.site.register(ProductTargetGroup,ProductTargetGroupAdmin)
admin.site.register(CenterD,CenterAdmin)
admin.site.register(CenterTargetDefinde,CenterTargetDefindeAdmin)
admin.site.register(Superviser,SuperviserAdmin)
admin.site.register(Visitor,VisitorAdmin)
admin.site.register(SetVisitorTarget,SetVisitorTargetAdmin)
admin.site.register(TargetAccess)

