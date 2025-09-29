from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.models import Footer, Partners, Stats
from apps.serializers.footer_serializer import FooterModelSerializer, PartnerModelSerializer, \
    StatsModelSerializer


@extend_schema(tags=["footer"])
class FooterListCreate(ListCreateAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterModelSerializer
    permission_classes = (AllowAny,)


@extend_schema(tags=["footer"])
class PartnerListCreate(ListCreateAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnerModelSerializer
    permission_classes = (AllowAny,)


@extend_schema(tags=["footer"])
class StatsListCreate(ListCreateAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatsModelSerializer
    permission_classes = (AllowAny,)
