from django.db import models

class Link(models.Model):
    """ The model for a link between polling stations and census tracts
    """

    pd_num = models.DateTimeField(max_length=1000)
    ctuid = models.DateTimeField(max_length=1000)
