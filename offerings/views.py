from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import interest_choices, minimum_choices, term_choices, industry_choices

from .models import Offering

def index(request):
  offerings = Offering.objects.order_by('-offer_date').filter(is_published=True)

  paginator = Paginator(offerings, 3)
  page = request.GET.get('page')
  paged_offerings = paginator.get_page(page)

  context = {
    'offerings': paged_offerings
  }
  return render(request, 'offerings/offerings.html', context)

def offering(request, offering_id):
  offering = get_object_or_404(Offering, pk=offering_id)

  context = {
    'offering': offering
  }

  return render(request, 'offerings/offering.html', context)

def search(request):
  queryset_list = Offering.objects.order_by('-offer_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # Term
  if 'term' in request.GET:
    term = request.GET['term']
    if term:
      queryset_list = queryset_list.filter(term__lte=term)

  # Industry
  if 'industry' in request.GET:
    industry = request.GET['industry']
    if industry:
      queryset_list = queryset_list.filter(industry__iexact=industry)

  # Interest
  if 'annual_interest' in request.GET:
    annual_interest = request.GET['annual_interest']
    if annual_interest:
      queryset_list = queryset_list.filter(annual_interest__gte=annual_interest)

  # minimum
  if 'minimum_investment' in request.GET:
    minimum_investment = request.GET['minimum_investment']
    if minimum_investment:
      queryset_list = queryset_list.filter(minimum_investment__lte=minimum_investment)

  context = {
     'interest_choices': interest_choices,
      'minimum_choices': minimum_choices,
      'term_choices': term_choices,
      'industry_choices': industry_choices,
      'offerings': queryset_list,
      'values': request.GET
  }
  return render(request, 'offerings/search.html', context)

