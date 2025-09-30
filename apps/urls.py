from django.urls import path

from apps.views import BlogDetailAPIView, BlogListAPIView, AboutListAPIView, FAQListAPIView, SimpleListAPIView, \
    FooterListCreate, PartnerListCreate, StatsListCreate, MainPageListAPIView, DirectlyContactListAPIView, \
    ContactOptionListCreate, SimpleStepsListAPIView, ChooseXpressListAPIView, OverviewListAPIView, \
    FaqFrequentlyListAPIView

urlpatterns = [
    # todo main
    path('main-page/', MainPageListAPIView.as_view(), name='main_page'),
    path('quotes-simple/', SimpleListAPIView.as_view(), name='simple_quotes'),
    path('choose-xpress/', ChooseXpressListAPIView.as_view(), name='choose_xpress'),
    path('overview/', OverviewListAPIView.as_view(), name='overview'),
    path('simple-steps/', SimpleStepsListAPIView.as_view(), name='simple_steps'),
    path('Frequently/', FaqFrequentlyListAPIView.as_view(), name='Frequently'),
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
    # todo contact
    path('quotes-directly/', DirectlyContactListAPIView.as_view(), name='directly_quotes'),

]
