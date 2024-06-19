from django.views.generic import ListView, TemplateView
from .models import New

class NewsListView(ListView):
    model = New
    template_name = "news.html"
    ordering = ["-date"]

class CatalogView(TemplateView):
    template_name = "catalog.html"

class HomeView(TemplateView):
    template_name = "index.html"

class NordGSMAirView(TemplateView):
    template_name = "nord-gsm-air.html"

class NordGSMMetalView(TemplateView):
    template_name = "nord-gsm-metal.html"

class NordMiniView(TemplateView):
    template_name = "nord-mini.html"

class NordGSMView(TemplateView):
    template_name = "untitlednord-gsm.html"