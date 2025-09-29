from django.urls import path

from apps.views import BlogDetailAPIView, BlogListAPIView, AboutListAPIView, FAQListAPIView
from apps.views import FooterListCreate, PartnerListCreate, StatsListCreate
from apps.views import MainPageListCreate, ProfessionalTeamListCreate

urlpatterns = [
    # todo main
    path('main-page/', MainPageListCreate.as_view(), name='main_page'),
    path('proffessional-team/', ProfessionalTeamListCreate.as_view(), name='professional_team'),
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
