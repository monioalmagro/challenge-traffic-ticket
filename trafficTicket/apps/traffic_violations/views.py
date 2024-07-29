from apps.traffic_violations.models import Person, Vehicle, Violation

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(["POST"])
def cargar_infraccion(request):
    placa_patente = request.data.get("placa_patente")
    timestamp = request.data.get("timestamp")
    comentarios = request.data.get("comentarios")

    try:
        vehicle = Vehicle.objects.get(license_plate=placa_patente)
    except Vehicle.DoesNotExist:
        return Response(
            {"error": "Vehicle not found"}, status=status.HTTP_404_NOT_FOUND
        )

    violation_kwargs = {"vehicle": vehicle}
    if timestamp:
        violation_kwargs["timestamp"] = timestamp
    if comentarios:
        violation_kwargs["comments"] = comentarios

    violation = Violation(**violation_kwargs)
    violation.save()

    return Response(
        {"message": "Violation recorded successfully"},
        status=status.HTTP_200_OK
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def generar_informe(request, email):
    person: Person = get_object_or_404(Person, email=email)
    vehicles = person.vehicles.all()
    violations = Violation.objects.filter(vehicle__in=vehicles).select_related(
        "vehicle"
    )

    violations_list = [
        {
            "vehicle": (
                f"{violation.vehicle.brand} - {violation.vehicle.license_plate}"
            ),
            "timestamp": violation.timestamp,
            "comments": violation.comments,
        }
        for violation in violations
    ]

    return JsonResponse(violations_list, safe=False)
