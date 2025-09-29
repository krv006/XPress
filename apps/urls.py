from django.urls import path

from apps.views import BlogDetailAPIView, BlogListAPIView
from apps.views import FooterListCreate, PartnerListCreate, FooterSimpleListCreate
from apps.views import MainPageListCreate, ProfessionalTeamListCreate

urlpatterns = [
    # todo main
    path('main-page/', MainPageListCreate.as_view(), name='main_page'),
    path('proffessional-team/', ProfessionalTeamListCreate.as_view(), name='professional_team'),
    # todo footer
    path('footer/', FooterListCreate.as_view(), name='footer'),
    path('footer-simple/', FooterSimpleListCreate.as_view(), name='footer_simple'),
    path('partners/', PartnerListCreate.as_view(), name='partners'),
    # todo blog
    path('blog-datil/<int:pk>', BlogDetailAPIView.as_view(), name='blog_detail'),
    path('blog/', BlogListAPIView.as_view(), name='blog'),
]
