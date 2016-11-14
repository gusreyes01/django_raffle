from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Raffle(models.Model):
    users = models.ManyToManyField(User)
    winner = models.ForeignKey(User, related_name="winner", null=True,blank=True)
