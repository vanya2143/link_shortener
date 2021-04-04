from hashlib import sha256
from time import time
import re

from django.db import models

pattern = re.compile(r'http?.:(?:\/\/127\.0{0,3}\.0{0,3}.0{0,2}1:\d)?(?:([A-Za-z]+):)?(\/{0,3})([0-9.\-A-Za-z]+)')


def get_site_name(url):
    return pattern.match(url).group()


class Link(models.Model):
    hash = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    def create_source_link(self):
        url = str.encode(self.url + str(time()))
        return sha256(url).hexdigest()[:8]

    def __str__(self):
        return f'{self.hash} to {get_site_name(self.url)}'

    def save(self, *args, **kwargs):
        self.hash = self.create_source_link()
        super().save(*args, **kwargs)
