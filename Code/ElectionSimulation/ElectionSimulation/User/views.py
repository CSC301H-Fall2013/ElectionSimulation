from django.shortcuts import render
from ElectionSimulation.Models.Campaign import Campaign
from ElectionSimulation.Models.Formula import Formula
from ElectionSimulation.Models.PoliticalParty import PoliticalParty
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
import random
import datetime
import time

def list_campaign(request):
    """ Get the list of all campaigns and render the list
    """

    context = {'campaigns': Campaign.objects.all()}
    return render(request, 'User/list.html', context)

def show_candidate_effort_form_form(request):
    context = {}
    context['campaigns'] = Campaign.v  
    return render(request,'User/add_candidate_effort.html', context)


def add_new_candidate_effort(request):
    # Get basic information about the campaign
    campaign_name = request.POST.get('campaign_name', "")
    # Get the list of candidates
    candidates = ""
    effort_list = []
    for i in range(1, 11):
        candidate_effort = request.POST.get("age_group_" + str(i), "")
        effort_list.append(candidate_effort)
    
    # Get the formula system and voting system
    # Create new campaign
    return show_candidate_effort_form_form(request)  

    
def add_candidate_effort(request):
    """ GET : Open the form to add new campaign
        POST : Add a new campaign
    """

    if request.method == 'GET':
        return show_candidate_effort_form_form(request)
    elif request.method == 'POST':
        return add_new_candidate_effort(request)
     