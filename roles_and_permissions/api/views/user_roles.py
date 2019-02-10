from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework import generics, filters
from ..models import UserRole
from ..serializers import UserRolesSerializer
# Create your views here.


class ListUserRolesView(generics.ListCreateAPIView):
    queryset = UserRole.objects.all()
    serializer_class = UserRolesSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    #lookup_field = 'id'
    search_fields = ('event_id', 'group_id', 'email', 'user_name')
    filter_fields = ('event_id', 'group_id', 'user_id')
    
class UpdateUserRolesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserRole.objects.all()
    serializer_class = UserRolesSerializer
    #lookup_field = 'id'
