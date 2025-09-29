from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView

from apps.models import About, FAQ
from apps.serializers.about_serializer import AboutModelSerializer, FAQModelSerializer


@extend_schema(tags=["about"])
class AboutListAPIView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutModelSerializer


@extend_schema(tags=["about"])
class FAQListAPIView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQModelSerializer
