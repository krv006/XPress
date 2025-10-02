from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from apps.models import BlogPost, Star
from apps.serializers import BlogModelSerializer, StarModelSerializer


@extend_schema(tags=["stars"])
class StarListAPIView(ListAPIView):
    queryset = Star.objects.all()
    serializer_class = StarModelSerializer


@extend_schema(tags=["blog"])
class BlogListAPIView(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogModelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = 'title',
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = BlogPost.objects.order_by('-id')
        BlogPost.objects.all().update(views=F('views') + 1)
        return queryset

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     BlogPost.objects.filter(pk=instance.pk).update(views=F('views') + 1)
    #     instance.refresh_from_db(fields=['views'])
    #     serializer = self.get_serializer(instance, context={"request": request})
    #     return Response(serializer.data)
