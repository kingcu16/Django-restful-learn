from django.contrib.auth.models import User, Group
from rest_framework import serializers
import quickstart.models as models

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password' ,'groups', models.USER_3DMODEL]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name', models.GROUP_3DMODEL]

class Oblique3DModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Oblique3DModel
        fields = ['url', 'user', 'group']