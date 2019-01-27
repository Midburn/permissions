from django.shortcuts import render
from rest_framework import generics, filters
from ..models import UserRole
from ..serializers import UserRolesSerializer
# Create your views here.


class ListUserRolesView(generics.ListCreateAPIView):
    queryset = UserRole.objects.all()
    serializer_class = UserRolesSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('event_id', 'group_id')
    #def get_queryset(self):
    #    event_id = self.request.query_params.get('event_id', None)
    #    group_id = self.request.query_params.get('group_id', None)
    #    user_id = self.request.query_params.get('user_id', None)
    #    queryset = UserRole.objects.all()
#
    #    filter_args = {}
#
    #    if event_id:
    #        filter_args['event_id'] = event_id
    #    if group_id:
    #        filter_args['group_id'] = group_id
    #    if user_id:
    #        filter_args['user_id'] = user_id
#
    #    return queryset.filter(**filter_args)