from rest_framework import serializers
from apps.hazards.models import HazardType, HazardZone, HazardAlert
from apps.accounts.serializers import UserSerializer


class HazardTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = HazardType
        fields = ['id', 'name', 'logo_class', 'is_active']


class HazardZoneSerializer(serializers.ModelSerializer):
    hazard_type  = HazardTypeSerializer(read_only=True)
    published_by = UserSerializer(read_only=True)

    class Meta:
        model  = HazardZone
        fields = [
            'id', 'barangay', 'published_by', 'hazard_type',
            'severity', 'status', 'geometry', 'description',
            'activated_at', 'resolved_at'
        ]
        geo_field = 'geometry'


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