from django.contrib import admin
from finalweb.models import *


class ImageInline(admin.TabularInline):
    model = RefImages
    extra = 0


class ReferenceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Quote)
admin.site.register(Reference, ReferenceAdmin)