from apps.traffic_violations.views import cargar_infraccion, generar_informe

from django.urls import path

urlpatterns = [
    path("cargar_infraccion/", cargar_infraccion, name="cargar_infraccion"),
    path(
        "generar_informe/<str:email>/",
        generar_informe,
        name="generar_informe"
    ),
]
