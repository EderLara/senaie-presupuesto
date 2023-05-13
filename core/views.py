from django.shortcuts import render
# Importamos la clase madre:
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'core/index.html'

    # atributos propios en diccionarios de contexto:
    dict_context = {
        'promo' : ['Prepara', 'Dispone', 'Gestiona'],
        'framework' : 'DJANGO',
        'titulo_mapa': 'Encuentranos aquí:'
    }

    # Sobreescribimos el método get de la clase TemplateView:
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.dict_context)