from django.contrib import admin
from import_export.admin import ExportActionMixin
from events.models import *

class CenterAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ["code","name"]

class EventAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ["title","affected","effectedList","date","firstAccept","secendAccept"]

admin.site.register(Center,CenterAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Access)




