from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from apps.models import Seo, Page, CustomerReview, TransportPrice
from apps.serializers import SeoModelSerializer, PageModelSerializer, CustomerReviewModelSerializer, \
    TransportPriceModelSerializer


@extend_schema(tags=["seo"])
class SeoListAPIView(ListAPIView):
    queryset = Seo.objects.all()
    serializer_class = SeoModelSerializer
    permission_classes = (AllowAny,)


@extend_schema(tags=["seo"])
class PageListAPIView(ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageModelSerializer
    permission_classes = (AllowAny,)


@extend_schema(tags=["seo"])
class TransportPriceListAPIView(ListAPIView):
    queryset = TransportPrice.objects.all()
    serializer_class = TransportPriceModelSerializer
    permission_classes = (AllowAny,)


@extend_schema(tags=["seo"])
class CustomerReviewListAPIView(ListAPIView):
    queryset = CustomerReview.objects.all()
    serializer_class = CustomerReviewModelSerializer
    permission_classes = (AllowAny,)
