from django.urls import path
# importar el view que tengo en la app:
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'inicio'),
]
