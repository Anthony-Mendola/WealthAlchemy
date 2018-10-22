from django.contrib import admin

from .models import Offering

class OfferingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'is_open', 'minimum_investment', 'industry', 'offer_date', 'affiliate')
  list__display_links = ('id', 'title')
  list__filter = ('affiliate',)
  list__editable = ('is_published',)
  search_fields = ('title', 'description', 'industry', 'annual_interest', 'term', 'category', 'minimum_investment')
  list__per_page = 25

admin.site.register(Offering, OfferingAdmin)