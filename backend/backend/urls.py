from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import CursoViewSet, InscripcionViewSet, CertificacionViewSet
from django.conf import settings
from django.conf.urls.static import static  # 👈 Import necesario

router = routers.DefaultRouter()
router.register(r'cursos', CursoViewSet)
router.register(r'inscripciones', InscripcionViewSet)
router.register(r'certificaciones', CertificacionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]