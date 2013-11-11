# This file manage top level url pattern that will direct to subsections of the site
from django.conf.urls import patterns, include, url
from django.contrib import admin
from ElectionSimulation.login.views import login, auth_view
admin.autodiscover()
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^campaign_master/', include('ElectionSimulation.CampaignMaster.urls')), # Campaign master's pages
    url(r'^login/$', login),
    url(r'^auth/$', auth_view),
    #url(r'^logout/$', logout),
    #url(r'^loggedin/$', loggedin),
    
    
    )
