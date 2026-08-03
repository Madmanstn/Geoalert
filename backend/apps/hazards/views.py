from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.contrib.gis.geos import GEOSGeometry

from apps.hazards.models import HazardType, HazardZone, HazardAlert
from apps.hazards.serializers import (
    HazardZoneSerializer,
    HazardZoneCreateSerializer,
    HazardTypeSerializer
)
from utils.permissions import IsDRRMOOfficer


class HazardZoneListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        zones = HazardZone.objects.filter(status='Active')
        serializer = HazardZoneSerializer(zones, many=True)
        return Response(serializer.data)


class HazardZoneCreateView(APIView):
    permission_classes = [IsAuthenticated, IsDRRMOOfficer]

    def post(self, request):
        serializer = HazardZoneCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        zone = serializer.save(published_by=request.user)

        # Create alert record
        HazardAlert.objects.create(
            hazard_zone = zone,
            issued_by   = request.user,
            hazard_type = zone.hazard_type,
            severity    = zone.severity,
            notes       = zone.description,
        )

        return Response(
            HazardZoneSerializer(zone).data,
            status=status.HTTP_201_CREATED
        )


class HazardZoneDetailView(APIView):
    permission_classes = [IsAuthenticated, IsDRRMOOfficer]

    def patch(self, request, pk):
        try:
            zone = HazardZone.objects.get(pk=pk)
        except HazardZone.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        zone.severity    = request.data.get('severity', zone.severity)
        zone.status      = request.data.get('status', zone.status)
        zone.description = request.data.get('description', zone.description)
        zone.save()

        return Response(HazardZoneSerializer(zone).data)


class HazardTypeListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        types = HazardType.objects.filter(is_active=True)
        serializer = HazardTypeSerializer(types, many=True)
        return Response(serializer.data)