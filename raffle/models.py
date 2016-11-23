from __future__ import unicode_literals

import os

from django.db import models
from django.contrib.auth.models import User

def get_board_folder_path(folder, filename):
    return os.path.join('banner/image/', filename)

# Create your models here.
class Raffle(models.Model):
    users = models.ManyToManyField(User)
    prize = models.CharField(max_length=255, null=True,blank=True)
    winner = models.PositiveIntegerField(null=True,blank=True)
    results = models.CharField(max_length=255, null=True,blank=True)
    def __str__(self):
        return str(self.pk)

class Banner(models.Model):
    banner_1 = models.ImageField(upload_to=get_board_folder_path, null=True,blank=True)
    banner_2 = models.ImageField(upload_to=get_board_folder_path, null=True,blank=True)
    banner_3 = models.ImageField(upload_to=get_board_folder_path, null=True,blank=True)
    banner_4 = models.ImageField(upload_to=get_board_folder_path, null=True,blank=True)