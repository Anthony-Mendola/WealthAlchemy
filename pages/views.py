from django.shortcuts import render
from django.http import HttpResponse
from offerings.choices import interest_choices, minimum_choices, term_choices, industry_choices

from affiliates.models import Affiliate
from offerings.models import Offering

def index(request):
    offerings = Offering.objects.order_by('-offer_date').filter(is_published=True)[:3]

    context = {
      'offerings': offerings,
      'interest_choices': interest_choices,
      'minimum_choices': minimum_choices,
      'term_choices': term_choices,
      'industry_choices': industry_choices

    }
    return render(request, 'pages/index.html', context)

def about(request):
  #get all affiliates
    affiliates = Affiliate.objects.order_by('-experience')


    #get affiliate of the month
    mvp_affiliates = Affiliate.objects.all().filter(is_mvp=True)

    context = {
      'affiliates': affiliates,
      'mvp_affiliates': mvp_affiliates
    }
    return render(request, 'pages/about.html', context)

