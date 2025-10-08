from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.models import BlogPost, Review, Stories


class BlogModelSerializer(ModelSerializer):
    published_date = SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = '__all__'
        read_only_fields = ('views',)

    def get_published_date(self, obj):
        return obj.published_at.strftime('%B %d %Y') if obj.published_at else None


class ReviewModelSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class StoriesModelSerializer(ModelSerializer):
    published_date = SerializerMethodField()

    class Meta:
        model = Stories
        fields = '__all__'
        read_only_fields = ('views',)

    def get_published_date(self, obj):
        return obj.published_at.strftime('%B %d %Y') if obj.published_at else None
