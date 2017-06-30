from django.contrib import admin

from .models import DailyFoodList, Food

admin.site.register(DailyFoodList)
admin.site.register(Food)
