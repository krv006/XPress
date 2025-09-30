from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.models import MainPage, QuoteRequest
from apps.serializers import MainPageModelSerializer, QuoteRequestModelSerializer


@extend_schema(tags=["main"])
class MainPageListCreate(ListCreateAPIView):
    queryset = MainPage.objects.all()
    serializer_class = MainPageModelSerializer
    permission_classes = (AllowAny,)


@extend_schema(tags=["main"])
class QuoteRequestListCreate(ListCreateAPIView):
    queryset = QuoteRequest.objects.all()
    serializer_class = QuoteRequestModelSerializer
    permission_classes = (AllowAny,)
