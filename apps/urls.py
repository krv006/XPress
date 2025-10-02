from django.urls import path

from apps.views import BlogListAPIView, AboutListAPIView, FAQListAPIView, SimpleListCreateAPIView, \
    FooterListCreate, PartnerListCreate, StatsListCreate, MainPageListAPIView, DirectlyContactListAPIView, \
    ContactOptionListCreate, SimpleStepsListAPIView, ChooseXpressListAPIView, OverviewListAPIView, \
    OrderStep1CreateAPIView, MainAboutListAPIView, StarListAPIView, VehicleMakeAPIView, VehicleYearAPIView, \
    VehicleModelAPIView, ZipCodeAPIView

urlpatterns = [
    # todo main
    path('main-page/', MainPageListAPIView.as_view(), name='main_page'),
    path('quotes/simple/', SimpleListCreateAPIView.as_view(), name='simple_quotes'),
    path('choose/xpress/', ChooseXpressListAPIView.as_view(), name='choose_xpress'),
    path('overview/', OverviewListAPIView.as_view(), name='overview'),
    path('steps/', SimpleStepsListAPIView.as_view(), name='simple_steps'),
    path('main/about/', MainAboutListAPIView.as_view(), name='main_about'),
    # todo contact-option
    path('contact-option/', ContactOptionListCreate.as_view(), name='contact_option'),
    # todo footer
    path('footer/', FooterListCreate.as_view(), name='footer'),
    path('stats/', StatsListCreate.as_view(), name='footer_simple'),
    path('partners/', PartnerListCreate.as_view(), name='partners'),
    # todo blog
    path('blog/', BlogListAPIView.as_view(), name='blog'),
    # todo about
    path("about/", AboutListAPIView.as_view(), name="about-list"),
    path("faq/", FAQListAPIView.as_view(), name="faq-list"),
    # todo contact
    path('quotes/directly/', DirectlyContactListAPIView.as_view(), name='directly_quotes'),
    # todo calculator integrations
    path("orders/", OrderStep1CreateAPIView.as_view(), name="order_step1"),

    # todo stars
    path("stars/", StarListAPIView.as_view(), name="star_list"),

    # todo apis
    path("vehicle-makes/", VehicleMakeAPIView.as_view(), name="vehicle-makes"),
    path("vehicle-models/", VehicleModelAPIView.as_view(), name="vehicle-models"),
    path("vehicle-years/", VehicleYearAPIView.as_view(), name="vehicle-years"),
    path("zip-codes/", ZipCodeAPIView.as_view(), name="zip-codes"),

]
