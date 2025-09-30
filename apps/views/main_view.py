from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from apps.models import MainPage, QuoteRequest
from apps.models.main_model import SimpleSteps
from apps.serializers import MainPageModelSerializer, DirectlyContactSerializer, SimpleContactSerializer, \
    SimpleStepsModelSerializer


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
class SimpleContactListAPIView(ListCreateAPIView):
    queryset = QuoteRequest.objects.filter(contact_type=QuoteRequest.Contacts.SIMPLE_CONTACT)
    serializer_class = SimpleContactSerializer
    permission_classes = (AllowAny,)


@extend_schema(tags=["contact"])
class DirectlyContactListAPIView(ListCreateAPIView):
    queryset = QuoteRequest.objects.filter(contact_type=QuoteRequest.Contacts.DIRECTLY_CONTACT)
    serializer_class = DirectlyContactSerializer
    permission_classes = (AllowAny,)
