from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.models import BlogPost


class BlogModelSerializer(ModelSerializer):
    main_image_url = SerializerMethodField()
    published_date = SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = (
            'id',
            'title',
            'short_description',
            'published_date',
            'views',
            'main_image_url',
        )
        read_only_fields = ('views',)

    def get_main_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.main_image.url) if obj.main_image else None

    def get_published_date(self, obj):
        return obj.published_at.strftime('%B %d %Y') if obj.published_at else None


class BlogDetailModelSerializer(ModelSerializer):
    main_image_url = SerializerMethodField()
    back_image_url = SerializerMethodField()
    published_date = SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = '__all__'
        read_only_fields = ('views',)

    def get_main_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.main_image.url) if obj.main_image else None

    def get_back_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.back_image.url) if obj.back_image else None

    def get_published_date(self, obj):
        return obj.published_at.strftime('%B %d %Y') if obj.published_at else None
