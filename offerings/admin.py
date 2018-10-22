from django.contrib import admin

from .models import Offering

class OfferingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'is_open', 'minimum_investment', 'industry', 'offer_date', 'affiliate')
  list_display_links = ('id', 'title')
  list_filter = ('affiliate',)
  list_editable = ('is_published',)
  search_fields = ('title', 'description', 'industry', 'annual_interest', 'term', 'category', 'minimum_investment')
  list_per_page = 25

admin.site.register(Offering, OfferingAdmin)