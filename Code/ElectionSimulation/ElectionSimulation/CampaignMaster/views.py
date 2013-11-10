from django.shortcuts import render
from ElectionSimulation.models import Campaign

def listCampaign(request):
    #c = Campaign(name="What's new?", create_date=timezone.now())
    context = {'campaigns': Campaign.objects.all()}
    return render(request, 'CampaignMaster/list.html', context)