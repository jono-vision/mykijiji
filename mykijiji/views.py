from django.views.generic.base import TemplateView
from .models import Search


class HomePageView(TemplateView):
    model = Search
    template_name = "home.html"
