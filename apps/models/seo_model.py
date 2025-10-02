from django.db.models import Model, CharField


class Seo(Model):
    title = CharField(max_length=1000)

