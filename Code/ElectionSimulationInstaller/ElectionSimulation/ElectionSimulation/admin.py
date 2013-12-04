from django.contrib import admin
from Models.Campaign import Campaign
from Models.Formula import Formula
from Models.Riding import Riding
from Models.PoliticalParty import PoliticalParty
from Models.PStation import PStation
from Models.CTract import CTract
from Models.Expenses import Expenses
from Models.Link import Link

admin.site.register(Campaign)
admin.site.register(Formula)
admin.site.register(Riding)
admin.site.register(PoliticalParty)
admin.site.register(PStation)
admin.site.register(CTract)
admin.site.register(Expenses)
admin.site.register(Link)