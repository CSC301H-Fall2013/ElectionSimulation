from django.contrib import admin
from Models.Campaign import Campaign
from Models.Formula import Formula
from Models.Riding import Riding
from Models.PoliticalParty import PoliticalParty

admin.site.register(Campaign)
admin.site.register(Formula)
admin.site.register(Riding)
admin.site.register(PoliticalParty)