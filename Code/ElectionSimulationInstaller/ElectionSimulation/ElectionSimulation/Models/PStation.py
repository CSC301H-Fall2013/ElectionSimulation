from django.db import models

class PStation(models.Model):
    """ The model for Polling Statons
    """
    pd_num = models.IntegerField()
    tot_votes = models.IntegerField()
    cand_num = models.IntegerField()
    votes = models.IntegerField()
