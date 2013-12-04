from django.db import models

class Result(models.Model):
    """ The model for a Result
    """

    # The name of the Riding
    candidates = models.CharField(max_length=1000)
    # The government code for the riding
    vote = models.IntegerField()
