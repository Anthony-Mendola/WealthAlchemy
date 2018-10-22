from django.contrib import admin

from .models import Affiliate

class AffiliateAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email', 'experience')
  list_display_links = ('id', 'name')
  search_fields = ('name',)
  list_per_page = 25


admin.site.register(Affiliate, AffiliateAdmin)