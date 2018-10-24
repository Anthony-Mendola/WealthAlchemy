from django.shortcuts import get_object_or_404, render
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
  offering = get_object_or_404(Offering, pk=offering_id)

  context= {
    'offering': offering
  }

  return render(request, 'offerings/offering.html', context)

def search(request):
  return render(request, 'offerings/search.html')

