from django.contrib import admin
from .models import *


class ModelProject(admin.ModelAdmin):
    list_display = ['title']


class ModelCategory(admin.ModelAdmin):
    pass


admin.site.register(Project, ModelProject)
admin.site.register(Category, ModelCategory)
admin.site.register(Language)
admin.site.register(Certificate)
admin.site.register(Comment)
