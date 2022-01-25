from django.contrib import admin
from .models import Client, Adset, MediaCost, DailyImpression, DailyClick, DailyConversion, DailyRevenue

admin.site.register(Client)
admin.site.register(Adset)
admin.site.register(MediaCost)
admin.site.register(DailyImpression)
admin.site.register(DailyClick)
admin.site.register(DailyConversion)
admin.site.register(DailyRevenue)
