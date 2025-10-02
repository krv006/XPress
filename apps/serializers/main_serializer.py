from rest_framework.fields import DateTimeField
from rest_framework.serializers import ModelSerializer

from apps.models import MainPage, QuoteRequest, Overview, Stats, MainAbout
from apps.models.main_model import ChooseXpress, SimpleSteps


class MainPageModelSerializer(ModelSerializer):
    class Meta:
        model = MainPage
        fields = 'id', 'title', 'description', 'contact_us',


class ChooseXpressModelSerializer(ModelSerializer):
    class Meta:
        model = ChooseXpress
        fields = 'id', 'title', 'description',


class MainAboutModelSerializer(ModelSerializer):
    class Meta:
        model = MainAbout
        fields = 'id', 'title', 'description', 'image',


class OverviewModelSerializer(ModelSerializer):
    class Meta:
        model = Overview
        fields = 'id', 'description',


class SimpleStepsModelSerializer(ModelSerializer):
    class Meta:
        model = SimpleSteps
        fields = 'id', 'title', 'description',


class StatsModelSerializer(ModelSerializer):
    class Meta:
        model = Stats
        fields = 'id', 'title', 'count',


class DirectlyContactSerializer(ModelSerializer):
    created_at = DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = QuoteRequest
        fields = [
            "id",
            "title",
            "phone_number",
            "message",
            "contact_type",
            "created_at",
        ]


class SimpleContactSerializer(ModelSerializer):
    created_at = DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = QuoteRequest
        fields = [
            "id",
            "title",
            "phone_number",
            "contact_type",
            "created_at",
        ]
