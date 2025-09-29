from django.db.models import F
from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.models import BlogPost
from apps.serializers.blog_serializer import BlogModelSerializer, BlogDetailModelSerializer


@extend_schema(tags=["blog"])
class BlogListAPIView(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogModelSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return BlogPost.objects.order_by('-id')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        BlogPost.objects.filter(pk=instance.pk).update(views=F('views') + 1)
        instance.refresh_from_db(fields=['views'])
        serializer = self.get_serializer(instance, context={"request": request})
        return Response(serializer.data)


@extend_schema(tags=["blog"])
class BlogDetailListAPIView(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogDetailModelSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return BlogPost.objects.order_by('-id')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        BlogPost.objects.filter(pk=instance.pk).update(views=F('views') + 1)
        instance.refresh_from_db(fields=['views'])
        serializer = self.get_serializer(instance, context={"request": request})
        return Response(serializer.data)