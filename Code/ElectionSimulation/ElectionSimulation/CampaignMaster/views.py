from django.shortcuts import render
from ElectionSimulation.Models.Campaign import Campaign
from django.utils import timezone
from django.http import HttpResponseRedirect
def list_campaign(request):
    """ Get the list of all campaigns and render the list
    """

    context = {'campaigns': Campaign.objects.all()}
    return render(request, 'CampaignMaster/list.html', context)


def add_new_campaign(request):
    """ Add a new campaign
    """

    return render(request, 'CampaignMaster/addNewCampaign.html')
    
def add(request):
    Campaign_Name = request.POST.get('Campaign_Name', "")
    date = request.POST.get("date", "")
    new_campaign = Campaign(name = Campaign_Name, create_date = date)
    new_campaign.save()
    
    return HttpResponseRedirect('/campaign_master/add_new_campaign/')
    