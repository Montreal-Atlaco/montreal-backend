from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import (
    CursoViewSet,
    InscripcionViewSet,
    CertificacionViewSet,
    ContactFormView,
)
from django.http import HttpResponse

# Rutas para tus modelos
router = routers.DefaultRouter()
router.register(r"cursos", CursoViewSet)
router.register(r"inscripciones", InscripcionViewSet)
router.register(r"certificaciones", CertificacionViewSet)

# Vista básica para la página de inicio
def home(request):
    return HttpResponse("<h1>Bienvenido a la API de Montreal</h1><p>Usa /api/ para acceder a los recursos.</p>")

# URL patterns
urlpatterns = [
    path("", home, name="home"),  # 👈 evita el error 404 en /
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/contacto/", ContactFormView.as_view(), name="contacto"),
]
