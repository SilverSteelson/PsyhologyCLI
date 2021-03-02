"""
Definition of models.
"""

from django.db import models
#from django.utils.translation import ugettext_lazy as trnsl

class Methods(models.Model):
    therapy = models.TextField(null=False,blank=False,unique = True)
    def __init__(self):
        return self.therapy

class Clinicus(models.Model):
    idrecord = models.CharField(max_length=20,unique = True)
    name = models.CharField(max_length=60)
    method = models.ManyToManyField(Methods)
    urlslrgefoto = models.URLField()
    urlssmlfoto = models.URLField()
    timeload = models.DateField(auto_now_add=True)