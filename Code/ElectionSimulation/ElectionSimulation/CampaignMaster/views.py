from django.shortcuts import render

def index(request):
    context = {'name': 'Minh'}
    #return render(request, 'CampaignMaster/index.html', context)
    return render(request, 'CampaignMaster/list.html', context)