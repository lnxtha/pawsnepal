from django.contrib import admin
from .models import Pets, PetItems, Blog, Brand

from django_summernote.admin import SummernoteModelAdmin


class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('post',)


# Register your models here.

admin.site.register(Pets)
admin.site.register(PetItems)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Brand)
