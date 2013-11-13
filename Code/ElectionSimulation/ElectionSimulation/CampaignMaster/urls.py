from django.conf.urls import patterns, url

from ElectionSimulation.CampaignMaster import views

urlpatterns = patterns('',
    # GET : Show the list of current campaigns
    url(r'^$', views.list_campaign, name='list_campaign'),
    # GET : Load form to create new campaign
    # POST : Load data to create new campaign
    url(r'^add_campaign/$', views.add_campaign, name='add_campaign'),
)