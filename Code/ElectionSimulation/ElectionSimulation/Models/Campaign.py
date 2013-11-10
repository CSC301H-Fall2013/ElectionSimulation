from django.db import models

class Campaign(models.Model):
    """ The model for a campaign
    """

    name = models.CharField(max_length=1000)
    create_date = models.DateTimeField(auto_now_add=True)

