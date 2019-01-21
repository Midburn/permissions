from rest_framework import serializers
from .models import Permission, Role, UserRole

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ("name",) 

class RoleSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)
    class Meta:
        model = Role
        fields = ("name", 'permissions')

class UserRolesSerializer(serializers.ModelSerializer):
    role = RoleSerializer(many=True)
    class Meta:
        model = UserRole
        fields = ('user_id', 'event_id', 'group_id', 'role', 'status', 'change_date')