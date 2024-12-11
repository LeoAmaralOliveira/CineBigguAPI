from rest_framework.permissions import BasePermission

class IsViewer(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'GET'

class IsEditor(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_staff:
            return request.method in ['POST', 'PUT', 'DELETE']
        return False

class IsUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.method in ['GET', 'POST', 'PUT', 'DELETE']
        return False
