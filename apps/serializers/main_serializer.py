from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.models import MainPage,  QuoteRequest


class MainPageModelSerializer(ModelSerializer):
    class Meta:
        model = MainPage
        fields = '__all__'


class QuoteRequestModelSerializer(ModelSerializer):
    class Meta:
        model = QuoteRequest
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('by_checking') is False:
            raise ValidationError("Tasdiqlanmagan: submit qilish mumkin emas!")
        return attrs
