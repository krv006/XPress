from django.db.models import Model, CharField, ImageField
from django_ckeditor_5.fields import CKEditor5Field


class About(Model):
    title = CKEditor5Field()
    image = ImageField(upload_to='about/images/')
    description = CKEditor5Field()

    class Meta:
        verbose_name = 'About us'
        verbose_name_plural = 'About us'

# todo Faq done and Home page Frequently
class FAQ(Model):
    title = CharField()
    description = CKEditor5Field()

    class Meta:
        verbose_name = 'FAQs'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return f' {self.title}'
