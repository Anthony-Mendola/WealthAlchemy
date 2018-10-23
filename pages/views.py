from django.shortcuts import render
from django.http import HttpResponse

from affiliates.models import Affiliate
from offerings.models import Offering

def index(request):
    offerings = Offering.objects.order_by('-offer_date').filter(is_published=True)[:3]

    context = {
      'offerings': offerings
    }
    return render(request, 'pages/index.html', context)

def about(request):
  #get all affiliates
    affiliates = Affiliate.objects.order_by('-hire_date')


    #get affiliate of the month
    mvp_affiliates = Affiliate.objects.all().filter(is_mvp=True)

    context = {
      'affiliates': affiliates,
      'mvp_affiliates': mvp_affiliates
    }
    return render(request, 'pages/about.html', context)

