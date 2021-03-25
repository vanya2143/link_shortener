from rest_framework import serializers

from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    short_link = serializers.HyperlinkedIdentityField(
        view_name='link-detail',
        lookup_field='hash',
    )

    class Meta:
        model = Link
        fields = ['id', 'destination_link', 'short_link']

