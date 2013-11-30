from django.conf.urls import patterns, url

from ElectionSimulation.User import views

urlpatterns = patterns('',
    # GET : Show the list of current campaigns
    url(r'^$', views.list_campaign, name='list_campaign'),
    url(r'^add_candidate_effort/$', views.add_candidate_effort, name='add_candidate_effort'),
    # GET : Load form to create new campaign
)