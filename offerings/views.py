from django.shortcuts import render

def index(request):
  return render(request, 'offerings/offerings.html')

def offering(request):
  return render(request, 'offerings/offering.html')

def search(request):
  return render(request, 'offerings/search.html')

