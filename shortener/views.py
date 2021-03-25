import csv

from django.http import Http404
from django.http.response import HttpResponseRedirect, HttpResponse
from django.views.generic.base import View

from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Link
from .serializers import LinkSerializer
from .mixins import CustomCreateModelMixin


class LinkList(CustomCreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LinkDetail(APIView):
    def get_object(self, hash):
        try:
            return Link.objects.get(hash=hash)
        except Link.DoesNotExists:
            raise Http404

    def get(self, request, hash):
        link = self.get_object(hash)
        # return Response({'link': link.destination_link})
        return HttpResponseRedirect(redirect_to=link.url)

    def delete(self, request, hash):
        link = self.get_object(hash)
        link.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExportView(View):
    def get(self, request):
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
