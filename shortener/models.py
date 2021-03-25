from hashlib import sha256
from time import time

from django.db import models


class Link(models.Model):
    hash = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    def create_source_link(self):
        url = str.encode(self.url + str(time()))
        return sha256(url).hexdigest()[:8]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.hash = self.create_source_link()
        super().save(*args, **kwargs)
