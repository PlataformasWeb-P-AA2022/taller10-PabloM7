from django.db import models


# Create your models here.
class Parroquia(models.Model):
    ordering = ["tipo_parroquia"]
    verbose_name_plural = "Los Estudiantes"

    opciones_tipo_parroquia = (
        ('urbana', 'Parroquia Urbana'),
        ('rural', 'Parroquia Rural'),
        )

    nombre = models.CharField("parroquia",max_length=30)
    tipo_parroquia = models.CharField("tipo",max_length=30, \
            choices=opciones_tipo_parroquia) 
    # modulos = models.ManyToManyField('Modulo', through='Matricula')

    def __str__(self):
        return "%s - %s" % (
                self.nombre,  
                self.tipo_parroquia)

class Barrio(models.Model):
    opciones_parques = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        )
    nombre = models.CharField("barrio",max_length=30)
    num_viviendas = models.IntegerField("numero de viviendas")
    parques = models.CharField("numero de parques",max_length=30, \
            choices=opciones_parques)
    num_edificios = models.IntegerField("numero de edificios")
    parroquia = models.ForeignKey(Parroquia, related_name='lasparroquias', 
            on_delete=models.CASCADE)

    def __str__(self):
        return "Módulo: %s - %s -%s -%s - %s" % (
                self.nombre,
                self.num_viviendas,
                self.parques,
                self.num_edificios,
                self.parroquia) 