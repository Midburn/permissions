from django.shortcuts import render
from rest_framework import generics
from ..models import Permission
from ..serializers import PermissionSerializer
# Create your views here.

class ListPermissionsView(generics.ListCreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class PermissionsDetail(generics.RetrieveAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
