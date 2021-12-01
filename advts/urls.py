from django.urls import path

from .views import AdvertList, AdvertDelete


urlpatterns = [
    path('adverts/', AdvertList.as_view()),
    path('advert/<int:pk>/', AdvertDelete.as_view())
]
