from rest_framework.serializers import ModelSerializer

from apps.models import Footer, Partners, Stats


class FooterModelSerializer(ModelSerializer):
    class Meta:
        model = Footer
        fields = 'phone_number', 'address', 'gmail_link', 'instagram_link', 'facebook_link', 'youtube_link',


class ContactOptionModelSerializer(ModelSerializer):
    class Meta:
        model = Footer
        fields = 'id', 'address', 'gmail_link', 'phone_number',


class PartnerModelSerializer(ModelSerializer):
    class Meta:
        model = Partners
        fields = 'id', 'title', 'image',



