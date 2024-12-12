from django.db import models

# Create your models here.

class Recode(models.Model):
    time = models.DateTimeField("time", auto_now_add=True)
    light = models.IntegerField("light")
    pressure = models.IntegerField("pressure")
    windD = models.IntegerField("windD")
    windS = models.IntegerField("windS")
    temp = models.IntegerField("temp")
    
    def __str__(self):
        return str(self.tempValue)
    