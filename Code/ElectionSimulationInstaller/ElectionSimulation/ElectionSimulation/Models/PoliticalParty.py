from django.db import models

class PoliticalParty(models.Model):
    """ The model for a political party
    """

    # The name of the Political party
    name = models.CharField(max_length=1000)
