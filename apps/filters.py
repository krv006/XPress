from django_filters import FilterSet, CharFilter, NumberFilter

from apps.models import FAQ, BlogPost


class FAQFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    contact_type = CharFilter(field_name='contact_type')

    class Meta:
        model = FAQ
        fields = 'title', 'contact_type',


class BlogPostFilter(FilterSet):
    category = CharFilter(field_name='category__name', lookup_expr='icontains')
    category_id = NumberFilter(field_name='category_id', lookup_expr='exact')

    class Meta:
        model = BlogPost
        fields = 'category',
