from django.conf.urls import patterns, url

from ElectionSimulation.User import views

urlpatterns = patterns('',
    # GET : Show the list of current campaigns
    url(r'^$', views.list_campaign, name='list_campaign'),
    # GET : Load form to create new campaign
)