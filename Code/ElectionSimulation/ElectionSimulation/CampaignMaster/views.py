from django.shortcuts import render
from ElectionSimulation.Models.Campaign import Campaign


def list_campaign(request):
    """ Get the list of all campaigns and render the list
    """

    context = {'campaigns': Campaign.objects.all()}
    return render(request, 'CampaignMaster/list.html', context)


def add_new_campaign(request):
    """ Add a new campaign
    """

    return render(request, 'CampaignMaster/addNewCampaign.html')