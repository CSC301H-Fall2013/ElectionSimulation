from django.db import models

class CTract(models.Model):
    """ The model for Census Tracts
    """

    ctuid = models.IntegerField()
    age_1 = models.FloatField()
    age_2 = models.FloatField()
    age_3 = models.FloatField()
    age_4 = models.FloatField()
    age_5 = models.FloatField()
    age_6 = models.FloatField()
    age_7 = models.FloatField()
    age_8 = models.FloatField()
    age_9 = models.FloatField()
    age_10 = models.FloatField()
