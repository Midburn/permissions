from django.shortcuts import render
from rest_framework import generics
from ..models import Role
from ..serializers import RoleSerializer
# Create your views here.


class ListRolesView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer