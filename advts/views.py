from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Advert
from .serializers import AdvertSerializer


class AdvertList(ListCreateAPIView):

    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer


class AdvertDelete(RetrieveUpdateDestroyAPIView):

    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
