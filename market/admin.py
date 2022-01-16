from django.contrib import admin
from .models import Company, CurrentMarketData, HistoricalMarketData

# Register your models here.

admin.site.register(Company)
admin.site.register(CurrentMarketData)
admin.site.register(HistoricalMarketData)
