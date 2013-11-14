from django.shortcuts import render
from ElectionSimulation.Models.Campaign import Campaign
from ElectionSimulation.Models.Formula import Formula
from ElectionSimulation.Models.PoliticalParty import PoliticalParty
from django.core.context_processors import csrf
from django.shortcuts import render_to_response


def list_campaign(request):
    """ Get the list of all campaigns and render the list
    """

    context = {'campaigns': Campaign.objects.all()}
    return render(request, 'User/list.html', context)

