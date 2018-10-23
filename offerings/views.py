from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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
  return render(request, 'offerings/offering.html')

def search(request):
  return render(request, 'offerings/search.html')

