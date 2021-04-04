import csv

from django.http.response import HttpResponseRedirect, HttpResponse

from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from .models import Link
from .serializers import LinkSerializer


class LinkViewSet(ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    lookup_field = 'hash'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return HttpResponseRedirect(redirect_to=serializer.data.get('url'))

    @action(detail=False, name='export')
    def export(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="links.csv"'

        urls = Link.objects.all()

        serializer = LinkSerializer(urls, context={'request': request}, many=True)
        urls_gen = ((x.get('short_url'), x.get('url')) for x in serializer.data)

        writer = csv.writer(response)
        writer.writerow(['short_url', 'url'])

        for url in urls_gen:
            writer.writerow(url)

        return response
