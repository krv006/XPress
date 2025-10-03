from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from apps.models import Seo, Page
from apps.serializers import SeoModelSerializer, PageModelSerializer


@extend_schema(tags=["seo"])
class SeoListAPIView(ListAPIView):
    queryset = Seo.objects.all()
    serializer_class = SeoModelSerializer
    permission_classes = (AllowAny,)


@extend_schema(tags=["page"])
class PageListAPIView(ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageModelSerializer
    permission_classes = (AllowAny,)
