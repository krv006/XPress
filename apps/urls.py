from django.urls import path

from apps.views import BlogDetailAPIView, BlogListAPIView, AboutListAPIView, FAQListAPIView, SimpleContactListAPIView, \
    FooterListCreate, PartnerListCreate, StatsListCreate, MainPageListAPIView, DirectlyContactListAPIView, \
    ContactOptionListCreate, SimpleStepsListAPIView

urlpatterns = [
    # todo main
    path('main-page/', MainPageListAPIView.as_view(), name='main_page'),
    path('quotes-directly/', DirectlyContactListAPIView.as_view(), name='directly_quotes'),
    path('quotes-simple/', SimpleContactListAPIView.as_view(), name='simple_quotes'),
    path('simple-steps/', SimpleStepsListAPIView.as_view(), name='simple_steps'),
    # todo contact-option
    path('contact-option/', ContactOptionListCreate.as_view(), name='contact_option'),
    # todo footer
    path('footer/', FooterListCreate.as_view(), name='footer'),
    path('footer-simple/', StatsListCreate.as_view(), name='footer_simple'),
    path('partners/', PartnerListCreate.as_view(), name='partners'),
    # todo blog
    path('blog-detail/<int:pk>', BlogDetailAPIView.as_view(), name='blog_detail'),
    path('blog/', BlogListAPIView.as_view(), name='blog'),
    # todo about
    path("about/", AboutListAPIView.as_view(), name="about-list"),
    path("faq/", FAQListAPIView.as_view(), name="faq-list"),
]
