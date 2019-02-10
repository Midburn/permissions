from rest_framework import serializers
from .models import Permission, Role, UserRole

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ("name",) 

class RoleSerializer(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)
    class Meta:
        model = Role
        fields = ("name", 'permissions')

class UserRolesSerializer(serializers.HyperlinkedModelSerializer):
    role = RoleSerializer(many=True, queryset=Role.objects.all())
    url = serializers.HyperlinkedIdentityField(view_name='view-user-roles', lookup_field='pk')
    class Meta:
        model = UserRole
        fields = (
                  'url',
                  'user_id',
                  'event_id',
                  'group_id',
                  'role',
                  'status',
                  'change_date',
                  'user_name',
                  'email')