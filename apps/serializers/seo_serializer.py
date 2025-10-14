from rest_framework.serializers import ModelSerializer

from apps.models import Seo, Page, TransportPrice, CustomerReview


class SeoModelSerializer(ModelSerializer):
    class Meta:
        model = Seo
        fields = '__all__'


class PageModelSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'


class TransportPriceModelSerializer(ModelSerializer):
    class Meta:
        model = TransportPrice
        fields = '__all__'


class CustomerReviewModelSerializer(ModelSerializer):
    class Meta:
        model = CustomerReview
        fields = '__all__'
