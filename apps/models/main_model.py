from django.db.models import Model, CharField, BooleanField, TextField, DateTimeField, ImageField
from django.db.models.enums import TextChoices
from django.db.models.fields import PositiveIntegerField
from django_ckeditor_5.fields import CKEditor5Field


# todo Reliable Door-to-Door
class MainPage(Model):
    title = CharField(max_length=500)
    description = CKEditor5Field()
    contact_us = CharField(max_length=100, help_text='Misol uchun: (929) 566-5040')

    class Meta:
        verbose_name = 'Main Page'
        verbose_name_plural = 'Main Page'

class QuoteRequest(Model):
    class Contacts(TextChoices):
        DIRECTLY_CONTACT = 'directly_contact', 'Directly_Contact'
        SIMPLE_CONTACT = 'simple_contact', 'Simple_Contact'

    title = CharField(max_length=500)
    phone_number = CharField(max_length=100, help_text='Misol uchun: (123) 456-7891')
    message = TextField(blank=True, null=True)
    contact_type = CharField(max_length=255, choices=Contacts.choices)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.phone_number}"


# todo Why Choose Xpress Auto Transportation?
class ChooseXpress(Model):
    title = CharField(max_length=500)
    description = CKEditor5Field()

    class Meta:
        verbose_name = 'Why choose us'
        verbose_name_plural = 'Why choose us'

# todo What Makes Us Stand Out?
class Overview(Model):
    description = CKEditor5Field()


# todo Simple Steps
class SimpleSteps(Model):
    title = CharField(max_length=500)
    description = CKEditor5Field()


class Stats(Model):
    title = CharField(max_length=100, default="Cars Transported")
    count = PositiveIntegerField(default=0)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}: {self.count}+"

    class Meta:
        verbose_name = 'Statistics'
        verbose_name_plural = 'Statistics'

class MainAbout(Model):
    title = CharField(max_length=500)
    image = ImageField(upload_to='main_about/images/')
    description = CKEditor5Field()
