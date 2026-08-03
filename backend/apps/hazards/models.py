import uuid
from django.contrib.gis.db import models
from apps.accounts.models import User
from apps.barangays.models import Barangay


class HazardType(models.Model):
    name       = models.CharField(max_length=50, unique=True)
    logo_class = models.CharField(max_length=50, blank=True)
    is_active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'hazard_type'

    def __str__(self):
        return self.name


class HazardZone(models.Model):
    SEVERITY_CHOICES = [
        ('Red',    'Extreme'),
        ('Orange', 'Moderate'),
        ('Green',  'Low'),
    ]
    STATUS_CHOICES = [
        ('Active',   'Active'),
        ('Resolved', 'Resolved'),
        ('Archived', 'Archived'),
    ]

    id           = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    barangay     = models.ForeignKey(Barangay, on_delete=models.SET_NULL, null=True)
    published_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hazard_type  = models.ForeignKey(HazardType, on_delete=models.SET_NULL, null=True)
    severity     = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    status       = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    geometry     = models.MultiPolygonField(srid=4326)
    description  = models.TextField(blank=True)
    activated_at = models.DateTimeField(auto_now_add=True)
    resolved_at  = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'hazard_zone'

    def __str__(self):
        return f'{self.hazard_type} - {self.severity} - {self.status}'


class HazardAlert(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hazard_zone = models.ForeignKey(HazardZone, on_delete=models.CASCADE)
    issued_by   = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hazard_type = models.ForeignKey(HazardType, on_delete=models.SET_NULL, null=True)
    severity    = models.CharField(max_length=20)
    notes       = models.TextField(blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'hazard_alert'

    def __str__(self):
        return f'Alert - {self.hazard_type} - {self.severity}'