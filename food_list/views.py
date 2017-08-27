from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from .models import DailyFoodList, Food
from .forms import AddFoodToDayForm

def index(request):
    try:
        recent_days_list = DailyFoodList.objects.order_by('-entry_date')[:7]
    except DailyFoodList.DoesNotExist:
        raise Http404("Cannot find daily meal plans.")
    template = loader.get_template("food_list/index.html")
    context = {
        'recent_days_list': recent_days_list,
    }
    return HttpResponse(template.render(context, request))

def daily_list(request, dailyfoodlist_id):
    # TODO: this should list meals and the foods eaten at each meal.
    try:
        daily_food_list = DailyFoodList.objects.get(pk=dailyfoodlist_id)
    except DailyFoodList.DoesNotExist:
        raise Http404("Food list does not exist for this day.")
    foods_to_eat = daily_food_list.food_text.all()
    entry_date = daily_food_list.entry_date
    total_cals = 0
    for item in foods_to_eat:
        total_cals += item.calorie_amount * item.number_of_servings
    template = loader.get_template("food_list/daily_list.html")
    context = {
        'foods_to_eat': foods_to_eat,
        'total_cals': total_cals,
        'entry_date': entry_date
    }
    return HttpResponse(template.render(context, request))

def food_index(request):
    try:
        list_of_foods = Food.objects.order_by('food_text')
    except Food.DoesNotExist:
        raise Http404("Cannot find list of foods.")
    template = loader.get_template("food_list/food_index.html")
    context = {
        'list_of_foods': list_of_foods,
    }
    return HttpResponse(template.render(context, request))

def food(request, food_id):
    try:
        food = Food.objects.get(pk=food_id)
    except Food.DoesNotExist:
        raise Http404("Food is not in our system yet.")
    template = loader.get_template("food_list/food_detail.html")
    context = {
        'food': food,
    }
    return HttpResponse(template.render(context, request))

def add_food(request):
    form = AddFoodToDayForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            # food_to_add = 
            day_to_add = form.cleaned_data['day_to_add']
            no_servings = form.cleaned_data['no_servings']
            request.session['add_food'] = request.POST['add_food']
            return HttpResponseRedirect('/Food added!/')
        else:
            form = AddFoodToDayForm()
        return render(request, 'food_detail.html', {'form': form})
    