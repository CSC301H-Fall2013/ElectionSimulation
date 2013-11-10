from django.conf.urls import patterns, url

from ElectionSimulation.CampaignMaster import views

urlpatterns = patterns('',
    url(r'^$', views.list_campaign, name='list_campaign'), # Show the list of current campaigns
    url(r'^add/$', views.add_new_campaign, name='add_new_campaign'), # Show the list of current campaigns
)