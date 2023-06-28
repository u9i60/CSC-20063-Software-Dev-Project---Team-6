from django.db import models
from django.utils import timezone

# Create your models here.

class Areas(models.Model):
    areaCode = models.TextField(db_column='areaCode', blank=True, null=True)  # Field name made lowercase.
    areaName = models.TextField(db_column='areaName', blank=True, null=True)  # Field name made lowercase.
    areaType = models.TextField(db_column='areaType', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'Areas'

        
class MetricDetails(models.Model):

    category = models.CharField(max_length=100)
    deprecated = models.CharField(max_length=100)
    doc_last_modified = models.CharField(max_length=100)
    metric = models.CharField(max_length=100)
    metric_name = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    
    class Meta:
        managed = False
        db_table = "MetricDetails"        
        
class Announcements(models.Model):
    body = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    expire = models.TextField(blank=True, null=True)
    has_expired = models.IntegerField(blank=True, null=True)
    launch = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Announcements'