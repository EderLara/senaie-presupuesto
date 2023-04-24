from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre_categoria = models.CharField(verbose_name ='Categoria', max_length = 45)
    # Atributos de Auditoria:
    create_at = models.DateField(auto_now = False, auto_now_add = True, verbose_name = "Fecha de creación", null = True, blank = True) 
    modify_at = models.DateField(auto_now = True, auto_now_add = False, verbose_name = "Fecha de actualización", null = True, blank = True)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return f'{ self.nombre_categoria }'

class Periodo(models.Model):
    nombre_periodo = models.CharField(verbose_name ='Año Fiscal', max_length = 4)
    # Atributos de Auditoria:
    create_at = models.DateField(auto_now = False, auto_now_add = True, verbose_name = "Fecha de creación", null = True, blank = True) 
    modify_at = models.DateField(auto_now = True, auto_now_add = False, verbose_name = "Fecha de actualización", null = True, blank = True)

    class Meta:
        verbose_name_plural = 'Periodo'

    def __str__(self):
        return f'{ self.nombre_periodo }'


class Mes(models.Model):
    nombre_mes = models.CharField(verbose_name ='Mes de Ejecución', max_length = 15)
    # Atributos de Auditoria:
    create_at = models.DateField(auto_now = False, auto_now_add = True, verbose_name = "Fecha de creación", null = True, blank = True) 
    modify_at = models.DateField(auto_now = True, auto_now_add = False, verbose_name = "Fecha de actualización", null = True, blank = True)

    class Meta:
        verbose_name_plural = 'Meses'

    def __str__(self):
        return f'{ self.nombre_mes }'
