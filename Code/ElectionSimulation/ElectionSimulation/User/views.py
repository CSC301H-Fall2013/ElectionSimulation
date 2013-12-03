from django.shortcuts import render
from ElectionSimulation.Models.Campaign import Campaign
from ElectionSimulation.Models.Formula import Formula
from ElectionSimulation.Models.PoliticalParty import PoliticalParty
from ElectionSimulation.Models.CTract import CTract
from ElectionSimulation.Models.PStation import PStation
from ElectionSimulation.Models.Link import Link
from ElectionSimulation.Models.Result import Result
from ElectionSimulation.Models.Expenses import Expenses
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
    context['campaigns'] = Campaign.objects.all()  
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

def piechart(request):
    """ Show the piechart for the user 
    """
    context = {'Result': Result.objects.all()}
    return render(request,'User/piechart.html', context)

def add_new_candidate_effort(request):
    # Get basic information about the campaign
    campaign_name = request.POST.get('campaign_name', "")
    effort_list = []
    for i in range(1, 11):
        candidate_effort = request.POST.get("age_group_" + str(i), "")
        effort_list.append(candidate_effort)

    ct_to_pd = {}
    key = 0
    for lnk in Link.objects.all():
        key = str(getattr(lnk, 'ctuid'))
        if (not(key in ct_to_pd)):
            ct_to_pd[key] = [getattr(lnk, 'pd_num')]
        else:
            ct_to_pd[key].append(getattr(lnk, 'pd_num'))

    pd_to_tots = {}
    pd_to_votes = {}
    for ps in PStation.objects.all():
        key = str(getattr(ps, 'pd_num'))
        if (not(key in pd_to_tots)):
            pd_to_tots[key] = [getattr(ps, 'tot_votes')]
            pd_to_votes[key] = [getattr(ps, 'votes')]
        else:
            pd_to_tots[key].append(getattr(ps, 'tot_votes'))
            pd_to_votes[key].append(getattr(ps, 'votes'))

    ct_to_ages = {}
    for ct in CTract.objects.all():
        key = str(getattr(ct, 'ctuid'))
        for i in range(1, 11):
            if (not(key in ct_to_ages)):
                ct_to_ages[key] = [getattr(ct, 'age_' + str(i))]
            else:
                ct_to_ages[key].append(getattr(ct, 'age_' + str(i)))

    exp_effort = []
    for exp in Expenses.objects.all():
        exp_effort.append(float(getattr(exp, 'expense'))/getattr(exp, 'expense_ceiling'))

    #sum of ctracts per cand 
        #sum of pstations in ctract * dotproduct of effort_age and Ct demogs
    expected_cand_vote_prop = [0, 0, 0]
    for i in range(3): #should be replaced with number of candidates.
        #s = 0
        d_prod = 0
        temp = 0
        for ct in ct_to_ages:
            for j in range(10):
                d_prod += ct_to_ages[ct][j]*float(effort_list[j])
            pd_arr = ct_to_pd[ct]
            for k in range(len(pd_arr)):
                #s += float(pd_to_tots[str(pd_arr[k])][i])
                temp += float(pd_to_votes[str(pd_arr[k])][i])
            expected_cand_vote_prop[i] += exp_effort[i]*(temp)


    #normalize the proportions
    #s = sum(sorted(expected_cand_vote_prop))
    expected_cand_vote_prop = [int(elem) for elem in expected_cand_vote_prop]
    context = {'Result': expected_cand_vote_prop}
    
    return render(request,'User/piechart.html', context)
     
