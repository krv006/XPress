from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from import_export.admin import ExportMixin

from apps.models import Footer, Stats, Partners, BlogPost, About, FAQ, ReviewBreakdown, \
    ReviewSource, Overview
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
    list_filter = ("contact_type", "by_checking")
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
    list_display = ("id", "title", "category")
    list_display_links = ("id", "title")
    list_editable = ("category",)
    list_filter = ("category",)
    search_fields = ("title", "description")
    ordering = ("title",)
    list_per_page = 15


@admin.register(BlogPost)
class BlogPostAdmin(ExportMixin, ModelAdmin):
    list_display = ('id','title', 'views')
    search_fields = ('title',)
    autocomplete_fields = ()
    list_per_page = 15
    save_on_top = True



class ReviewBreakdownInline(TabularInline):
    model = ReviewBreakdown
    extra = 0  # qo'shimcha bo'sh qator qo'ymasin
    min_num = 0
    fields = ("stars", "count", "percentage")
    ordering = ("-stars",)  # 5 → 1 tartibda ko‘rsatish


@admin.register(ReviewSource)
class ReviewSourceAdmin(ModelAdmin):
    list_display = ("name", "average_rating", "total_reviews")
    search_fields = ("name",)
    list_per_page = 20
    inlines = (ReviewBreakdownInline,)


@admin.register(ReviewBreakdown)
class ReviewBreakdownAdmin(ModelAdmin):
    list_display = ("source", "stars", "count", "percentage")
    list_filter = ("source", "stars")
    search_fields = ("source__name",)
    ordering = ("source", "-stars")
    list_per_page = 50


admin.site.register(Overview)
