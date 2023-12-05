from django.db import models

# Create your models here.
class Truck(models.Model):
    samsara_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)