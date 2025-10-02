from django.db.models import Model, ImageField, CharField, DateTimeField, PositiveIntegerField, ForeignKey, \
    CASCADE, FloatField, PositiveSmallIntegerField
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


class ReviewSource(Model):
    name = CharField(max_length=100, help_text="Transport Reviews, Trustpilot, BBB")
    average_rating = FloatField(help_text="5.0, 4.2, 4.28")
    total_reviews = PositiveIntegerField(help_text="14, 49, 32")

    def __str__(self):
        return f"{self.name} ({self.average_rating} / 5)"


class ReviewBreakdown(Model):
    source = ForeignKey(ReviewSource, on_delete=CASCADE, related_name="breakdowns")
    stars = PositiveSmallIntegerField(help_text="1–5")
    percentage = FloatField(help_text="100.0, 86.0, 12.0")
    count = PositiveIntegerField(default=0, help_text="Costumers soni (14, 49, 32)")

    def __str__(self):
        return f"{self.stars} stars - {self.percentage}%"
