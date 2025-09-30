from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.models import BlogPost, Category, BlogImage


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def get_published_date(self, obj):
        return obj.published_at.strftime('%B %d %Y') if obj.published_at else None


class BlogImageModelSerializer(ModelSerializer):
    post = SerializerMethodField()

    class Meta:
        model = BlogImage
        fields = 'id', 'image', 'post',

    def get_post(self, obj):
        if obj.post:
            return {
                'id': obj.post.id,
                'title': obj.post.category.title,
                'views': obj.post.views,
            }


class BlogModelSerializer(ModelSerializer):
    images = BlogImageModelSerializer(many=True, read_only=True)  # <-- shu yer to‘g‘rilandi
    category = SerializerMethodField()
    published_date = SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = '__all__'
        read_only_fields = ('views',)

    def get_category(self, obj):
        if obj.category:
            return {
                'id': obj.category.id,
                'title': obj.category.title,
                'slug': obj.category.slug
            }
        return None

    def get_published_date(self, obj):
        return obj.published_at.strftime('%B %d %Y') if obj.published_at else None
