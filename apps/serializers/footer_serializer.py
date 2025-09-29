from rest_framework.serializers import ModelSerializer

from apps.models import Footer,Partners, Stats


class FooterModelSerializer(ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'


class PartnerModelSerializer(ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'


class StatsModelSerializer(ModelSerializer):
    class Meta:
        model = Stats
        fields = '__all__'
