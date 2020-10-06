from django.contrib import admin
from .models import *

class ModelPost(admin.ModelAdmin):
    list_display = ['title', 'created_on']


class ModelCategory(admin.ModelAdmin):
    pass


admin.site.register(Post, ModelPost)
admin.site.register(Category, ModelCategory)
admin.site.register(Comment)