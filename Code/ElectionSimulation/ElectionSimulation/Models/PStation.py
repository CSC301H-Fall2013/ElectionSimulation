from django.db import models

class PStation(models.Model):
	""" The model for Polling Statons
    """

    pd_num = models.DateTimeField(max_length=1000) 
    tot_votes = models.DateTimeField(max_length=1000)
    cand_num = models.DateTimeField(max_length=1000)
    votes = models.DateTimeField(max_length=1000)
