from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    room_name = models.CharField(max_length=150, null=False, blank=False)


class Room(models.Model):
    room_name = models.CharField(max_length=255)

    def __str(self):
        return self.room_name


class Messages(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    message = models.TextField()

    def __str(self):
        return str(self.room)
