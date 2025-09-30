from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from import_export.admin import ExportMixin

from apps.models import Footer, Stats, Partners, BlogPost, About, FAQ, BlogImage, Category
from apps.models.main_model import MainPage, QuoteRequest, ChooseXpress
from apps.resources import MainPageResource


class BlogImageInline(TabularInline):
    model = BlogImage
    extra = 3
    max_num = 15


@admin.register(MainPage)
class MainPageModelAdmin(ExportMixin, ModelAdmin):
    resource_class = MainPageResource
    list_display = ('id', 'title', 'description')


@admin.register(ChooseXpress)
class ChooseXpressModelAdmin(ModelAdmin):
    pass


@admin.register(QuoteRequest)
class QuoteRequestModelAdmin(ModelAdmin):
    pass


@admin.register(Footer)
class FooterModelAdmin(ModelAdmin):
    pass


@admin.register(Stats)
class StatsModelAdmin(ModelAdmin):
    pass


@admin.register(Partners)
class PartnersModelAdmin(ExportMixin, ModelAdmin):
    pass


@admin.register(About)
class AboutModelAdmin(ModelAdmin):
    pass


@admin.register(FAQ)
class FAQModelAdmin(ModelAdmin):
    pass


@admin.register(BlogPost)
class BlogPostAdmin(ExportMixin, ModelAdmin):
    inlines = [BlogImageInline]
    list_display = ('id', 'category', 'slug', 'published_at')
    prepopulated_fields = {"slug": ("category",)}  # slug avtomatik


@admin.register(Category)
class CategoryAdmin(ExportMixin, ModelAdmin):
    exclude = 'slug',


@admin.register(BlogImage)
class BlogImageAdmin(ModelAdmin):
    list_display = ('id', 'post', 'image')
