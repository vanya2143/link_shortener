from django.http import Http404
from rest_framework.reverse import reverse

from shortener.models import Link


class GetObjectMixin:
    def get_object(self, short_url):
        try:
            return Link.objects.get(short_url=short_url)
        except Link.DoesNotExists:
            raise Http404


class GetObjectReverseUrlMixin:
    def get_reversed_url(self, view_name, url_hash, request):
        return reverse(view_name, args=[url_hash], request=request)
