from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from apps.models import MainPage, QuoteRequest, ChooseXpress, Overview, Stats, FAQ, MainAbout
from apps.models.main_model import SimpleSteps
from apps.serializers import MainPageModelSerializer, DirectlyContactSerializer, SimpleContactSerializer, \
    SimpleStepsModelSerializer, ChooseXpressModelSerializer, OverviewModelSerializer, StatsModelSerializer, \
    FAQModelSerializer, MainAboutModelSerializer


@extend_schema(tags=["main"])
class MainPageListAPIView(ListAPIView):
    queryset = MainPage.objects.all()
    serializer_class = MainPageModelSerializer
    permission_classes = (AllowAny,)


@extend_schema(tags=["main"])
class SimpleStepsListAPIView(ListAPIView):
    queryset = SimpleSteps.objects.all()
    serializer_class = SimpleStepsModelSerializer
    permission_classes = (AllowAny,)


@extend_schema(tags=["main"])
class MainAboutListAPIView(ListAPIView):
    queryset = MainAbout.objects.all()
    serializer_class = MainAboutModelSerializer
    permission_classes = (AllowAny,)


@extend_schema(tags=["main"])
class OverviewListAPIView(ListAPIView):
    queryset = Overview.objects.all()
    serializer_class = OverviewModelSerializer
    permission_classes = (AllowAny,)


@extend_schema(tags=["main"])
class SimpleListAPIView(ListAPIView):
    queryset = QuoteRequest.objects.filter(contact_type=QuoteRequest.Contacts.SIMPLE_CONTACT)
    serializer_class = SimpleContactSerializer
    permission_classes = (AllowAny,)


@extend_schema(tags=["main"])
class FaqFrequentlyListAPIView(ListAPIView):
    queryset = FAQ.objects.filter(category=FAQ.Choose.FREQUENTLY)
    serializer_class = FAQModelSerializer


@extend_schema(tags=["contact"])
class DirectlyContactListAPIView(ListCreateAPIView):
    queryset = QuoteRequest.objects.filter(contact_type=QuoteRequest.Contacts.DIRECTLY_CONTACT)
    serializer_class = DirectlyContactSerializer
    permission_classes = (AllowAny,)


@extend_schema(tags=["main-about"])
class StatsListCreate(ListCreateAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatsModelSerializer
    permission_classes = (AllowAny,)


@extend_schema(tags=["main-about"])
class ChooseXpressListAPIView(ListAPIView):
    queryset = ChooseXpress.objects.all()
    serializer_class = ChooseXpressModelSerializer
    permission_classes = (AllowAny,)
