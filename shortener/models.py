from hashlib import sha256

from django.db import models


class Link(models.Model):
    hash = models.CharField(max_length=250)
    destination_link = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    def create_source_link(self):
        url = str.encode(self.destination_link)
        return sha256(url).hexdigest()[:8]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.hash = self.create_source_link()
        super().save(*args, **kwargs)
