from django.db.models import Model, CharField, ImageField


class Footer(Model):
    phone_number = CharField(max_length=200, help_text='Footer uchun telefon raqam kiriting: (929) 566-5040')
    address = CharField(max_length=500)
    gmail_link = CharField(max_length=200, help_text='Gmail link')
    instagram_link = CharField(max_length=200, help_text='Instagram link')
    facebook_link = CharField(max_length=200, help_text='Facebook link')
    youtube_link = CharField(max_length=200, help_text='Youtube link')



class Partners(Model):
    title = CharField(max_length=255, null=True, blank=True, help_text='Name of partner')
    image = ImageField(upload_to='partners/')

    class Meta:
        verbose_name = 'Partners'
        verbose_name_plural = 'Partners'