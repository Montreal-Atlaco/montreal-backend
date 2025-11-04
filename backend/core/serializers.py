from rest_framework import serializers
from .models import Curso, Inscripcion, Certificacion

class CursoSerializer(serializers.ModelSerializer):
    class Meta: model = Curso; fields = "__all__"

class InscripcionSerializer(serializers.ModelSerializer):
    class Meta: model = Inscripcion; fields = "__all__"

class CertificacionSerializer(serializers.ModelSerializer):
    class Meta: model = Certificacion; fields = "__all__"
