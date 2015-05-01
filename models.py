from django.db import models

class User(models.Model):
      name = models.CharField(max_length=255)
      password = models.CharField(max_length=255) # Temp
      email = models.EmailField(max_length=255) 
      gender = models.BooleanField() # True - man, False - patetic woman.


class Event(models.Model):
      time = models.DateTimeField()
      playfield = models.ManyToManyField(PlayField)
      user = models.ManyToManyField(User)
      interest = models.ManyToManyField(Interest)

class PlayField(models.Model):
      # coordinates
      latitude = models.DecimalField(max_digits=5,decimal_places=2)
      longitude = models.DecimalField(max_digits=5,decimal_places=2)
      #???
      interest = models.ManyToManyField(Interest)
      user = models.ManyToManyField(User)    
       
class Location(models.Model):
      playfield = models.ManyToManyField(PlayField)
      user = models.ManyToManyField(User)
      interest = models.ManyToManyField(Interest)

class Interest(models.Model):
      interest_area = None #????
      type = None #????
