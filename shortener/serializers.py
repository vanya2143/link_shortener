from rest_framework import serializers

from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    short_url = serializers.HyperlinkedIdentityField(
        view_name='link-detail',
        lookup_field='hash',
    )

    class Meta:
        model = Link
        fields = ['id', 'url', 'short_url']

