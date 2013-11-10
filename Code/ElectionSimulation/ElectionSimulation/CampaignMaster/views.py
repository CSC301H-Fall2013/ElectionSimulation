from django.shortcuts import render
from ElectionSimulation.Models.Campaign import Campaign

def listCampaign(request):
    """ Get the list of all campaigns and render the list
    """

    #c = Campaign(name="What's new?", create_date=timezone.now())
    context = {'campaigns': Campaign.objects.all()}
    return render(request, 'CampaignMaster/list.html', context)