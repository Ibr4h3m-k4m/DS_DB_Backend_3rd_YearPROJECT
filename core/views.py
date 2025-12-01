from django.core.mail import send_mass_mail, mail_admins, BadHeaderError, EmailMessage
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from djoser.views import UserViewSet
from djoser.views import UserViewSet as BaseUserViewSet
"""
from rest_framework.viewsets import ModelViewSet , GenericViewSet
from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from .models import User
from django.conf import settings
from .models import Project
from .serializers import ViewModifyProjectSerializer, CreateProjectSerializer
from . import permissions


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ViewModifyProjectSerializer
    permission_classes = [permissions.IsProjectLeaderOrAuthenticatedUser]
    
    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return CreateProjectSerializer
        return ViewModifyProjectSerializer
    
        
"""    
        



    
    
    
        






    
    
    
    