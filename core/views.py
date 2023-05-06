from django.shortcuts import render
# Importamos la clase madre:
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'core/index.html'