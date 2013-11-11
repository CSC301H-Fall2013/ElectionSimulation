from django.db import models

class Riding(models.Model):
    """ The model for a riding
    """

    # The name of the Riding
    name = models.CharField(max_length=1000)
    # The government code for the riding
    code = models.DateTimeField(max_length=1000)
