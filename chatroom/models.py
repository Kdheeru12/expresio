from django.db import models
from api.models import Room
# Create your models here.
# class Room(models.Model):
#   title = models.CharField(max_length=50)

#   def __str__(self):
#     return self.title


# Create your models here.
class Message(models.Model):
  room_name = models.ForeignKey(Room, on_delete=models.CASCADE)
  message = models.CharField(max_length=100)
  sender = models.CharField(max_length=50)

  def __str__(self):
    return self.message

