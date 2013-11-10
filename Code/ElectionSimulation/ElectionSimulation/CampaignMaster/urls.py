from django.conf.urls import patterns, url

from ElectionSimulation.CampaignMaster import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)