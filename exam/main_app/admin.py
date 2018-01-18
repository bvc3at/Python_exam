from django.contrib import admin

from main_app import models

# Register your models here.
admin.site.register(models.Product)
admin.site.register(models.ProductVersion)
admin.site.register(models.ProductAndCount)
admin.site.register(models.Cart)
admin.site.register(models.Order)
