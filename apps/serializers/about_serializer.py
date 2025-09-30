from rest_framework.serializers import ModelSerializer

from apps.models import About, FAQ


class AboutModelSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'title', 'description')


class FAQModelSerializer(ModelSerializer):
    class Meta:
        model = FAQ
        fields = 'id', 'title', 'description', 'category',
