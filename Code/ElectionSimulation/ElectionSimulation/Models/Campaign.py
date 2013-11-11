from django.db import models

class Campaign(models.Model):
    """ The model for a campaign
    """

    # Name of the campaign
    name = models.CharField(max_length=1000)
    # The date this campaign is created
    create_date = models.DateTimeField(auto_now_add=True)

