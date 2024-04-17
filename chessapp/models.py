from django.db import models


class Tshirts(models.Model):
    parentsname = models.CharField(max_length=25, blank=False, null=False)
    membersname = models.CharField(max_length=25, blank=False, null=False)
    color = models.CharField(max_length=25, blank=False, null=False)
    size = models.CharField(max_length=25, blank=False, null=False)
    units = models.IntegerField()


class Hoodies(models.Model):
    parentsname2 = models.CharField(max_length=25, blank=False, null=False)
    membersname2 = models.CharField(max_length=25, blank=False, null=False)
    color2 = models.CharField(max_length=25, blank=False, null=False)
    size2 = models.CharField(max_length=25, blank=False, null=False)
    units2 = models.IntegerField()

class Goodies(models.Model):
    parentsname3 = models.CharField(max_length=25, blank=False, null=False)
    membersname3 = models.CharField(max_length=25, blank=False, null=False)
    item = models.CharField(max_length=25, blank=False, null=False)
    units3 = models.IntegerField()


class Events(models.Model):
     parentsname1 = models.CharField(max_length=25, blank=False, null=False)
     membersname1 = models.CharField(max_length=25, blank=False, null=False)
     adm = models.CharField(max_length=25, blank=False, null=False)
     Class = models.CharField(max_length=25)
     dob = models.CharField(max_length=25)
     gender = models.CharField(max_length=25)