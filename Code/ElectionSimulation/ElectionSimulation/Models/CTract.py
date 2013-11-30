from django.db import models

class CTract(models.Model):
	""" The model for Census Tracts
    """

    ctuid = models.DateTimeField(max_length=1000)
    age_1 = models.DateTimeField(max_length=1000)
    age_2 = models.DateTimeField(max_length=1000)
    age_3 = models.DateTimeField(max_length=1000)
    age_4 = models.DateTimeField(max_length=1000)
    age_5 = models.DateTimeField(max_length=1000)
    age_6 = models.DateTimeField(max_length=1000)
    age_7 = models.DateTimeField(max_length=1000)
    age_8 = models.DateTimeField(max_length=1000)
    age_9 = models.DateTimeField(max_length=1000)
    age_10 = models.DateTimeField(max_length=1000)
