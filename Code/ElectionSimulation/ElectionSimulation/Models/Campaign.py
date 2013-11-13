from django.db import models
from ElectionSimulation.Models.Formula import Formula


class Campaign(models.Model):
    """ The model for a campaign
    """

    # Name of the campaign
    name = models.CharField(max_length=1000)
    # The date this campaign is created
    create_date = models.DateTimeField(auto_now_add=True)
    # List of all candidates
    candidates = models.CharField(max_length=1000)
    # Name of the voting system
    voting_system = models.CharField(max_length=1000)
    # The formula for the calculation
    formula = models.ForeignKey(Formula)
  
    def __unicode__(self):
      return self.name
