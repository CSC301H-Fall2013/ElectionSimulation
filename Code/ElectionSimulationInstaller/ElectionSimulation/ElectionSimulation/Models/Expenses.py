from django.db import models

class Expenses(models.Model):
    """ The model for Candidates' Expenses
    """

    cand_num = models.IntegerField()
    expense = models.IntegerField()
    expense_ceiling =  models.IntegerField()
