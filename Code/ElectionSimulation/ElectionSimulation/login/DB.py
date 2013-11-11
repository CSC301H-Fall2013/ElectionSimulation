from django.db import models

class Census(models.Model):
  census_tract = models.CharField(max_length=30)
  CT_vote = models.IntegerField()
  CT_a = models.IntegerField()
  
  
