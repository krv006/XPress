from django.contrib import admin
from django.contrib.admin import ModelAdmin
from import_export.admin import ExportMixin

from apps.models import Footer, Stats, Partners, BlogPost, About, FAQ, Overview, Review, Seo, Page, Stories, \
    TelegramConfig
from apps.models.main_model import MainPage, QuoteRequest, ChooseXpress
from apps.resources import MainPageResource


@admin.register(MainPage)
class MainPageModelAdmin(ExportMixin, ModelAdmin):
    resource_class = MainPageResource
    list_display = ('id', 'title', 'description')
    list_display_links = ("id", "title")
    search_fields = ("title", "description", "contact_us")
    ordering = ("id",)


@admin.register(ChooseXpress)
class ChooseXpressModelAdmin(ModelAdmin):
    pass


@admin.register(QuoteRequest)
class QuoteRequestModelAdmin(ModelAdmin):
    list_display = ("id", "title", "phone_number", "contact_type", "created_at",)
    list_display_links = ("id", "title")
    list_filter = ("contact_type",)
    search_fields = ("title", "phone_number")
    ordering = ("-created_at",)
    date_hierarchy = "created_at"
    list_per_page = 15


@admin.register(Footer)
class FooterModelAdmin(ModelAdmin):
    list_display = ('id', 'phone_number', 'address', 'gmail_link')
    list_display_links = ("id", "phone_number")
    search_fields = ("phone_number", "address")


@admin.register(Stats)
class StatsModelAdmin(ModelAdmin):
    pass


@admin.register(Partners)
class PartnersModelAdmin(ExportMixin, ModelAdmin):
    list_display = ('id', 'title')


@admin.register(About)
class AboutModelAdmin(ModelAdmin):
    pass


@admin.register(FAQ)
class FAQModelAdmin(ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title", "description")
    ordering = ("title",)
    list_per_page = 15


@admin.register(BlogPost)
class BlogPostAdmin(ExportMixin, ModelAdmin):
    list_display = ('id', 'title', 'views')
    search_fields = ('title',)
    autocomplete_fields = ()
    list_per_page = 15
    save_on_top = True


@admin.register(Stories)
class StoriesAdmin(ExportMixin, ModelAdmin):
    list_display = ('id', 'title', 'views')
    search_fields = ('title',)
    autocomplete_fields = ()
    list_per_page = 15
    save_on_top = True


@admin.register(TelegramConfig)
class TelegramConfigAdmin(admin.ModelAdmin):
    pass


admin.site.register(Overview)
admin.site.register(Review)
admin.site.register(Seo)
admin.site.register(Page)


admin.site.site_header = "XPress Management"
admin.site.site_title = "XPress Admin Portal"
admin.site.index_title = "XPress Dashboard"
