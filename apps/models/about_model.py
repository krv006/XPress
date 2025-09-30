from django.db.models import Model, CharField
from django.db.models.enums import TextChoices
from django_ckeditor_5.fields import CKEditor5Field


class About(Model):
    title = CKEditor5Field()
    description = CKEditor5Field()


# todo Faq done and Home page Frequently
class FAQ(Model):
    class Choose(TextChoices):
        FAQ = 'faq', 'Faq'
        FREQUENTLY = 'frequently', 'Frequently'

    title = CharField()
    description = CKEditor5Field()
    category = CharField(max_length=255, choices=Choose.choices)

    def __str__(self):
        return f'{self.category} {self.title}'
