from django import forms

from .models import DailyFoodList, Food

class AddFoodToDayForm(forms.Form):
    day_to_add = forms.DateField(label="Add this food to date")
    no_servings = forms.FloatField(label="Number of servings")
    # food_to_add = forms.CharField()
