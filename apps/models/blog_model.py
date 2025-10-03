from django.db.models import Model, ImageField, CharField, DateTimeField, PositiveIntegerField, \
    PositiveSmallIntegerField, DecimalField, ForeignKey, CASCADE
from django.db.models import URLField
from django_ckeditor_5.fields import CKEditor5Field


class BlogPost(Model):
    title = CharField(max_length=500)
    main_image = ImageField(upload_to="blog/main/", null=True, blank=True)
    description = CKEditor5Field()
    body = CKEditor5Field()
    link = URLField(null=True, blank=True)
    views = PositiveIntegerField(
        default=0, help_text="Kategoriya necha marta ko‘rilganligini ko‘rsatadi.")
    created = DateTimeField(auto_now_add=True)
    seo = ForeignKey('apps.Seo', CASCADE, related_name='blog_posts')


class Star(Model):
    title = CharField(max_length=500)
    costumers_rating = PositiveSmallIntegerField(help_text="14, 45, 150")
    average_rating = DecimalField(max_digits=3, decimal_places=1, help_text="O‘rtacha baho (masalan: 4.9)")
    stars_5 = PositiveIntegerField(default=0)
    stars_4 = PositiveIntegerField(default=0)
    stars_3 = PositiveIntegerField(default=0)
    stars_2 = PositiveIntegerField(default=0)
    stars_1 = PositiveIntegerField(default=0)
