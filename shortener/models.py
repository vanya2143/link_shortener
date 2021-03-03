from django.db import models


class Link(models.Model):
    hash = models.CharField(max_length=250, unique=True, db_index=True)
    url = models.CharField(max_length=250)
    short_url = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

