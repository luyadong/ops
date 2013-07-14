from django.db import models
from device.models import Device

class Project(models.Model):
    name     = models.CharField(max_length=50,unique=True)
    web      = models.CharField(max_length=50)
    document = models.CharField(max_length=50)
    device   = models.ManyToManyField(Device)

    def __unicode__(self):
        return self.name

