from django.db import models

class Formula(models.Model):
    """ The model for a Formula
    """

    # The name of the Formula
    name = models.CharField(max_length=1000)
