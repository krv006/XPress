from django.db.models import Model, ImageField, CharField, DateTimeField, PositiveIntegerField, SlugField, ForeignKey, \
    PROTECT, CASCADE, FloatField, PositiveSmallIntegerField
from django.db.models.fields import TextField
from django.db.models.indexes import Index
from django.utils import timezone
from django.utils.text import slugify


def cover_upload_to(instance, filename):
    return f"blog/{instance.slug or slugify(instance.title)}/{filename}"


def category_image_upload_to(instance, filename):
    slug = instance.slug or slugify(instance.title)
    return f"category/{slug}/{filename}"


class Category(Model):
    title = CharField(max_length=160, help_text="Kategoriya nomi yoki sarlavhasi (masalan: 'Car Shipment').")
    description = TextField(blank=True, help_text="Kategoriya uchun qisqa tavsif (kartochkada chiqadi).")
    image = ImageField(
        upload_to=category_image_upload_to, blank=True, null=True,
        help_text="Kategoriya uchun asosiy rasm (kartochka rasmi).")
    published_at = DateTimeField(default=timezone.now, help_text="Chop etilgan sana.")
    views = PositiveIntegerField(
        default=0, help_text="Kategoriya necha marta ko‘rilganligini ko‘rsatadi.")
    slug = SlugField(
        max_length=180, unique=True, blank=True, help_text="URL-friendly slug. Avtomatik generatsiya qilinadi.")

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return f'{self.title} {self.views}'

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:170]
            slug = base or "category"
            i = 2
            from django.apps import apps
            Category = apps.get_model(self._meta.app_label, self.__class__.__name__)
            while Category.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug
        return super().save(*args, **kwargs)


class BlogPost(Model):
    category = ForeignKey('apps.Category', PROTECT, related_name="posts")
    slug = SlugField(max_length=240, unique=True, blank=True)
    excerpt = TextField(blank=True, help_text="Rasm tepasidagi qisqa matn")
    body = TextField(help_text="To‘liq maqola")
    published_at = DateTimeField(default=timezone.now)
    views = PositiveIntegerField(default=0)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published_at"]
        indexes = [
            Index(fields=["-published_at"]),
            Index(fields=["slug"]),
        ]

    def __str__(self):
        return self.category.title

    def save(self, *args, **kwargs):

        if not self.slug:
            base = slugify(self.category.title)[:170]
            slug = base
            i = 2
            while BlogPost.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug

        return super().save(*args, **kwargs)


class BlogImage(Model):
    post = ForeignKey('apps.BlogPost', CASCADE, related_name="images")
    image = ImageField(upload_to='blog/image/')


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
