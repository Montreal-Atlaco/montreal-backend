from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    duracion_horas = models.PositiveIntegerField(default=20)
    activo = models.BooleanField(default=True)

    def __str__(self): return self.nombre



class Certificacion(models.Model):
    alumno = models.CharField(max_length=140)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    folio = models.CharField(max_length=50, unique=True)
    fecha_emision = models.DateField()

    def __str__(self): return self.folio
class Inscripcion(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    curso = models.CharField(max_length=50)
    nivel = models.CharField(max_length=50)
    comentarios = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.curso} ({self.nivel})"