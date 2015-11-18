from django.db import models


class Foo(models.Model):
    # dla ujednolicenia nazwy pol zapisane zostaly po angielsku
    # pole id pozostawilem domyslnie
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name
