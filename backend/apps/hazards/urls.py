from django.urls import path
from apps.hazards.views import (
    HazardZoneListView,
    HazardZoneCreateView,
    HazardZoneDetailView,
    HazardTypeListView,
)

urlpatterns = [
    path('',              HazardZoneListView.as_view(),   name='hazard-list'),
    path('create/',       HazardZoneCreateView.as_view(), name='hazard-create'),
    path('<uuid:pk>/',    HazardZoneDetailView.as_view(), name='hazard-detail'),
    path('types/',        HazardTypeListView.as_view(),   name='hazard-types'),
]