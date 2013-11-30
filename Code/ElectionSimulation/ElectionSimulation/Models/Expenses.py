from django.db import models

class Expenses(models.Model):
	""" The model for Candidates' Expenses
    """

    cand_num = models.DateTimeField(max_length=1000)
    expense = models.DateTimeField(max_length=1000)
    expense_ceiling =  models.DateTimeField(max_length=1000)
