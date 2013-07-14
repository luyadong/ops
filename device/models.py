#!coding:utf8
from django.db import models

class Device(models.Model):
    nei_ip	    = models.CharField(max_length=50,unique=True)
    wai_ip	    = models.CharField(max_length=50,null=True)
    hostname	    = models.CharField(max_length=50)
    serial_number   = models.CharField(max_length=50)
    buy_date	    = models.DateField(null=True)
    inventar_Nummer = models.CharField(max_length=50)
    manufacturer    = models.CharField(max_length=50)
    type	    = models.CharField(max_length=50)
    monitor	    = models.CharField(max_length=1, choices=(('y','是'),('n','否')))
    location	    = models.CharField(max_length=50)
    principal	    = models.CharField(max_length=50,null=True)
    administrator   = models.CharField(max_length=50,null=True)
    purpose	    = models.CharField(max_length=50,null=True)
    status	    = models.CharField(max_length=1,choices=(('y','活动'),('n','非活动')))
    remarks	    = models.TextField(null=True)
    os		    = models.CharField(max_length=1, choices=(('c','Centos'),('w','Windows'),('f','Fedora')))
    partion	    = models.CharField(max_length=50,null=True)
    cpu		    = models.CharField(max_length=50)
    memory	    = models.CharField(max_length=50)
    disk	    = models.CharField(max_length=50)
    disk_controller = models.CharField(max_length=50,null=True)
    protocol	    = models.CharField(max_length=20)
    port	    = models.CharField(max_length=20)
    username	    = models.CharField(max_length=20)
    password	    = models.CharField(max_length=20)

    def __unicode__(self):
        return self.nei_ip
