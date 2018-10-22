from django.shortcuts import render

from .models import Offering

def index(request):
  offerings = Offering.objects.all()

  context = {
    'offerings': offerings
  }
  return render(request, 'offerings/offerings.html', context)

def offering(request):
  return render(request, 'offerings/offering.html')

def search(request):
  return render(request, 'offerings/search.html')

