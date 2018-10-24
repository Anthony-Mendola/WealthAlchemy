from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='offerings'),
  path('<int:offering_id>', views.offering, name='offering'),
  path('search', views.search, name='search')
]