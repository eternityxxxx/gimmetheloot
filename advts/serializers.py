from rest_framework import serializers

from .models import Advert, AdvertImage


class AdvertImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdvertImage
        fields = ('image', 'advert')


class AdvertSerializer(serializers.ModelSerializer):

    # images = serializers.ImageField()

    class Meta:
        model = Advert
        fields = ['id', 'title', 'description', 'price', 'address', ]
        read_only_fields = ('created_at', 'updated_at')
        depth = 1

    # def create(self, validated_data):
    #
    #     images = validated_data.pop('images')
    #
    #     advert = super().create(validated_data)
    #
    #     for image in images:
    #         serializer = AdvertImageSerializer(data={'image': image, 'advert': advert.pk})
    #         serializer.is_valid()
    #         serializer.save()
    #
    #     return advert
