from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
import quickstart.models as models
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, Oblique3DModelSerializer

import os

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class Oblique3DmodelViewSet(viewsets.ModelViewSet):
    queryset = models.Oblique3DModel.objects.all()
    serializer_class = Oblique3DModelSerializer