from django.http import Http404
from django.http.response import HttpResponseRedirect

from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Link
from .serializers import LinkSerializer


class LinkList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
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
        return HttpResponseRedirect(redirect_to=link.destination_link)

    def delete(self, request, hash):
        link = self.get_object(hash)
        link.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
