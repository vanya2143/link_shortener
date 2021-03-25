from hashlib import sha256
from time import time
import csv

from django.http import HttpResponse
from django.views import View
from django.http.response import HttpResponseRedirect

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.reverse import reverse

from .models import Link
from .serializers import LinkSerializer
from .mixins import GetObjectMixin, GetObjectReverseUrlMixin


def create_url_hash(url):
    url = str.encode(url + str(time()))
    return sha256(url).hexdigest()[:8]


class LinkList(GetObjectMixin, APIView):
    def get(self, request):
        links = Link.objects.all()
        serializer = LinkSerializer(links, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            url_hash = create_url_hash(serializer.validated_data.get('url'))
            short_url = reverse('link-detail', args=[url_hash], request=request)

            serializer.save(short_url=short_url)

            response = {
                'short_url': serializer.data.get('short_url')
            }

            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LinkRedirectView(GetObjectReverseUrlMixin, GetObjectMixin, APIView):
    def get(self, request, url_hash):
        link = self.get_object(self.get_reversed_url('link-detail', url_hash, request))
        return HttpResponseRedirect(redirect_to=link.url)

    def delete(self, request, url_hash):
        link = self.get_object(self.get_reversed_url('link-detail', url_hash, request))
        link.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExportView(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="links.csv"'

        _urls = Link.objects.values_list('url', 'short_url')

        writer = csv.writer(response)
        writer.writerow(['url', 'short_url'])

        for url in _urls:
            writer.writerow(url)

        return response
