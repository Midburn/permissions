from django.urls import path
from .views.permissions import ListPermissionsView, PermissionsDetail
from .views.roles import ListRolesView
from .views.user_roles import ListUserRolesView

urlpatterns = [
        path('permissions/', ListPermissionsView.as_view(),name='permissions-all'),
        path('permissions/<int:pk>', PermissionsDetail.as_view(),name='view-permissions'),
        path('roles/', ListRolesView.as_view(),name='permissions-all'),
        path('user_roles/', ListUserRolesView.as_view(), name='user-roles'),
        path('user_roles/<int:id>', ListUserRolesView.as_view(), name='view-user-roles')
]