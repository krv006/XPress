from django.core.validators import MinLengthValidator, RegexValidator
from django.db.models import Model, CharField, TextField, SlugField, ImageField, DateTimeField
from django_ckeditor_5.fields import CKEditor5Field

slug_validator = RegexValidator(
    regex=r'^[A-Za-z0-9_]+$',
    message="Slug may contain only letters, digits, and underscores."
)


def title_logo_upload_to(instance, filename):
    return f"pages/{instance.slug or 'no-slug'}/{filename}"


class Seo(Model):
    title = CharField(max_length=1000)
    description = CKEditor5Field()
    keywords = CharField(max_length=1000)


class Page(Model):
    title = CharField(max_length=256, validators=[MinLengthValidator(1)])
    content = TextField(validators=[MinLengthValidator(1)])
    slug = SlugField(
        max_length=50, unique=True, validators=[slug_validator, MinLengthValidator(1)],
        help_text="Only letters, digits, and underscores."
    )
    title_logo = ImageField(
        upload_to=title_logo_upload_to, blank=True, null=True,
        help_text="Title logo image (URL will be read-only in API)."
    )

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    @property
    def title_logo_url(self):
        return self.title_logo.url if self.title_logo else None

    def __str__(self):
        return self.title
