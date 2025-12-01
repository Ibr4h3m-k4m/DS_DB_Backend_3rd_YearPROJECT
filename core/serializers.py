from django.contrib.auth import authenticate, get_user_model
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from requests import request
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer as BaseTokenObtainSerializer, TokenObtainPairSerializer as BaseTokenObtainPairSerializer

from dsdb.settings.common import MEDIA_URL
from . import models


from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import update_last_login
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions, serializers
from rest_framework.exceptions import ValidationError

from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken, SlidingToken, UntypedToken

from djoser.serializers import UserSerializer as BaseUserSerializer
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

from core.models import User


class UserCreateSerializer(BaseUserCreateSerializer):
   
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'type', 'username', 'password',
                  'email', 'first_name', 'last_name',] 
        


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'type', 'username', 'email' , 
                  'first_name', 'last_name',]
    
        




    
        
    
    

    
      