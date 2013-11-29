from django.shortcuts import render
from ElectionSimulation.Models.Campaign import Campaign
from ElectionSimulation.Models.Formula import Formula
from ElectionSimulation.Models.PoliticalParty import PoliticalParty
from django.core.context_processors import csrf
from django.shortcuts import render_to_response


def list_campaign(request):
    """ Get the list of all campaigns and render the list
    """

    context = {'campaigns': Campaign.objects.all(), 'full_name': request.user.username}
    return render(request, 'CampaignMaster/list.html', context)


def show_add_campaign_form(request):
    context = {}
    context['full_name'] = request.user.username
    # Load list of formula
    context['formulas'] = Formula.objects.all()
    # Must load list of voting system
    context['voting_systems'] = ['Single-winner',
                                 'Multiple-winner',
                                 'Proxy voting',
                                 'Random selection',
                                 'Social choice theory',
                                 'Politics portal']
    context['parties'] = PoliticalParty.objects.all()
    return render(request, 'CampaignMaster/addNewCampaign.html', context)


def add_new_campaign(request):
    # Get basic information about the campaign
    campaign_name = request.POST.get('campaign_name', "")
    # Get the list of candidates
    candidate_count = int(request.POST.get('candidate_count', ""))
    candidates = ""
    for i in range(0, candidate_count):
        candidate_name = request.POST.get("candidate_name_" + str(i), "")
        candidate_party = request.POST.get("candidate_party_" + str(i), "")
        if candidate_name.strip() != "":
            candidates = candidates + candidate_name + chr(10)
            candidates = candidates + candidate_party + chr(10)
    # Get the formula system and voting system
    formula = request.POST.get('formula', "")
    voting_system = request.POST.get('voting_system', "")
    # Create new campaign
    new_campaign = Campaign(name=campaign_name,
                            candidates=candidates,
                            formula=Formula.objects.get(id=formula),
                            voting_system=voting_system)
    # Add into DB
    new_campaign.save()
    return render('CampaignMaster/addNewCampaign.html', {'full_name': request.user.username})


def add_campaign(request):
    """ GET : Open the form to add new campaign
        POST : Add a new campaign
    """

    if request.method == 'GET':
        return show_add_campaign_form(request)
    elif request.method == 'POST':
        return add_new_campaign(request)