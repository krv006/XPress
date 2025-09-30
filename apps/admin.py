from django.contrib import admin
from django.contrib.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin

from apps.models import Footer, Stats, Partners, BlogPost, About, FAQ, BlogImage, Category
from apps.models.main_model import MainPage, QuoteRequest, ChooseXpress
from apps.resources import MainPageResource


class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 3
    max_num = 15


@admin.register(MainPage)
class MainPageModelAdmin(ImportExportModelAdmin):
    resource_class = MainPageResource


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
class PartnersModelAdmin(ModelAdmin):
    pass


@admin.register(About)
class AboutModelAdmin(ModelAdmin):
    pass


@admin.register(FAQ)
class FAQModelAdmin(ModelAdmin):
    pass


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    inlines = [BlogImageInline]
    list_display = ('id', 'category', 'slug', 'published_at')
    prepopulated_fields = {"slug": ("category",)}  # slug avtomatik


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = 'slug',


@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'image')
