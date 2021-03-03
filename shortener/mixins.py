from django.http import Http404

from shortener.models import Link


class GetObjectMixin:
    def get_object(self, url_hash):
        try:
            return Link.objects.get(hash=url_hash)
        except Link.DoesNotExists:
            raise Http404
