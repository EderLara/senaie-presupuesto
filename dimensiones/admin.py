from django.contrib import admin
from .models import Categoria, Periodo, Mes

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Periodo)
admin.site.register(Mes)