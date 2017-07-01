from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import DailyFoodList

def index(request):
    recent_days_list = DailyFoodList.objects.order_by('-entry_date')[:7]
    template = loader.get_template("food_list/index.html")
    context = {
        'recent_days_list': recent_days_list,
    }
    return HttpResponse(template.render(context, request))

def daily_list(request, dailyfoodlist_id):
    response = "Meal plan for %s:"
    return HttpResponse(response % dailyfoodlist_id)
