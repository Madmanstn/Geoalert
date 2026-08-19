from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from apps.hazards.models import HazardType, HazardZone, HazardAlert
from apps.accounts.serializers import UserSerializer


class HazardTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = HazardType
        fields = ['id', 'name', 'logo_class', 'is_active']


class HazardZoneGeoSerializer(GeoFeatureModelSerializer):
    """
    Returns hazard zones as proper GeoJSON FeatureCollection.
    This is what Leaflet.js consumes directly.
    """
    hazard_type_name = serializers.CharField(
        source='hazard_type.name', read_only=True
    )

    class Meta:
        model       = HazardZone
        geo_field   = 'geometry'
        fields = [
            'id', 'hazard_type_name', 'severity',
            'status', 'description', 'activated_at',
            'resolved_at'
        ]


class HazardZoneSerializer(serializers.ModelSerializer):
    hazard_type = HazardTypeSerializer(read_only=True)

    class Meta:
        model  = HazardZone
        fields = [
            'id', 'barangay', 'published_by', 'hazard_type',
            'severity', 'status', 'description',
            'activated_at', 'resolved_at'
        ]


class HazardZoneCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model  = HazardZone
        fields = [
            'barangay', 'hazard_type', 'severity',
            'geometry', 'description'
        ]


class HazardAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model  = HazardAlert
        fields = [
            'id', 'hazard_zone', 'issued_by',
            'hazard_type', 'severity', 'notes', 'created_at'
        ]