from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.

USER_3DMODEL = 'oblique_model_user'
GROUP_3DMODEL = 'oblique_model_group'

class Oblique3DModel(models.Model):
    url = models.CharField(max_length=250)
    user = models.ForeignKey(to='auth.User', related_name=USER_3DMODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(to='auth.Group', related_name=GROUP_3DMODEL, on_delete=models.CASCADE)

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
User = get_user_model()

class UserBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as _:
            return None