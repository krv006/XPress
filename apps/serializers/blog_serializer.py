from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.models import BlogPost, ReviewSource, ReviewBreakdown



class BlogModelSerializer(ModelSerializer):
    published_date = SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = '__all__'
        read_only_fields = ('views',)


    def get_published_date(self, obj):
        return obj.published_at.strftime('%B %d %Y') if obj.published_at else None


class ReviewBreakdownSerializer(ModelSerializer):
    class Meta:
        model = ReviewBreakdown
        fields = ("id", "source", "stars", "percentage", "count")


class ReviewSourceSerializer(ModelSerializer):
    breakdowns = ReviewBreakdownSerializer(many=True, read_only=True)

    class Meta:
        model = ReviewSource
        fields = ("id", "name", "average_rating", "total_reviews", "breakdowns")
