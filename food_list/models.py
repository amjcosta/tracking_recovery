from django.db import models

class Food(models.Model):
    food_text = models.CharField(max_length=200)
    calorie_amount = models.IntegerField(default=0)
    serving_size = models.CharField(max_length=200)
    number_of_servings = models.DecimalField(max_digits=100, decimal_places=3)
    def __str__(self):
        return self.food_text

class DailyFoodList(models.Model):
    # TODO: This needs to accommodate a list of foods that are associated with a date.
    # Ideally, associated with a certain meal on a certain date.
    entry_date = models.DateTimeField('date of food')
    food_text = models.ForeignKey(Food, on_delete=models.CASCADE)
    def __str__(self):
        return self.entry_date.strftime("%B %d, %Y")
