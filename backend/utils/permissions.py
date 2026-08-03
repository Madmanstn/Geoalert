from rest_framework.permissions import BasePermission


class IsSystemAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            hasattr(request.user, 'role') and
            request.user.role is not None and
            request.user.role.name == 'System_Admin'
        )


class IsDRRMOOfficer(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if not hasattr(request.user, 'role') or request.user.role is None:
            return False
        return request.user.role.name in ['DRRMO_Officer', 'System_Admin']


class IsBarangayPersonnel(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if not hasattr(request.user, 'role') or request.user.role is None:
            return False
        return request.user.role.name in [
            'Barangay_Personnel', 'DRRMO_Officer', 'System_Admin'
        ]