from django.db import models

class DailyFoodList(models.Model):
    entry_date = models.DateTimeField('date of food')

class Food(models.Model):
    day_eaten = models.ForeignKey(DailyFoodList, on_delete=models.CASCADE)
    food_text = models.CharField(max_length=200)
    calorie_amount = models.IntegerField(default=0)