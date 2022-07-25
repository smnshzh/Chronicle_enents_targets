from django.contrib import admin
from .models import *
from import_export.admin import ExportActionMixin
# Register your models here.
class ProductInfoAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ["code1","name","group"]
admin.site.register(ProductGroup)
admin.site.register(ProductInfo,ProductInfoAdmin)
admin.site.register(CarInfo)
admin.site.register(MainGroup)
