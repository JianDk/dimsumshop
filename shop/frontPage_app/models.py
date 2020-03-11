from django.db import models

# Create your models here.
class customerLocation(models.Model):
    postnr = models.IntegerField(null = False, blank = False)
    
    
   
    
