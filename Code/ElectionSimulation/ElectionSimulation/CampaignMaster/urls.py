from django.conf.urls import patterns, url

from ElectionSimulation.CampaignMaster import views

urlpatterns = patterns('',
    url(r'^$', views.listCampaign, name='listCampaign') # Show the list of current campaigns
)