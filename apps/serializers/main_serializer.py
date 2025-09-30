from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.models import MainPage, QuoteRequest, Overview
from apps.models.main_model import ChooseXpress, SimpleSteps


class MainPageModelSerializer(ModelSerializer):
    class Meta:
        model = MainPage
        fields = 'id', 'title', 'description', 'contact_us',


class ChooseXpressModelSerializer(ModelSerializer):
    class Meta:
        model = ChooseXpress
        fields = 'id', 'title', 'description',


class OverviewModelSerializer(ModelSerializer):
    class Meta:
        model = Overview
        fields = 'id', 'description',


class SimpleStepsModelSerializer(ModelSerializer):
    class Meta:
        model = SimpleSteps
        fields = 'id', 'title', 'description',


class DirectlyContactSerializer(ModelSerializer):
    class Meta:
        model = QuoteRequest
        fields = [
            "id",
            "title",
            "phone_number",
            "by_checking",
            "message",
            "contact_type",
            "created_at",
        ]

    def validate(self, attrs):
        if attrs.get('by_checking') is False:
            raise ValidationError("Tasdiqlanmagan: submit qilish mumkin emas!")
        return attrs


class SimpleContactSerializer(ModelSerializer):
    class Meta:
        model = QuoteRequest
        fields = [
            "id",
            "title",
            "phone_number",
            "by_checking",
            "contact_type",
            "created_at",
        ]

    def validate(self, attrs):
        if attrs.get('by_checking') is False:
            raise ValidationError("Tasdiqlanmagan: submit qilish mumkin emas!")
        return attrs
