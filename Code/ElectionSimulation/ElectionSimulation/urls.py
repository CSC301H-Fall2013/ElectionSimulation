# This file manage top level url pattern that will direct to subsections of the site
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^campaign_master/', include('ElectionSimulation.CampaignMaster.urls')), # Campaign master's pages
)
