from rest_framework.serializers import ModelSerializer

from apps.models import Seo, Page


class SeoModelSerializer(ModelSerializer):
    class Meta:
        model = Seo
        fields = '__all__'


class PageModelSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'
