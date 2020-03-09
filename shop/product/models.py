from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length = 200, null = False, blank = False)
    description = models.TextField(null = True, blank = True)
    price = models.DecimalField(decimal_places=0, max_digits = 10)
    active = models.BooleanField(default = True)

    def __str__(self):
        return self.title