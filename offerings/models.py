from django.db import models
from datetime import datetime
from affiliates.models import Affiliate

class Offering(models.Model):
  affiliate = models.ForeignKey(Affiliate, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  originator = models.CharField(max_length=200, blank=True)
  industry = models.CharField(max_length=100)
  location = models.CharField(max_length=100, blank=True)
  category = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  minimum_investment = models.IntegerField()
  annual_interest = models.IntegerField()
  percent_funded = models.IntegerField(default=0)
  current_funded = models.IntegerField(default=0)
  offering_size = models.IntegerField(blank=True)
  term = models.IntegerField(blank=True)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  is_open = models.BooleanField(default=True)
  offer_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title
