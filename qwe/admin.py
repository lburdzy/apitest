from django.contrib import admin
from .models import Foo
from django.utils.text import slugify


class FooAdmin(admin.ModelAdmin):
    exclude = ('slug', )

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(str(obj.id) + '-' + obj.name)
        obj.save()


admin.site.register(Foo, FooAdmin)
